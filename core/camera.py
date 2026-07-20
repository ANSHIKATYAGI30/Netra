import cv2
import threading

class Camera:
    """
    Handles background thread-safe webcam stream operations.
    """
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None
        self.is_running = False
        self.frame = None
        self.lock = threading.Lock()
        self.thread = None

    def start(self):
        if self.is_running:
            return
        
        self.cap = cv2.VideoCapture(
        self.camera_index,
        cv2.CAP_DSHOW
        )
        
        if not self.cap.isOpened():
            raise Exception("Unable to access webcam.")
        
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        self.is_running = True

        self.thread = threading.Thread(
        target=self._update_loop,
        daemon=True
        )
        self.thread.start()
    
    def _update_loop(self):
        """Continuously pulls frames into an internal buffer."""
        while self.is_running:
            success, frame = self.cap.read()
            if success:
                with self.lock:
                    self.frame = frame.copy()

    def read_frame(self):
        """Returns the latest frame snapshot from the thread buffer."""
        with self.lock:
            if self.frame is not None:
                return True, self.frame.copy()
            return False, None

    def stop(self):
        """Gracefully release the webcam hardware and stop execution threads."""
        self.is_running = False
        if self.thread is not None:
            self.thread.join(timeout=1.0)
            self.thread = None
            
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def is_open(self):
        """Returns True if webcam is active."""
        return self.cap is not None