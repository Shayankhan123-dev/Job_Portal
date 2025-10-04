import time
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

# ===== Scraper Function =====
def scrape_rozee_jobs(search_term="Data Scientist", location="Karachi", pages=1):
    driver = get_brave_driver()
    jobs_data = []

    try:
        base_url = f"https://www.rozee.pk/job/jsearch/q/{search_term.replace(' ', '-')}/l/{location.replace(' ', '-')}"
        driver.get(base_url)

        for page in range(1, pages + 1):
            print(f"Scraping page {page}...")

            # wait until job cards appear
            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.job"))
                )
            except:
                print("⚠️ No job cards found on this page.")
                break

            # extract job details
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
                    "link": link
                })

            # try to click next page
            try:
                next_button = driver.find_element(By.CSS_SELECTOR, "a[rel='next']")
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(3)
            except:
                print("No more pages found.")
                break

    finally:
        driver.quit()

    return jobs_data


# ===== Test Run =====
if __name__ == "__main__":
    results = scrape_rozee_jobs("Python Developer", "Karachi", pages=2)
    for job in results:
        print(job)

