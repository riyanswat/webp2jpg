import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QMessageBox, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap
from PIL import Image

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'WebP to JPG Converter'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 120
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create input frame
        input_frame = QWidget(self)

        input_label = QLabel('Select WebP file:', input_frame)

        self.input_entry = QLabel('', input_frame)

        browse_button = QPushButton('Browse', input_frame)
        browse_button.clicked.connect(self.browse_file)

        # Create convert button
        convert_button = QPushButton('Convert', self)
        convert_button.clicked.connect(self.convert_file)

        # Create layouts
        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_entry)
        input_layout.addWidget(browse_button)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(convert_button)

        input_frame.setLayout(input_layout)
        self.setLayout(main_layout)

        self.show()

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "WebP files (*.webp)")
        if file_path:
            self.input_entry.setText(file_path)

    def convert_file(self):
        input_path = self.input_entry.text()
        if not input_path:
            QMessageBox.critical(self, 'Error', 'Please select a webp file.')
            return
        output_path = input_path[:-5] + ".jpg"
        try:
            image = Image.open(input_path)
            image.save(output_path)
            QMessageBox.information(self, 'Success', 'File converted successfully!')
        except:
            QMessageBox.critical(self, 'Error', 'Failed to convert file.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
