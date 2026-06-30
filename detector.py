from pathlib import Path

class Detector:
    def __init__(self):
        from ultralytics import YOLO
        self.model = YOLO("yolo11n.pt")
        self.targets = {2:"car",7:"truck"}

    def scan_folder(self, folder: Path):
        # Geçici iskelet. Video tarama sonraki aşamada eklenecek.
        events=[]
        for f in sorted(folder.glob("*.mp4")):
            print("Hazır:", f.name)
        return events
