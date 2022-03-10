from django.db import models

class Assigned_Tutor(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    tutor = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.course}: {self.tutor}"
