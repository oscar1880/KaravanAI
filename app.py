import sys
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QTextEdit,
    QProgressBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("KaravanAI")
        self.resize(700, 500)

        self.video_folder = None

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.folder_label = QLabel("Henüz video klasörü seçilmedi.")
        layout.addWidget(self.folder_label)

        self.select_button = QPushButton("📂 Video Klasörü Seç")
        self.select_button.clicked.connect(self.select_folder)
        layout.addWidget(self.select_button)

        self.start_button = QPushButton("▶ Analizi Başlat")
        self.start_button.clicked.connect(self.start_analysis)
        self.start_button.setEnabled(False)
        layout.addWidget(self.start_button)

        self.progress = QProgressBar()
        self.progress.setValue(0)
        layout.addWidget(self.progress)

        self.log = QTextEdit()
        self.log.setReadOnly(True)
        layout.addWidget(self.log)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Video klasörünü seç"
        )

        if folder:
            self.video_folder = Path(folder)
            self.folder_label.setText(str(self.video_folder))
            self.start_button.setEnabled(True)
            self.log.append("Video klasörü seçildi.")

    def start_analysis(self):
        self.progress.setValue(0)
        self.log.append("")
        self.log.append("Analiz başlıyor...")

        videos = list(self.video_folder.glob("*.mp4"))

        if not videos:
            self.log.append("MP4 dosyası bulunamadı.")
            return

        total = len(videos)

        for i, video in enumerate(videos, start=1):
            self.log.append(f"Taranacak: {video.name}")

            percent = int((i / total) * 100)
            self.progress.setValue(percent)
            QApplication.processEvents()

        self.log.append("")
        self.log.append("Hazır. Bir sonraki aşamada gerçek YOLO analizi eklenecek.")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())