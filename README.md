
# Job Portal (Real-Time Job Analyzer)

A Django-based Job Portal Web Application that allows users to search, scrape, and analyze real-time job postings from online job boards. The project provides a simple interface for job seekers to find opportunities and explore hiring trends.

---

## Features

* Job Search & Scraping – Enter a job title and fetch real-time jobs
* Job Searching Option - Search by typing field name or search the job by uploading cv, the app will automatically analyze the skills and search jobs according to the cv
* Organized Listings – Display job title, company, and location
* Responsive UI – Works on desktop and mobile devices
* Django-Powered – Secure backend with CSRF protection
* Extendable – Easy to add job analytics (top roles, skills, locations)

---

## Tech Stack

* Backend: Django (Python)
* Frontend: HTML5, CSS3 (inline styles for simplicity, responsive support)
* Database: SQLite (default, can be switched to PostgreSQL/MySQL)
* Scraping: BeautifulSoup / Selenium (for live job extraction)

---

## Project Structure

```
Job_Portal/
│── job_portal/        # Main Django project (settings, urls, wsgi, asgi)
│── home/              # App for job scraping and displaying results
│── templates/         # HTML templates (frontend)
│── manage.py          # Django project manager
│── db.sqlite3         # Database (ignored in production)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
```

---

## Installation & Setup

1. Clone the repository

   ```bash
   git clone https://github.com/Shayankhan123-dev/Job_Portal.git
   cd Job_Portal
   ```

2. Create and activate virtual environment

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations

   ```bash
   python manage.py migrate
   ```

5. Create superuser (for admin access)

   ```bash
   python manage.py createsuperuser
   ```

6. Run development server

   ```bash
   python manage.py runserver
   ```

   Open in browser: `http://127.0.0.1:8000/`

---

## Usage

* Open the site and search for job titles (e.g., Python Developer, Data Scientist).
* Scraped jobs will be displayed with title, company, location, and link.
* Extend the project to include data analysis dashboards for top skills, salaries, and cities.

---

## Responsive Design

Added the following meta tag in HTML templates to support mobile devices:

```
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

## Contribution

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Add feature"`)
4. Push to branch (`git push origin feature-name`)
5. Create a Pull Request

---

## License

This project is licensed under the MIT License.
