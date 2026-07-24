from dataclasses import dataclass
from datetime import datetime
import os
import pandas as pd

@dataclass
class ScanRecord:
    """
    Represents a single scan entry.
    """

    timestamp: str
    qr_type: str
    data: str


class ScanHistory:
    """
    Handles reading and writing scan history.
    """

    def __init__(self):

        self.history_dir = "history"
        self.history_file = os.path.join(
            self.history_dir,
            "scans.csv"
        )

        self._create_history()

    def _create_history(self):

        os.makedirs(
            self.history_dir,
            exist_ok=True
        )

        if not os.path.exists(self.history_file):

            df = pd.DataFrame(
                columns=[
                    "Timestamp",
                    "Type",
                    "Data"
                ]
            )

            df.to_csv(
                self.history_file,
                index=False
            )

    def save_scan(
        self,
        qr_type,
        data
    ):

        record = ScanRecord(
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            qr_type=qr_type,
            data=data
        )

        row = pd.DataFrame(
            [
                {
                    "Timestamp": record.timestamp,
                    "Type": record.qr_type,
                    "Data": record.data
                }
            ]
        )

        row.to_csv(
            self.history_file,
            mode="a",
            header=False,
            index=False
        )

    def load_history(self):

        return pd.read_csv(
            self.history_file
        )

    def clear_history(self):

        df = pd.DataFrame(
            columns=[
                "Timestamp",
                "Type",
                "Data"
            ]
        )

        df.to_csv(
            self.history_file,
            index=False
        )
