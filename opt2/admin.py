from django.contrib import admin
from .models import UploadedCV, RecommendedJob

@admin.register(UploadedCV)
class UploadedCVAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "uploaded_at")
    search_fields = ("id",)
    ordering = ("-uploaded_at",)

@admin.register(RecommendedJob)
class RecommendedJobAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "company", "location", "matched_skill", "recommended_at")
    search_fields = ("title", "company", "location", "matched_skill")
    list_filter = ("location", "recommended_at")
    ordering = ("-recommended_at",)
