from django.db import models

# Create your models here.
class employees(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	emp_id=models.IntegerField()

	def __self__(self):
		return self.firstname

