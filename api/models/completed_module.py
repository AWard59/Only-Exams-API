from django.db import models

class Completed_Module(models.Model):
    module_complete = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='module_complete')
    student = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
      return f"{self.completed_module}: {self.student}"
