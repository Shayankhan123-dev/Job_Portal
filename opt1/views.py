from django.shortcuts import render, redirect
from .models import Job
from .scraper import scrape_rozee_jobs

def job_list(request):
    jobs = Job.objects.all()
    return render(request, "opt1/job_list.html", {"jobs": jobs})

def scrape_jobs(request):
    if request.method == "POST":
        search_term = request.POST.get("search_term")  # 👈 get user input
    else:
        search_term = "Data Scientist"  # fallback default

    # Scrape fresh jobs with user query
    scraped_jobs = scrape_rozee_jobs(search_term, "Karachi", pages=2)

    # Save to database (only if new)
    for job in scraped_jobs:
        Job.objects.get_or_create(
            title=job.get("title") or "N/A",
            company=job.get("company") or "N/A",
            location=job.get("location") or "N/A",
            link=job.get("link") or "https://rozee.pk",
        )

    # Redirect to job list page after saving
    return redirect("opt1")
