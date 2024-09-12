import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import yt_dlp as youtube_dl

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.resizable(False, False)
        self.create_widgets()
        self.apply_styles()

    def create_widgets(self):
        label = tk.Label(self.root, text="YouTube Downloader", font=("Helvetica", 24, "bold"), background="#212a54")
        label.pack(pady=5)

        file_frame = tk.Frame(self.root)
        file_frame.pack(padx=20, pady=5, fill="x")

        link_text = ScrolledText(self.root, wrap=tk.WORD, height=10, width=80, font=("Helvetica", 10))
        link_text.pack(padx=20, pady=(0, 5))
        self.link_text = link_text  # Store link_text as a member variable

        self.link_entry = tk.Entry(self.root, width=80)
        self.link_entry.pack(padx=20, pady=(0, 5))

        add_button = ttk.Button(self.root, text="Add Link", command=self.add_link)
        add_button.pack(padx=20, pady=(0, 5))

        delete_button = ttk.Button(self.root, text="Delete Links", command=self.delete_links)
        delete_button.pack(padx=20, pady=(0, 5))

        download_button = ttk.Button(self.root, text="Download Videos", command=self.download_videos)
        download_button.pack(padx=20, pady=(0, 5))

        self.output_text = ScrolledText(self.root, wrap=tk.WORD, height=10, width=40, font=("Ariel", 10))
        self.output_text.pack(padx=20, pady=(0, 10))

    def add_link(self):
        link = self.link_entry.get()
        if link:
            self.link_text.insert(tk.END, link + "\n")
            self.link_entry.delete(0, tk.END)

    def delete_links(self):
        self.link_text.delete(1.0, tk.END)

    def download_videos(self):
        self.output_text.delete(1.0, tk.END)
        file_path = "../mp3_player"

        # Get all the links from the text box
        links = self.link_text.get(1.0, tk.END).strip().split("\n")

        for link in links:
            try:
                self.output_text.insert(tk.END, f"Downloading: {link}\n")
                self.output_text.update()  # Ensure the UI stays responsive

                ydl_opts = {
                    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
                    'outtmpl': './MP3 player/%(title)s.%(ext)s',
                    'ignoreerrors': True  # Skip unavailable videos
                }

                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                self.output_text.insert(tk.END, f"Downloaded: {link}\n")
            except youtube_dl.utils.DownloadError as e:
                # Skip video if it's unavailable or has an error
                self.output_text.insert(tk.END, f"Error: {str(e)}\nSkipping to the next video...\n")
                continue  # Skip to the next link

            except Exception as e:
                self.output_text.insert(tk.END, f"Unexpected error: {str(e)}\n")
                continue  # Skip to the next link if any other exception occurs

        self.output_text.update()  # Ensure the output text widget updates

    def apply_styles(self):
        self.root.configure(bg="#212a54")  # Background color

        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="black", foreground="black")  # Change button colors here
        style.map("TButton", background=[("active", "#333333")])  # Change active button color here

        # Adding hover effect
        style.map("TButton",
                  background=[("active", "#333333"),
                              ("!active", "black")])

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()