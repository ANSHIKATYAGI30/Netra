import re
import webbrowser
from datetime import datetime

import pyperclip


class Utils:
    """
    Utility functions for Netra.
    """

    @staticmethod
    def detect_qr_type(data: str) -> str:
        """
        Detect the type of QR code content.
        """

        if not data:
            return "UNKNOWN"

        data = data.strip()

        # Website
        if data.startswith(("http://", "https://")):
            return "URL"

        # Email
        if data.startswith("mailto:"):
            return "EMAIL"

        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", data):
            return "EMAIL"

        # Phone
        if data.startswith("tel:"):
            return "PHONE"

        # WiFi
        if data.startswith("WIFI:"):
            return "WIFI"

        # UPI
        if data.startswith("upi://"):
            return "UPI"

        # SMS
        if data.startswith("SMSTO:"):
            return "SMS"

        # Geo Location
        if data.startswith("geo:"):
            return "LOCATION"

        # Contact Card
        if data.startswith(("BEGIN:VCARD", "MECARD:")):
            return "CONTACT"

        # Calendar Event
        if data.startswith("BEGIN:VEVENT"):
            return "EVENT"

        return "TEXT"

    @staticmethod
    def copy_to_clipboard(text: str):
        """
        Copy text to clipboard.
        """

        if text:
            pyperclip.copy(text)

    @staticmethod
    def open_url(url: str):
        """
        Open a URL in the default browser.
        """

        if url.startswith(("http://", "https://")):
            webbrowser.open(url)

    @staticmethod
    def current_timestamp():
        """
        Return current timestamp.
        """

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")