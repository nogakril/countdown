from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor

GREY = QColor(100, 100, 100)
RED = QColor(255, 0, 0)


class DotGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.dots = {}
        self.dot_size = 8
        self.spacing = 16  # Space between centers of dots
        self.rows = 0
        self.cols = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # For smoother circles
        painter.setBrush(GREY)  # Default grey color
        self.rows = (self.height() - self.dot_size) // self.spacing + 1
        self.cols = (self.width() - self.dot_size) // self.spacing + 1
        start_x = (self.width() - (self.cols - 1) * self.spacing) // 2
        start_y = (self.height() - (self.rows - 1) * self.spacing) // 2
        for row in range(self.rows):
            for col in range(self.cols):
                x = start_x + col * self.spacing
                y = start_y + row * self.spacing
                color = self.dots.get((row, col), GREY)
                painter.setBrush(color)
                painter.drawEllipse(x, y, self.dot_size, self.dot_size)

    def display_digit(self, base_row, base_col, digit):
        # Define the segments for each digit (0-9)
        segments = {
            '0': [(0, 1), (1, 0), (1, 2), (2, 0), (2, 2), (3, 1)],
            '1': [(1, 2), (2, 2)],
            '2': [(0, 1), (1, 2), (2, 1), (2, 0), (3, 1)],
            '3': [(0, 1), (1, 2), (2, 1), (2, 2), (3, 1)],
            '4': [(1, 0), (2, 1), (1, 2), (2, 2)],
            '5': [(0, 1), (1, 0), (2, 1), (2, 2), (3, 1)],
            '6': [(0, 1), (1, 0), (2, 0), (2, 1), (2, 2), (3, 1)],
            '7': [(0, 1), (1, 2), (2, 2)],
            '8': [(0, 1), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (3, 1)],
            '9': [(0, 1), (1, 0), (1, 2), (2, 1), (2, 2), (3, 1)]
        }

        # Clear previous digits in this space
        for r in range(4):
            for c in range(3):
                self.change_dot_color(base_row + r, base_col + c, GREY)

        # Set the new digit
        if str(digit) in segments:
            for (r, c) in segments[str(digit)]:
                self.change_dot_color(base_row + r, base_col + c, RED)
        self.update()

    def paint_number_eight(self, width):
        # Calculate the base row and column to paint the number 8
        base_row = (self.rows - 4) // 2
        base_col = (self.cols - 3 - width) // 2
        self.display_digit(base_row, base_col, 8)

    def mousePressEvent(self, event):
        col = (event.x() - (self.width() - ((self.cols - 1) * self.spacing)) // 2) // self.spacing
        row = (event.y() - (self.height() - ((self.rows - 1) * self.spacing)) // 2) // self.spacing
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.change_dot_color(row, col)
            self.update()

    def change_dot_color(self, row, col):
        current_color = self.dots.get((row, col), GREY)
        if current_color == RED:
            self.dots[(row, col)] = GREY
        else:
            self.dots[(row, col)] = RED
