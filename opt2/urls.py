from django.urls import path
from . import views

urlpatterns = [
    path("upload-cv/", views.upload_cv_and_recommend_jobs, name="opt2"),
]
