from django.db import models

class Job(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    code = models.IntegerField()
    archived = models.BooleanField(default=False)

