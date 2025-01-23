from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StudyRecord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='study_record')
    hours_studied = models.DecimalField(max_digits=7, decimal_places=1, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.hours_studied} hours"