import customtkinter as ctk
import cv2
from datetime import datetime

from core.scanner import Scanner
from core.utils import Utils

from gui.sidebar import Sidebar
from gui.toolbar import Toolbar
from gui.live_view import LiveView
from gui.result_panel import ResultPanel
from gui.statusbar import StatusBar

from tkinter import filedialog

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ---------------- Window ---------------- #

        self.title("👁 Netra - Intelligent Vision Suite")
        self.geometry("1400x800")
        self.minsize(1200, 700)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ---------------- Scanner ---------------- #

        self.scanner = Scanner()

        self.camera_running = False

        self.latest_data = ""
        self.latest_type = ""

        # ---------------- Layout ---------------- #

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.main_frame.grid_columnconfigure(0, weight=3)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Toolbar

        self.toolbar = Toolbar(self.main_frame)
        self.toolbar.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=10
        )

        # Camera View

        self.live_view = LiveView(self.main_frame)
        self.live_view.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # Result Panel

        self.result_panel = ResultPanel(self.main_frame)
        self.result_panel.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # Status Bar

        self.statusbar = StatusBar(self.main_frame)
        self.statusbar.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=10,
            pady=(0, 10)
        )

        # ---------------- Button Bindings ---------------- #

        self.toolbar.start_btn.configure(
            command=self.start_camera
        )

        self.toolbar.stop_btn.configure(
            command=self.stop_camera
        )

        self.toolbar.copy_btn.configure(
            command=self.copy_result
        )

        self.toolbar.open_btn.configure(
            command=self.open_result
        )

        self.toolbar.clear_btn.configure(
            command=self.clear_result
        )

        # Image scan will be implemented later
        self.toolbar.image_btn.configure(
            command=self.scan_image
        )

        # Handle Window Close

        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    # =====================================================
    # Camera Controls
    # =====================================================

    def start_camera(self):

        if self.camera_running:
            return

        try:
            self.scanner.start()

            self.camera_running = True

            self.sidebar.set_status(True)

            self.statusbar.update_status(
                "Camera Started"
            )

            # Live update loop starts in Part 2
            self.update_camera()

        except Exception as e:

            self.statusbar.update_status(str(e))

            self.live_view.show_message(
                "Unable to access camera."
            )

    def stop_camera(self):

        if not self.camera_running:
            return

        self.camera_running = False

        self.scanner.stop()

        self.sidebar.set_status(False)

        self.statusbar.update_status(
            "Camera Stopped"
        )

        try:
            self.live_view.clear()
        except AttributeError:
            pass

        self.statusbar.update_status("Camera Stopped")

    # =====================================================
    # Toolbar Actions
    # =====================================================

    def copy_result(self):

        if self.latest_data:

            Utils.copy_to_clipboard(
                self.latest_data
            )

            self.statusbar.update_status(
                "Copied to clipboard"
            )

    def open_result(self):

        if self.latest_type == "URL":

            Utils.open_url(
                self.latest_data
            )

            self.statusbar.update_status(
                "Opening URL..."
            )

    def clear_result(self):

        self.latest_data = ""
        self.latest_type = ""

        self.result_panel.clear()

        self.statusbar.update_status(
            "Result Cleared"
        )

    def scan_image(self):
        path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
            (
                "Images",
                "*.png *.jpg *.jpeg *.bmp"
            )
        ]
        )
        if not path:
            return
        
        image = cv2.imread(path)
        if image is None:
            return
        
        results = self.scanner.detector.detect(image)

        if not results:
            self.statusbar.update_status("No QR Code Found")
        return

        qr = results[0]

        self.latest_type = Utils.detect_qr_type(qr["data"])

        self.latest_data = qr["data"]

        self.update_result_panel(self.latest_type,self.latest_data)

        image = self.draw_results(
            image,[
            {
                "type": self.latest_type,
                "data": self.latest_data,
                "points": qr["points"]
            }
            ])

        self.live_view.update_frame(image)

    # =====================================================
    # Placeholder
    # =====================================================

       # =====================================================
    # Live Camera Loop
    # =====================================================

    def update_camera(self):
        if not self.camera_running:
            return
        
        success, frame, results = self.scanner.get_frame()
        if success:
            frame = self.draw_results(
            frame,
            results
            )

        self.live_view.update_frame(frame)
        
        self.after(
        30,
        self.update_camera
        )

    def draw_results(self, frame, results):
        if not results:
            return frame
        
        for qr in results:
            points = qr["points"]
            
            for i in range(4):
                cv2.line(
                frame,
                tuple(points[i]),
                tuple(points[(i + 1) % 4]),
                (0,255,0),
                2
            )

            qr_type = qr["type"]
            qr_data = qr["data"]

            self.latest_type = qr_type
            self.latest_data = qr_data

            self.update_result_panel(
            qr_type,
            qr_data
            )

            cv2.putText(
            frame,
            qr_type,
            (
                points[0][0],
                points[0][1]-10
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

        return frame
    
    def update_result_panel(self, qr_type, qr_data):
        timestamp = datetime.now().strftime(
        "%H:%M:%S"
        )
        try:
            self.result_panel.update_result(
            qr_type,
            qr_data,
            timestamp
        )

        except AttributeError:
            pass

        self.statusbar.update_status(f"Detected : {qr_type}")

    # =====================================================
    # Cleanup
    # =====================================================

    def on_close(self):
        try:
            self.stop_camera()

        except Exception:
            pass
        
        self.destroy()