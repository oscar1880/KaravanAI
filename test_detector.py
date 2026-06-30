from pathlib import Path

from core.detector import Detector

detector = Detector()

video = Path("/Users/hsyn_mac/Desktop/1.mp4")

events = detector.scan_video(video)

for e in events:
    print(e)

print()
print("Toplam:", len(events))