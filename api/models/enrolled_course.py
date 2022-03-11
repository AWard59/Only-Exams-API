from django.db import models

class Enrolled_Course(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    student = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.course}: {self.student}"
