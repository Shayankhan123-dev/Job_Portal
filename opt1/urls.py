from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_list, name="opt1"),
    path("scrape/", views.scrape_jobs, name="scrape_jobs"),
]
