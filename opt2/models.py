from django.db import models
from django.utils import timezone

class UploadedCV(models.Model):
    file = models.FileField(upload_to="cvs/")
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"CV {self.id} uploaded at {self.uploaded_at}"


class RecommendedJob(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    matched_skill = models.CharField(max_length=100, blank=True, null=True)
    recommended_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} at {self.company}"
