from django.db import models

# Create your models here.

class Module(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.2/ref/models/fields/
  course = models.ForeignKey(
      'course',
      on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  content = models.CharField(max_length=255)

  def __str__(self):
    # This must return a string
    return f"{self.name} in {self.course}"

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'course': self.course,
        'name': self.name,
        'content': self.content,
    }
