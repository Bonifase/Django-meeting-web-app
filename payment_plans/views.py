import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import stripe
from .models import MeetingPlan
from users.models import Customer

stripe.api_key = os.getenv('STRIPE_PUBLISHABLE_KEY', None)


@user_passes_test(lambda user: user.is_superuser)
def update_accounts(request):
    customers = Customer.objects.all()
    for customer in customers:
        subscription = stripe.Subscription.retrieve(
            customer.stripe_subscription_id
        )
        if subscription.status == 'active':
            customer.membership = False
        else:
            customer.membership = True
        customer.cancel_at_period_end = subscription.cancel_at_period_end
        customer.save()
        return HttpResponse('Completed')


@login_required
def plans(request):
    plans = MeetingPlan.objects
    return render(request, 'plans/plans.html', {'plans': plans})


@login_required
def plan(request, pk):
    template = 'plans/plan.html'
    plan = get_object_or_404(MeetingPlan, pk=pk)

    if plan.premium:
        if request.user.is_authenticated:
            try:
                if request.user.customer.membership:
                    return render(request, template, {'plan': plan})
            except Customer.DoesNotExist:
                return redirect('plans:join')

        return redirect('plans:join')
    else:
        return render(request, template, {'plan': plan})


@login_required
def join(request):
    return render(request, 'plans/join.html')


@login_required
def checkout(request):
    try:
        if request.user.customer.membership:
            return redirect('users:settings')
    except Customer.DoesNotExist:
        pass
    coupons = {
        'haloween': 31,
        'welcome': 10
    }
    if request.method == 'POST':
        stripe_customer = stripe.Customer.create(
            email=request.user.email,
            source=request.POST['stripeToken']
        )
        plan = os.getenv('MONTHLY', None)
        if request.POST['plan'] == 'yearly':
            plan = os.getenv('YEARLY', None)
        if request.POST['coupon'] in coupons:
            percentage = coupons[request.POST['coupon'].lower()]
            try:
                coupon = stripe.Coupon.create(
                    duration='once',
                    id=request.POST['coupon'].lower(),
                    percent_off=percentage
                )
            except Exception:
                pass
            subscriprion = stripe.Subscription.create(
                customer=stripe_customer.id,
                items=[{'plan': plan}],
                coupon=request.POST['coupon'].lower()
            )
        else:
            subscriprion = stripe.Subscription.create(
                customer=stripe_customer.id,
                items=[{'plan': plan}]
            )
        customer = Customer()
        customer.user = request.user
        customer.stripe_id = stripe.customer.id
        customer.membership = True
        customer.cancel_at_period_end = False
        customer.stripe_subscription_id = subscriprion.id
        customer.save()
        return redirect('website:home')
    else:
        plan = 'monthly'
        coupon = 'none'
        price = 1000
        og_dollar = 10
        coupon_dollar = 0
        final_dollar = 10
        if request.method == 'GET' and 'plan' in request.GET:
            if request.GET['plan'] == 'yearly':
                plan = 'yearly'
                price = 10000
                og_dollar = 100
                final_dollar = 100
        if request.method == 'GET' and 'coupon' in request.GET:
            if request.GET['coupon'].lower() in coupons:
                coupon = request.GET['coupon'].lower()
                percentage = coupons[coupons]
                coupons_price = int(percentage / 100) * price
                price = price - coupons_price
                coupon_dollar = (
                    str(coupons_price[:-2]) + '.' + str(coupons_price[-2:])
                    )
                final_dollar = str(price[:-2]) + '.' + str(price[-2:])
        return render(
            request,
            'plans/checkout.html',
            {
                'plan': plan, 'coupon': coupon,
                'price': price, 'og_dollar': og_dollar,
                'coupon_dollar': coupon_dollar,
                'final_dollar': final_dollar
            }
        )


@login_required
def unsubscribe(request):
    return render(request, 'plans/unsubscribe')


@login_required
def settings(request):
    template = 'users/settings.html'
    membership = False
    if request.method == 'POST':
        subscription = stripe.Subscription.retrieve(
            request.user.stripe_subscription_id
        )
        subscription.cancel_at_period_end = True
        request.user.customer.cancel_at_period_end = True
        cancel_at_period_end = True
        subscription.save()
    else:
        try:
            if request.user.customer.membership:
                membership = True
            if request.user.customer.cancel_at_period_end:
                cancel_at_period_end = True
        except Customer.DoesNotExist:
            pass
    return render(
        request,
        template,
        {
            'membership': membership,
            'cancel_at_period_end': cancel_at_period_end
        }
    )
  