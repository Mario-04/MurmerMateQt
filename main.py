import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog


# Step 1: Create the main application class
class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Step 2: Set up the window properties
        self.setWindowTitle('My First PyQt5 App')
        self.setGeometry(100, 100, 280, 80)

        # Step 3: Create a label and a button
        self.label = QLabel('Hello, PyQt5!', self)
        self.button = QPushButton('Click Me', self)

        # Step 4: Set up a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Step 5: Set the layout for the main widget
        self.setLayout(layout)

        # Step 6: Connect the button's click event to a method
        self.button.clicked.connect(self.on_button_clicked)

    # Step 7: Define what happens when the button is clicked
    def on_button_clicked(self):
        self.label.setText('Button Clicked!')
        self.openFileNameDialog()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)


# Step 8: Set up the application loop
def main():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


# Run the application
if __name__ == '__main__':
    main()
