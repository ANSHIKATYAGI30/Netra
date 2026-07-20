import customtkinter as ctk

class ResultPanel(ctk.CTkFrame):
    """
    Displays the latest scan details.
    """

    def __init__(self, master):
        super().__init__(master)
        self.configure(width=300)
        
        title = ctk.CTkLabel(
            self,
            text="Latest Scan",
            font=("Segoe UI", 22, "bold")
        )

        title.pack(
            pady=(20, 15)
        )

        self.type_label = ctk.CTkLabel(
            self,
            text="Type: ---",
            anchor="w",
            font=("Segoe UI", 16)
        )

        self.type_label.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.time_label = ctk.CTkLabel(
            self,
            text="Time: ---",
            anchor="w",
            font=("Segoe UI", 16)
        )

        self.time_label.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.content_box = ctk.CTkTextbox(
            self,
            height=220
        )

        self.content_box.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        self.content_box.insert(
            "1.0",
            "Waiting for scan..."
        )

        self.content_box.configure(
            state="disabled"
        )

    def update_result(
        self,
        qr_type,
        data,
        timestamp
    ):

        self.type_label.configure(
            text=f"Type : {qr_type}"
        )

        self.time_label.configure(
            text=f"Time : {timestamp}"
        )

        self.content_box.configure(
            state="normal"
        )

        self.content_box.delete(
            "1.0",
            "end"
        )

        self.content_box.insert(
            "1.0",
            data
        )

        self.content_box.configure(
            state="disabled"
        )

    def clear(self):

        self.type_label.configure(
            text="Type : ---"
        )

        self.time_label.configure(
            text="Time : ---"
        )

        self.content_box.configure(
            state="normal"
        )

        self.content_box.delete(
            "1.0",
            "end"
        )

        self.content_box.insert(
            "1.0",
            "Waiting for scan..."
        )

        self.content_box.configure(
            state="disabled"
        )