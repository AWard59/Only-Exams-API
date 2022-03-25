from django.db import models

from .completed_module import Completed_Module

# Create your models here.

class Module(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  course = models.ForeignKey(
      'course',
      on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  content = models.TextField()
  completed = models.CharField(max_length=100, default="")

  completed_module = models.ManyToManyField('User', through=Completed_Module, through_fields=(
      'module_complete', 'student'), related_name='module_students', blank=True)

  def __str__(self):
    # This must return a string
    return f"{self.name} in {self.course}"

  def as_dict(self):
    """Returns dictionary version of module models"""
    return {
        'id': self.id,
        'course': self.course,
        'name': self.name,
        'content': self.content,
    }
