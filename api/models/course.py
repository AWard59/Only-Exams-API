from django.db import models
from django.contrib.auth import get_user_model

from .assigned_tutors import Assigned_Tutor
from .enrolled_course import Enrolled_Course

# Create your models here.
class Course(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=255)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )
  assigned_tutors = models.ManyToManyField('User', through=Assigned_Tutor, through_fields=('course', 'tutor'), related_name='tutors', blank=True)

  enrolled_courses = models.ManyToManyField('User', through=Enrolled_Course, through_fields=('course', 'student'), related_name='students', blank=True)

  def __str__(self):
    # This must return a string
    return f"{self.name} by {self.owner}."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'owner': self.owner
    }
