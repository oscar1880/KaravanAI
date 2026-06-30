import csv

class Report:
    def save(self, events, path):
        with open(path,"w",newline="",encoding="utf-8") as f:
            w=csv.writer(f)
            w.writerow(["video","time","object","confidence"])
            for e in events:
                w.writerow(e)
