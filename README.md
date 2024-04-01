# ULD (URL List Downloader)

ULD (URL List Downloader) is a lightweight Python application designed to simplify the process of downloading multiple files from a list of URLs. Whether you're a content creator, researcher, or simply someone who frequently needs to download files from a list of URLs, ULD streamlines the task and saves you time.

## Key Features:

### 1. Easy URL List Management
ULD allows you to effortlessly manage and download files from a list of URLs stored in a text file. Simply create a text file containing the URLs you want to download, and ULD will handle the rest.

### 2. Fast and Reliable Downloads
Powered by the robust `requests` library, ULD ensures fast and reliable downloads of files from each URL in your list. It automatically handles HTTP requests and efficiently downloads files in the background.

### 3. Progress Monitoring with Visual Feedback
With the integration of the `tqdm` library, ULD provides real-time progress monitoring with visually appealing progress bars. You can track the download progress of each file and know exactly how much time is remaining.

### 4. Seamless Integration into Your Workflow
ULD is designed to seamlessly integrate into your existing workflow. Whether you prefer to run it from the command line or incorporate it into your Python scripts, ULD offers flexibility and ease of use.

### 5. Cross-Platform Compatibility
Built using Python, ULD is compatible with Windows, macOS, and Linux operating systems, ensuring that you can use it on any platform without compatibility issues.

## Prerequisites

Before running the app, make sure you have the following modules installed:

- [requests](https://pypi.org/project/requests/): This module is used for making HTTP requests. It's commonly used for downloading files from URLs. Install it by running:
  

```bash
pip install requests
```

- [tqdm](https://pypi.org/project/tqdm/): This module is used to create progress bars. It's not strictly necessary for the functionality of the code, but it provides a nice visual representation of the download progress. Install it by running:
  
```bash
pip install tqdm
```  


## Usage

To use the ULD (URL List Downloader) app, follow these steps:

1. **Prepare Your URL List File**: Create a text file containing a list of URLs that you want to download.

2. **Navigate to the App Directory**: Open your terminal or command prompt and navigate to the directory where the ULD app is located.

3. **Run the App**: Enter one of the following commands in your terminal or command prompt:

    ```bash
    python ULD.v0.1.py
    ```

    or

    ```bash
    python3 ULD.v0.1.py
    ```

   Replace `ULD.v0.1.py` with the actual filename of the ULD app if it's different.

4. **Follow the Prompts**: The app will prompt you to provide the path to the text file containing your list of URLs.

5. **Sit Back and Relax**: The app will then proceed to download each URL from the list.

**That's it! Enjoy using ULD!**
