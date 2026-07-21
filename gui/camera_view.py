import tkinter as tk
from PIL import Image, ImageTk
import cv2

class CameraView(tk.Frame):
    """
    Widget responsible for displaying the live camera feed.
    """

    def __init__(self, master):
        super().__init__(master, bg="#202020")

        self.label = tk.Label(
            self,
            bg="black"
        )
        self.label.pack(
            fill="both",
            expand=True
        )

        self.current_image = None

    def update_frame(self, frame):
        """
        Display an OpenCV frame.
        """
        if frame is None:
            return

        # Convert BGR → RGB
        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(rgb)

        self.current_image = ImageTk.PhotoImage(image)

        self.label.configure(
            image=self.current_image
        )

    def clear(self):

        self.label.configure(
            image=""
        )
        self.current_image = None
