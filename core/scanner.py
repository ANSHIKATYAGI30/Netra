from core.camera import Camera
from core.detector import QRDetector
from core.history import ScanHistory
from core.utils import Utils


class Scanner:
    """
    Main scanning engine for Netra.
    Responsible for:
    - Reading camera frames
    - Detecting QR codes
    - Avoiding duplicate scans
    - Saving scan history
    """

    def __init__(self):
        self.camera = Camera()
        self.detector = QRDetector()
        self.history = ScanHistory()

        # Last successfully scanned QR
        self.last_scan = None

    def start(self):
        """Start the webcam."""
        self.camera.start()

    def stop(self):
        """Stop the webcam."""
        self.camera.stop()

    def get_frame(self):
        """
        Returns:
            frame (OpenCV image)
            results (list of detected QR codes)
        """

        success, frame = self.camera.read_frame()

        if not success:
            return False, None, []

        results = self.detector.detect(frame)

        processed_results = []

        for qr in results:

            data = qr["data"]

            qr_type = Utils.detect_qr_type(data)

            # Avoid duplicate scans
            if data != self.last_scan:

                self.last_scan = data

                self.history.save_scan(
                    qr_type,
                    data
                )

            processed_results.append(
                {
                    "type": qr_type,
                    "data": data,
                    "points": qr["points"]
                }
            )

        return True, success, frame, processed_results

    def reset_last_scan(self):
        """
        Allows scanning the same QR again.
        """

        self.last_scan = None