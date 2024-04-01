import tkinter as tk
from tkinter import filedialog, messagebox
import requests
import os
import threading
import time
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class DownloadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Download Manager")
        
        self.url_label = tk.Label(root, text="URL List File:")
        self.url_label.grid(row=0, column=0, padx=5, pady=5)

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.dir_label = tk.Label(root, text="Destination Directory:")
        self.dir_label.grid(row=1, column=0, padx=5, pady=5)

        self.dir_entry = tk.Entry(root, width=50)
        self.dir_entry.grid(row=1, column=1, padx=5, pady=5)

        self.dir_button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.dir_button.grid(row=1, column=2, padx=5, pady=5)

        self.download_button = tk.Button(root, text="Download", command=self.download)
        self.download_button.grid(row=2, column=1, padx=5, pady=5)

        self.download_info_label = tk.Label(root, text="")
        self.download_info_label.grid(row=3, columnspan=3, padx=5, pady=5)

        self.progress_frame = tk.Frame(root)
        self.progress_frame.grid(row=4, columnspan=3, padx=5, pady=5)

        self.progress_label = tk.Label(self.progress_frame, text="Progress:")
        self.progress_label.grid(row=0, column=0, padx=5, pady=5)

        self.progress_bar = tk.Canvas(self.progress_frame, width=200, height=20, bg="white")
        self.progress_bar.grid(row=0, column=1, padx=5, pady=5)

        self.percentage_label = tk.Label(self.progress_frame, text="")
        self.percentage_label.grid(row=0, column=2, padx=5, pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, file_path)

    def browse_directory(self):
        dir_path = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, dir_path)

    def download(self):
        url_list_file = self.url_entry.get()
        download_dir = self.dir_entry.get()

        if not url_list_file or not download_dir:
            messagebox.showerror("Error", "Please select URL list file and destination directory")
            return

        threading.Thread(target=self.start_download, args=(url_list_file, download_dir)).start()

    def start_download(self, url_list_file, download_dir):
        with open(url_list_file, 'r') as file:
            total_urls = sum(1 for _ in file)
            file.seek(0)
            for index, url in enumerate(file, start=1):
                url = url.strip()
                self.download_file(url, download_dir)
                self.update_progress(index, total_urls)

    def download_file(self, url, download_dir, max_retries=5):
        filename = url.split('/')[-1]
        file_path = os.path.join(download_dir, filename)
        retries = 0
        while retries < max_retries:
            try:
                with requests.get(url, stream=True, verify=False) as response:
                    response.raise_for_status()
                    with open(file_path, 'wb') as file:
                        start_time = time.time()
                        total_length = response.headers.get('content-length')
                        if total_length:
                            total_length = int(total_length)
                            downloaded = 0
                            for chunk in response.iter_content(chunk_size=8192):
                                file.write(chunk)
                                downloaded += len(chunk)
                                percent = (downloaded / total_length) * 100
                                self.update_progress_bar(percent)
                                current_time = time.time()
                                download_speed = downloaded / (current_time - start_time)
                                download_speed /= 1024  # Convert to KB/s
                                download_speed_str = f"{download_speed:.2f} KB/s"
                                downloaded_size = downloaded / (1024 * 1024)  # Convert to MB
                                total_size_mb = total_length / (1024 * 1024)  # Convert to MB
                                self.update_progress_info(filename, download_speed_str, f"{downloaded_size:.2f} MB", f"{total_size_mb:.2f} MB")
                        else:
                            file.write(response.content)
                return  # Download successful
            except (requests.exceptions.RequestException, ConnectionResetError) as e:
                print(f"Failed to download {url}: {e}")
                retries += 1
                time.sleep(5)  # Wait before retrying
        print(f"Download of {url} failed after {max_retries} retries.")

    def update_progress(self, current, total):
        progress_percent = (current / total) * 100
        print(f"Progress: {progress_percent:.2f}%")

    def update_progress_bar(self, percent):
        self.progress_bar.delete("progress")
        self.progress_bar.create_rectangle(0, 0, percent*2, 20, fill="blue", tags="progress")
        self.percentage_label.config(text=f"{percent:.2f}%")

    def update_progress_info(self, filename, download_speed, downloaded_size, total_size):
        self.download_info_label.config(text=f"Downloading: {filename}\nSpeed: {download_speed}\nDownloaded: {downloaded_size}/{total_size}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DownloadApp(root)
    root.mainloop()
