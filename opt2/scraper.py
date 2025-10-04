import time
import os
from pypdf import PdfReader
import docx
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# ===== Brave Driver Setup =====
def get_brave_driver():
    brave_path = r"C:\Users\arsal\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
    chromedriver_path = r"D:\realTimeJobAnalyzer\job_portal\chromedriver.exe"  # <-- update if needed

    options = Options()
    options.binary_location = brave_path
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# ===== Extract Skills/Keywords from CV =====
def extract_keywords_from_cv(cv_file_path):
    text = ""
    if cv_file_path.endswith(".pdf"):
        reader = PdfReader(open(cv_file_path, "rb"))
        for page in reader.pages:
            text += page.extract_text()
    elif cv_file_path.endswith(".docx"):
        doc = docx.Document(cv_file_path)
        for para in doc.paragraphs:
            text += para.text

    # 🔑 Expandable skill dictionary
    skills_list = ["Python", "Machine Learning", "Data Science", "SQL", "Django", "Java", "C++", "AWS", "React", "Flutter"]
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]

    return found_skills if found_skills else ["Software Engineer"]


# ===== Scraper Function =====
def scrape_rozee_jobs(search_terms, location="Karachi", pages=1):
    """
    search_terms = list of keywords (from CV)
    """
    driver = get_brave_driver()
    jobs_data = []

    try:
        for term in search_terms:
            base_url = f"https://www.rozee.pk/job/jsearch/q/{term.replace(' ', '-')}/l/{location.replace(' ', '-')}"
            driver.get(base_url)

            for page in range(1, pages + 1):
                print(f"Scraping {term} - Page {page}...")

                try:
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.job"))
                    )
                except:
                    print(f"⚠️ No job cards found for {term}.")
                    break

                job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job")
                for card in job_cards:
                    try:
                        title_elem = card.find_element(By.CSS_SELECTOR, "h3 a")
                        title = title_elem.text.strip()
                        link = title_elem.get_attribute("href")
                    except:
                        title, link = "N/A", None

                    try:
                        company = card.find_element(By.CSS_SELECTOR, "span.company-name").text.strip()
                    except:
                        company = "N/A"

                    try:
                        location_elem = card.find_element(By.CSS_SELECTOR, "span.job-location")
                        location_text = location_elem.text.strip()
                    except:
                        location_text = "N/A"

                    jobs_data.append({
                        "title": title,
                        "company": company,
                        "location": location_text,
                        "link": link,
                        "matched_skill": term
                    })

                # next page
                try:
                    next_button = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
                    driver.execute_script("arguments[0].click();", next_button)
                    time.sleep(3)
                except:
                    print(f"No more pages found for {term}.")
                    break

    finally:
        driver.quit()

    return jobs_data


# ===== Test Run =====
if __name__ == "__main__":
    # Example CV test
    cv_path = r"D:\realTimeJobAnalyzer\job_portal\sample_cv.pdf"
    skills = extract_keywords_from_cv(cv_path)
    print("Extracted skills:", skills)

    results = scrape_rozee_jobs(skills, "Karachi", pages=1)
    for job in results:
        print(job)
