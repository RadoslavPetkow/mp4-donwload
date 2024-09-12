Here's a README file for your YouTube Downloader application:

---

# YouTube Video Downloader

This is a simple desktop application built using Python's `tkinter` library and `yt_dlp` for downloading YouTube videos. The app provides a graphical user interface (GUI) for managing and downloading videos from YouTube.

## Features

- **Add YouTube Links:** Input and add YouTube video URLs to a list.
- **Delete Links:** Clear all added links from the list.
- **Download Videos:** Download videos in the best available quality.
- **Display Status:** Shows progress and status of the downloads in the GUI.

## Requirements

To run this application, you need Python installed along with the following libraries:

- `tkinter` (included with Python standard library)
- `yt_dlp` (YouTube video downloader)

You can install `yt_dlp` using pip:

```bash
pip install yt-dlp
```

## Usage

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd <project-directory>
   ```

3. **Run the Application:**

   ```bash
   python your_script_name.py
   ```

4. **Using the Application:**
   - **Add Links:** Enter a YouTube URL in the entry field and click "Add Link" to add it to the list.
   - **Delete Links:** Click "Delete Links" to remove all links from the list.
   - **Download Videos:** Click "Download Videos" to start downloading the videos from the list.

## Code Overview

- **`YouTubeDownloaderApp` Class:** This is the main class for the application that sets up the GUI, manages user interactions, and handles video downloading.
  - **`create_widgets` Method:** Creates and packs the GUI components.
  - **`add_link` Method:** Adds a YouTube URL to the list.
  - **`delete_links` Method:** Clears all URLs from the list.
  - **`download_videos` Method:** Downloads videos from the URLs in the list and handles errors.
  - **`apply_styles` Method:** Applies custom styles to the GUI components.

## Troubleshooting

- Ensure that `yt_dlp` is installed correctly.
- Make sure the application has permission to write files to the specified output directory.
- If you encounter any issues or errors, check the console for detailed error messages.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust any details based on your actual setup or preferences!
