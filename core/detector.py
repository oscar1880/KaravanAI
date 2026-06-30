from pathlib import Path
import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.model=YOLO('yolo11n.pt')
        self.target_classes={2:'car',7:'truck'}

    def scan_video(self, video_path: Path):
        events=[]
        cap=cv2.VideoCapture(str(video_path))
        fps=cap.get(cv2.CAP_PROP_FPS) or 30
        frame=0
        active={}
        while True:
            ok,img=cap.read()
            if not ok:
                break
            if frame % int(fps)!=0:
                frame+=1
                continue
            sec=int(frame/fps)
            seen=set()
            results=self.model.predict(img,verbose=False,conf=0.5)
            for r in results:
                for b in r.boxes:
                    cls=int(b.cls.item())
                    if cls in self.target_classes:
                        obj=self.target_classes[cls]
                        seen.add(obj)
                        active.setdefault(obj,sec)
            for obj in list(active):
                if obj not in seen:
                    events.append({'object':obj,'start':active[obj],'end':sec})
                    del active[obj]
            frame+=1
        cap.release()
        return events
