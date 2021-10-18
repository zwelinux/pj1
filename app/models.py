from django.db import models
# inhertance


# Create your models here.

class TaskType(models.Model):
	task_name = models.CharField(max_length=255)

	def __str__(self):
		return self.task_name

class Task(models.Model):
	title = models.CharField(max_length=255)
	task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
	content = models.TextField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	date = models.DateField()

	def __str__(self):
		return self.title 