from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(max_length=500, unique=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
