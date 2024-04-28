import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


def get_instagram_stories(username, download_folder):
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
        url_input.send_keys(f"{username}")

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
        return False

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
    # Example = r"C:\Users\PC\Downloads\InstaDownloader\"
    # Example = r"/home/kali/Downloads/InstaDownloader/"
    # User id      ↓
    username = "jiri_mdf"
    ######################################################################

    stories_folder = os.path.join(download_folder, "Stories")
    if not os.path.exists(stories_folder):
        os.makedirs(stories_folder)

    downloaded_links_file = os.path.join(download_folder, "downloaded_links.txt")
    if not os.path.exists(downloaded_links_file):
        with open(downloaded_links_file, "w"):
            pass

    task_file_path = os.path.join(download_folder, 'task.txt')
    if not os.path.exists(task_file_path):
        with open(task_file_path, 'w') as task_file:
            task_file.write(f'{datetime.now()} - The script ran\n')

    if not get_instagram_stories(username, download_folder):
        return False

run_script()
