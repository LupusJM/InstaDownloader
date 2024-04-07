import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import urllib.parse


def get_instagram_stories(url, download_folder):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://fastdl.app/")

    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Consent']"))
        )
        cookies_button.click()

        url_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='url']"))
        )
        url_input.send_keys(url)

        url_input.submit()

        close_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'ads-modal-close')]"))
        )
        close_button.click()

        time.sleep(10)

        download_buttons = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.ID, "download-btn"))
        )

        for index, download_button in enumerate(download_buttons):
            download_url = download_button.get_attribute("href")
            media_type = download_button.get_attribute("data-mediatype")

            username = urllib.parse.urlparse(url).path.split('/')[2]

            if media_type.lower() == "image":
                extension = "jpg"
            else:
                extension = "mp4"

            download_date = datetime.now().strftime("%d%m%Y")
            filename = os.path.join(download_folder, "Stories", f"LupusDownloader_{username}_{download_date}_{index + 1}.{extension}")

            if not is_already_downloaded(download_url, download_folder):
                response = requests.get(download_url)
                with open(filename, 'wb') as file:
                    file.write(response.content)
                record_downloaded_link(download_url, download_folder)
            else:
                print(f"Link already downloaded: {download_url}")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()


def is_already_downloaded(download_url, download_folder):
    downloaded_links_file = os.path.join(download_folder, "downloaded_links.txt")
    if os.path.exists(downloaded_links_file):
        with open(downloaded_links_file, "r") as f:
            return download_url in f.read()
    return False


def record_downloaded_link(download_url, download_folder):
    downloaded_links_file = os.path.join(download_folder, "downloaded_links.txt")
    with open(downloaded_links_file, "a") as f:
        f.write(download_url + "\n")


def run_script():

    ######################################################################
    # Folder
    download_folder = r"(YOUR FOLDER PATH)"
    # Example = r"C:\Users\PC\Downloads\InstaDownloader"
    # Example = r"/home/kali/Downloads/InstaDownloader/"
    # User                                                 User id ↓
    instagram_stories_url = "https://www.instagram.com/stories/jiri_mdf/0"
    ######################################################################


    stories_folder = os.path.join(download_folder, "Stories")
    if not os.path.exists(stories_folder):
        os.makedirs(stories_folder)

    downloaded_links_file = os.path.join(download_folder, "downloaded_links.txt")
    if not os.path.exists(downloaded_links_file):
        with open(downloaded_links_file, "w"):
            pass

    get_instagram_stories(instagram_stories_url, download_folder)

    # Recording the run time in the task.txt file
    with open(os.path.join(download_folder, 'task.txt'), 'a') as file:
        file.write(f'{datetime.now()} - The script ran\n')

run_script()
