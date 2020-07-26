from django.urls import path
from .views import meetings, meeting, new_meeting

app_name = 'meetings'
urlpatterns = [
    path('meetings', meetings, name='meetings'),
    path('meetings/<int:id>', meeting, name='meeting_detail'),
    path('meetings/new', new_meeting, name='new')
]