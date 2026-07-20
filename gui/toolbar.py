import customtkinter as ctk


class Toolbar(ctk.CTkFrame):
    """
    Top toolbar for Netra.

    This widget only creates the buttons.
    Their functionality will be connected
    inside main_window.py.
    """

    def __init__(self, master):
        super().__init__(master)

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self):

        self.start_btn = ctk.CTkButton(
            self,
            text="▶ Start Camera",
            width=140
        )

        self.stop_btn = ctk.CTkButton(
            self,
            text="⏹ Stop",
            width=110
        )

        self.image_btn = ctk.CTkButton(
            self,
            text="🖼 Scan Image",
            width=140
        )

        self.copy_btn = ctk.CTkButton(
            self,
            text="📋 Copy",
            width=100
        )

        self.open_btn = ctk.CTkButton(
            self,
            text="🌐 Open URL",
            width=120
        )

        self.clear_btn = ctk.CTkButton(
            self,
            text="🗑 Clear",
            width=100
        )

    def _layout_widgets(self):

        self.start_btn.pack(
            side="left",
            padx=8,
            pady=10
        )

        self.stop_btn.pack(
            side="left",
            padx=8,
            pady=10
        )

        self.image_btn.pack(
            side="left",
            padx=8,
            pady=10
        )

        self.copy_btn.pack(
            side="left",
            padx=8,
            pady=10
        )

        self.open_btn.pack(
            side="left",
            padx=8,
            pady=10
        )

        self.clear_btn.pack(
            side="left",
            padx=8,
            pady=10
        )