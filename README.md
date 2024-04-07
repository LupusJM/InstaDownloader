# Instagram Stories Downloader

This script allows you to download Instagram stories from any public account.<br>
You can also automate the script to run at system startup, for example, every 2 hours using Task Scheduler.


## How it works

The script operates in several steps:

1. **Opening Web Browser**: The script initiates a headless web browser session using Selenium WebDriver.

2. **Navigating to Download Page**: It directs the browser to the webpage, which facilitates content downloading from social media platforms.

3. **Inputting Instagram Story URL**: The user provides the URL of the Instagram story they wish to download.

4. **Identifying and Downloading Media**: The script identifies the type of media (images or videos) present in the story and proceeds to download them to the specified directory.

5. **Recording Downloaded Links**: To avoid redundant downloads, the script maintains a record of `downloaded_links.txt`.

6. **Recording Run Time**: The script records the time of execution in the `task.txt` file, providing a log of script runs.

7. **Error Handling**: The script includes error-handling mechanisms to deal with unexpected situations, ensuring smooth execution.

By following these steps, the script enables users to conveniently download Instagram stories for offline viewing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/LupusJM/InstaDownloader.git
    ```

3. Install Dependencies:

   ```bash
   pip install requests selenium urllib3
   ```

## Usage

1. **Configuration**:
   - Modify the \`download_folder\` variable to your target directory. You can right-click on the script, choose "Open With" and select Notepad. Then, change the \`download_folder\` variable to point to your desired folder path.
   - Update the \`instagram_stories_url\` variable with the URL of the Instagram story you want to download.

2. **Run the Script**:

   ```bash
   python main.py
   ```
3. **Enjoy your files**:
<br>

![LupusDownloader](https://github.com/LupusJM/InstaDownloader/assets/163419314/b4130af9-a9a2-4adb-8e7a-dd08d8dc488f)
> LupusDownloader\_{username}\_{download\_date}\_{index + 1}.\{extension\}

5. **Automation with Task Scheduler**: Optionally, you can automate the script to run at system startup or at regular intervals using Task Scheduler. This allows you to schedule the script to run, for example, every 2 hours for periodic updates.


## Notes

- This script requires the Google Chrome browser and its driver suitable for your operating system.
- Remember that downloading content from social media platforms may be restricted by copyright and Instagram's terms of service.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/lupusjm/InstaDownloader/blob/main/LICENSE)
