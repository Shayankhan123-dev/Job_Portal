from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CVUploadForm
from .models import UploadedCV, RecommendedJob
from .scraper import extract_keywords_from_cv, scrape_rozee_jobs
from datetime import datetime
import os
import traceback

def upload_cv_and_recommend_jobs(request):
    if request.method == "POST":
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            cv_instance = form.save()

            try:
                cv_path = cv_instance.file.path

                # extract skills
                skills = extract_keywords_from_cv(cv_path)
                print("Extracted skills:", skills)

                # run scraper
                jobs = scrape_rozee_jobs(skills, location="Karachi", pages=1)

                # save jobs
                for job in jobs:
                    RecommendedJob.objects.get_or_create(
                        link=job.get("link"),
                        defaults={
                            "title": job.get("title"),
                            "company": job.get("company"),
                            "location": job.get("location"),
                            "matched_skill": job.get("matched_skill"),
                            "recommended_at": datetime.now(),
                        },
                    )

                all_jobs = RecommendedJob.objects.all().order_by("-recommended_at")
                return render(request, "opt2/recommendations.html", {"jobs": all_jobs, "skills": skills})

            except Exception as e:
                error_message = f"❌ Failed: {str(e)}\n\n{traceback.format_exc()}"
                return HttpResponse(f"<pre>{error_message}</pre>", status=500)
    else:
        form = CVUploadForm()

    return render(request, "opt2/upload_cv.html", {"form": form})
