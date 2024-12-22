import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from moviepy.editor import *
from gtts import gTTS
from PIL import Image, ImageFont, ImageDraw

class VideoCreatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.audio_path = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Créateur Vidéo Avancé')
        self.setGeometry(200, 200, 800, 600)

        # Appliquer des styles
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial;
            }

            QLineEdit {
                border: 2px solid #cccccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #45a049;
            }

            QLabel {
                font-size: 16px;
                color: #333333;
            }
        """)

        # Layout principal
        layout = QtWidgets.QVBoxLayout()

        # Champs de texte
        self.text_input = QtWidgets.QLineEdit()
        self.text_input.setPlaceholderText("Entrez le texte pour la vidéo...")

        # Sélection d'images ou vidéos
        self.media_dir_input = QtWidgets.QLineEdit()
        self.media_dir_button = QtWidgets.QPushButton("Parcourir Répertoire")
        self.media_dir_button.clicked.connect(self.browse_media_directory)

        # Sélection d'audio
        self.audio_input = QtWidgets.QLineEdit()
        self.audio_button = QtWidgets.QPushButton("Parcourir Audio")
        self.audio_button.clicked.connect(self.browse_audio_file)

        # Couleur d'arrière-plan
        self.bg_color_input = QtWidgets.QLineEdit()
        self.bg_color_input.setPlaceholderText("#FFFFFF")

        # Bouton pour créer la vidéo
        self.create_button = QtWidgets.QPushButton("Créer la Vidéo")
        self.create_button.clicked.connect(self.handle_create_video)

        # Ajouter des widgets au layout
        layout.addWidget(QtWidgets.QLabel("Bienvenue dans le Créateur de Vidéo Avancé"))
        layout.addWidget(QtWidgets.QLabel("Texte :"))
        layout.addWidget(self.text_input)

        media_layout = QtWidgets.QHBoxLayout()
        media_layout.addWidget(self.media_dir_input)
        media_layout.addWidget(self.media_dir_button)
        layout.addLayout(media_layout)

        audio_layout = QtWidgets.QHBoxLayout()
        audio_layout.addWidget(self.audio_input)
        audio_layout.addWidget(self.audio_button)
        layout.addLayout(audio_layout)

        bg_color_layout = QtWidgets.QHBoxLayout()
        bg_color_layout.addWidget(QtWidgets.QLabel("Couleur d'arrière-plan :"))
        bg_color_layout.addWidget(self.bg_color_input)
        layout.addLayout(bg_color_layout)

        layout.addWidget(self.create_button)
        self.setLayout(layout)
        self.show()

    def browse_media_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Sélectionner un répertoire")
        if directory:
            self.media_dir_input.setText(directory)

    def browse_audio_file(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Sélectionner un fichier audio", "", "Audio Files (*.mp3 *.wav)"
        )
        if file_path:
            self.audio_path = file_path
            self.audio_input.setText(file_path)

    def create_typing_effect(self, text, duration_per_letter, bg_color):
        clips = []
        width, height = 1280, 720

        def wrap_text(draw, text, font, max_width):
            lines = []
            words = text.split()
            current_line = ""
            for word in words:
                test_line = current_line + word + " "
                if draw.textlength(test_line, font=font) > max_width:
                    lines.append(current_line)
                    current_line = word + " "
                else:
                    current_line = test_line
            lines.append(current_line.strip())
            return lines

        font_size = 50
        font = ImageFont.truetype("arial.ttf", font_size)

        for i in range(1, len(text) + 1):
            sub_text = text[:i]
            img = Image.new("RGB", (width, height), bg_color)
            draw = ImageDraw.Draw(img)

            lines = wrap_text(draw, sub_text, font, width - 100)
            while len(lines) * (font_size + 10) > height - 100 and font_size > 10:
                font_size -= 2
                font = ImageFont.truetype("arial.ttf", font_size)
                lines = wrap_text(draw, sub_text, font, width - 100)

            y_offset = (height - len(lines) * (font_size + 10)) // 2
            for line in lines:
                x_offset = (width - draw.textlength(line, font=font)) // 2
                draw.text((x_offset, y_offset), line, fill=(0, 0, 0), font=font)
                y_offset += font_size + 10

            img_path = f"temp_{i}.png"
            img.save(img_path)
            clip = ImageClip(img_path).set_duration(duration_per_letter)

            clips.append(clip)
            os.remove(img_path)

        return concatenate_videoclips(clips, method="compose")

    def create_video(self, text, audio_file, bg_color, media_dir):
        try:
            # Effet de texte
            typing_effect = self.create_typing_effect(text, 0.1, bg_color)

            # Ajouter des séquences d'images ou vidéos
            media_clips = []
            if os.path.isdir(media_dir):
                for file in os.listdir(media_dir):
                    file_path = os.path.join(media_dir, file)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        media_clips.append(ImageClip(file_path).set_duration(2))
                    elif file.lower().endswith(('.mp4', '.avi', '.mov')):
                        media_clips.append(VideoFileClip(file_path).subclip(0, 5))

            # Combiner les clips
            full_video = concatenate_videoclips([typing_effect] + media_clips, method="compose")

            # Ajouter l'audio
            if audio_file and os.path.exists(audio_file):
                audio_clip = AudioFileClip(audio_file).subclip(0, full_video.duration)
                full_video = full_video.set_audio(audio_clip)

            # Exporter la vidéo
            full_video.write_videofile("output_video.mp4", fps=24)
            QtWidgets.QMessageBox.information(self, "Succès", "Vidéo créée avec succès !")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Erreur", f"Erreur lors de la création : {e}")

    def handle_create_video(self):
        text = self.text_input.text()
        bg_color = self.bg_color_input.text()
        media_dir = self.media_dir_input.text()
        audio_file = self.audio_path

        if not text:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Veuillez entrer un texte.")
            return

        if not bg_color.startswith("#") or len(bg_color) != 7:
            QtWidgets.QMessageBox.warning(self, "Erreur", "Couleur d'arrière-plan invalide, utilisez #FFFFFF")
            return

        if not os.path.isdir(media_dir):
            QtWidgets.QMessageBox.warning(self, "Erreur", "Répertoire des médias invalide.")
            return

        self.create_video(text, audio_file, bg_color, media_dir)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = VideoCreatorApp()
    sys.exit(app.exec_())
