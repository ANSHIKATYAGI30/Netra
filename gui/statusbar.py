import customtkinter as ctk


class StatusBar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=35)

        self.pack_propagate(False)

        self.status = ctk.CTkLabel(
            self,
            text="Ready",
            anchor="w"
        )

        self.status.pack(
            side="left",
            padx=15
        )

        self.fps = ctk.CTkLabel(
            self,
            text="FPS: --"
        )

        self.fps.pack(
            side="right",
            padx=15
        )

    def update_status(self, text):
        self.status.configure(text=text)

    def update_fps(self, fps):
        self.fps.configure(text=f"FPS: {fps}")