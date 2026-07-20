import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import time

class LiveView(ctk.CTkFrame):
    """
    Displays the live camera feed.
    """
    def __init__(self, master):
        super().__init__(master)

        self.configure(corner_radius=15)

        self.image_label = ctk.CTkLabel(
            self,
            text="Camera Offline",
            font=("Segoe UI", 18, "bold")
        )

        self.image_label.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.current_image = None

    def update_frame(self, frame):
        """
        Display an OpenCV frame inside the GUI.
        """
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(rgb)
        self.current_image = ImageTk.PhotoImage(image)
        self.image_label.configure(
            image=self.current_image,
            text=""
        )

    def show_message(self, message):
        """
        Show a centered message when no camera/image is displayed.
        """
        self.image_label.configure(
            image=None,
            text=message
        )
        self.current_image = None

    def clear(self):
        self.show_message("Camera Offline")