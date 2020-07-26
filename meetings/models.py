from django.db import models
from datetime import time


class Meeting(models.Model):
    """Meeting model."""

    class MeetingType(models.TextChoices):
        STATUS_UPDATE = 'SU', ('Status Update')
        INFORMATION_SHARING = 'IS', ('Information Sharing')
        DECISION_MAKING = 'DM', ('Decision Making')
        PROBLEM_SOLVING = 'PS', ('Problem Solving')
        INNOVATION = 'IN', ('Innovation')
        TEAM_BUILDING = 'TB', ('Team Building')

    title = models.CharField(max_length=255)
    meeting_type = models.CharField(
        max_length=2,
        choices=MeetingType.choices,
        default=MeetingType.STATUS_UPDATE,
    )
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} at {self.start_time} on {self.date}'
