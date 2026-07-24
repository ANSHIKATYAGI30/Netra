import cv2

class QRDetector:
    """
    Handles QR code detection and decoding.
    """
    
    def __init__(self):
        self.detector = cv2.QRCodeDetector()

    def detect(self, frame):
        """
        Detect QR codes in a frame.
        Returns:
            List of dictionaries
        """
        results = []

        # Try detecting multiple QR codes
        success, decoded_info, points, _ = self.detector.detectAndDecodeMulti(frame)

        if success:
            for text, box in zip(decoded_info, points):
                if not text:
                    continue
                corners = []
                for point in box:
                    corners.append(
                        (
                            int(point[0]),
                            int(point[1])
                        )
                    )
                results.append(
                    {
                        "data": text,
                        "points": corners
                    }
                )
            return results

        # Fallback to single QR detection
        text, points, _ = self.detector.detectAndDecode(frame)

        if text and points is not None:
            corners = []
            for point in points[0]:
                corners.append(
                    (
                        int(point[0]),
                        int(point[1])
                    )
                )

            results.append(
                {
                    "data": text,
                    "points": corners
                }
            )

        return results
