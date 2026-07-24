import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    """
    Left navigation sidebar.
    """
    def __init__(self, master):
        super().__init__(master, width=220, corner_radius=0)
        self.grid_rowconfigure(10, weight=1)
        self.logo = ctk.CTkLabel(
            self,
            text="👁 NETRA",
            font=("Segoe UI", 26, "bold")
        )
        self.logo.pack(pady=(25, 5))
        self.subtitle = ctk.CTkLabel(
            self,
            text="Intelligent Vision Suite",
            font=("Segoe UI", 13)
        )

        self.subtitle.pack(pady=(0, 30))

        self.scan_btn = ctk.CTkButton(
            self,
            text="📷 Live Scanner"
        )

        self.scan_btn.pack(fill="x", padx=20, pady=8)

        self.image_btn = ctk.CTkButton(
            self,
            text="🖼 Scan Image"
        )

        self.image_btn.pack(fill="x", padx=20, pady=8)

        self.history_btn = ctk.CTkButton(
            self,
            text="📄 History"
        )

        self.history_btn.pack(fill="x", padx=20, pady=8)

        self.settings_btn = ctk.CTkButton(
            self,
            text="⚙ Settings"
        )

        self.settings_btn.pack(fill="x", padx=20, pady=8)

        self.status_title = ctk.CTkLabel(
            self,
            text="Status",
            font=("Segoe UI", 16, "bold")
        )

        self.status_title.pack(pady=(40, 5))

        self.status = ctk.CTkLabel(
            self,
            text="🔴 Camera Offline",
            font=("Segoe UI", 14)
        )

        self.status.pack()

    def set_status(self, online=True):

        if online:
            self.status.configure(text="🟢 Camera Online")
        else:
            self.status.configure(text="🔴 Camera Offline")
