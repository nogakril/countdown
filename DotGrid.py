from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor

GREY = QColor(34,34,34)
RED = QColor(255, 0, 0)


class DotGrid(QWidget):
    def __init__(self):
        super().__init__()
        self.dots = {}
        self.dot_size = 14
        self.spacing = 17  # Space between centers of dots
        self.rows = 0
        self.cols = 0
        self.display_parameters = {
            'start_col': 5,
            'first_row': 1,
            'second_row': 30,
            'width': 8,
            'height': 16,
            'gap': 2,
            'space': 10,
            'letter_space': 2,
            'letter_gap': 1,
            'letter_width': 4,
        }
        self.letters = {
            'A': [(0, 1), (0, 2),
                  (1, 0), (1, 3),
                  (2, 0), (2, 1), (2, 2), (2, 3),
                  (3, 0), (3, 3),
                  (4, 0), (4, 3)],
            'B': [(0, 0), (0, 1), (0, 2),
                  (1, 0), (1, 3),
                  (2, 0), (2, 1), (2, 2),
                  (3, 0), (3, 3),
                  (4, 0), (4, 1), (4, 2)],
            'D': [(0, 0), (0, 1), (0, 2),
                  (1, 0), (1, 3),
                  (2, 0), (2, 3),
                  (3, 0), (3, 3),
                  (4, 0), (4, 1), (4, 2)],
            'Y': [(0, 0), (0, 4),
                  (1, 1), (1, 3),
                  (2, 2),
                  (3, 2),
                  (4, 2)],
            'S': [(0, 1), (0, 2),
                  (1, 0),
                  (2, 0), (2, 1), (2, 2),
                  (3, 3),
                  (4, 1), (4, 2)],
            'H': [(0, 0), (0, 3),
                  (1, 0), (1, 3),
                  (2, 0), (2, 1), (2, 2), (2, 3),
                  (3, 0), (3, 3),
                  (4, 0), (4, 3)],
            'O': [(0, 1), (0, 2),
                  (1, 0), (1, 3),
                  (2, 0), (2, 3),
                  (3, 0), (3, 3),
                  (4, 1), (4, 2)],
            'U': [(0, 0), (0, 3),
                  (1, 0), (1, 3),
                  (2, 0), (2, 3),
                  (3, 0), (3, 3),
                  (4, 1), (4, 2)],
            'R': [(0, 0), (0, 1), (0, 2),
                  (1, 0), (1, 3),
                  (2, 0), (2, 1), (2, 2),
                  (3, 0), (3, 3),
                  (4, 0), (4, 3)],
            'M': [(0, 0), (0, 4),
                  (1, 0), (1, 1), (1, 3), (1, 4),
                  (2, 0), (2, 2), (2, 4),
                  (3, 0), (3, 4),
                  (4, 0), (4, 4)],
            'I': [(0, 1), (0, 2),
                  (1, 2),
                  (2, 2),
                  (3, 2),
                  (4, 1), (4, 2)],
            'N': [(0, 0), (0, 3),
                  (1, 0), (1, 1), (1, 3),
                  (2, 0), (2, 2), (2, 3),
                  (3, 0), (3, 3),
                  (4, 0), (4, 3)],
            'T': [(0, 0), (0, 1), (0, 2), (0, 3),
                  (1, 2),
                  (2, 2),
                  (3, 2),
                  (4, 2)],
            'E': [(0, 0), (0, 1), (0, 2),
                  (1, 0),
                  (2, 0), (2, 1), (2, 2),
                  (3, 0),
                  (4, 0), (4, 1), (4, 2)],
            'C': [(0, 1), (0, 2),
                  (1, 0),
                  (2, 0),
                  (3, 0),
                  (4, 1), (4, 2)]
        }

        # Digit positions mapping
        self.digit_positions = [
            # Days
            {'row': 'first_row', 'col_offset': 0, 'digit': 8},
            {'row': 'first_row', 'col_offset': 1, 'digit': 8},
            # Months
            {'row': 'first_row', 'col_offset': 2, 'digit': 8},
            {'row': 'first_row', 'col_offset': 3, 'digit': 8},
            # Years
            {'row': 'first_row', 'col_offset': 4, 'digit': 8},
            {'row': 'first_row', 'col_offset': 5, 'digit': 8},
            # Hours
            {'row': 'second_row', 'col_offset': 0, 'digit': 8},
            {'row': 'second_row', 'col_offset': 1, 'digit': 8},
            # Minutes
            {'row': 'second_row', 'col_offset': 2, 'digit': 8},
            {'row': 'second_row', 'col_offset': 3, 'digit': 8},
            # Seconds
            {'row': 'second_row', 'col_offset': 4, 'digit': 8},
            {'row': 'second_row', 'col_offset': 5, 'digit': 8}
        ]

    def draw_letter(self, letter, base_row=None, base_col=None):
        if letter not in self.letters:
            return

        for row_offset, col_offset in self.letters[letter]:
            self.change_dot_color(base_row + row_offset, base_col + col_offset)

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

    def display_digit(self, base_row, base_col, height, width, digit):
        # Define segment mappings
        segments = {
            'top': [0, 2, 3, 5, 6, 7, 8, 9],
            'middle': [2, 3, 4, 5, 6, 8, 9],
            'bottom': [0, 2, 3, 5, 6, 8, 9],
            'left_top': [0, 4, 5, 6, 8, 9],
            'right_top': [0, 1, 2, 3, 4, 7, 8, 9],
            'left_bottom': [0, 2, 6, 8],
            'right_bottom': [0, 1, 3, 4, 5, 6, 7, 8, 9]
        }

        # Draw horizontal segments
        if digit in segments['top']:
            for r in range(width + 1):
                self.change_dot_color(base_row, base_col + r)
        if digit in segments['middle']:
            for r in range(width + 1):
                self.change_dot_color(base_row + height // 2, base_col + r)
        if digit in segments['bottom']:
            for r in range(width + 1):
                self.change_dot_color(base_row + height, base_col + r)

        # Draw vertical segments
        for r in range(height + 1):
            if digit in segments['left_top'] and r < height // 2:
                self.change_dot_color(base_row + r, base_col)
            if digit in segments['right_top'] and r < height // 2:
                self.change_dot_color(base_row + r, base_col + width)
            if digit in segments['left_bottom'] and r >= height // 2:
                self.change_dot_color(base_row + r, base_col)
            if digit in segments['right_bottom'] and r >= height // 2:
                self.change_dot_color(base_row + r, base_col + width)

        self.update()

    def mousePressEvent(self, event):
        col = (event.x() - (self.width() - ((self.cols - 1) * self.spacing)) // 2) // self.spacing
        row = (event.y() - (self.height() - ((self.rows - 1) * self.spacing)) // 2) // self.spacing
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.change_dot_color(row, col)
            self.update()

    def draw_digits(self):
        params = self.display_parameters
        start_col = params['start_col']
        width = params['width']
        height = params['height']
        gap = params['gap']
        space = params['space']

        for pos in self.digit_positions:
            row = params[pos['row']]
            col_offset = pos['col_offset']
            # Calculate column position based on offset and gaps/spaces
            base_col = start_col + col_offset * (width + gap) + (col_offset // 2) * space
            self.display_digit(row, base_col, height, width, pos['digit'])

    def draw_letters(self):
        params = self.display_parameters
        start_col = params['start_col']
        width = params['width']
        gap = params['gap']
        space = params['space']

        # Base columns for each label aligned with the digits
        base_columns = {
            "YRS": start_col,
            "MOS": start_col + (2 * width) + (2 * gap) + space,
            "DAYS": start_col + (4 * width) + (4 * gap) + (2 * space),
            "HRS": start_col,
            "MINS": start_col + (2 * width) +(2 * gap) + space,
            "SECS": start_col + (4 * width) + (4 * gap) + (2 * space)
        }

        # First Row Labels
        start_row_1 = params['first_row'] + params['height'] + params['letter_space'] + 1
        for label, base_col in base_columns.items():
            if label in ["YRS", "MOS", "DAYS"]:
                self.draw_word(label, start_row_1, base_col)

        # Second Row Labels
        start_row_2 = params['second_row'] + params['height'] + params['letter_space'] + 1
        for label, base_col in base_columns.items():
            if label in ["HRS", "MINS", "SECS"]:
                self.draw_word(label, start_row_2, base_col)

    def draw_word(self, word, base_row, base_col):
        params = self.display_parameters
        letter_gap = params['letter_gap']
        letter_width = params['letter_width']

        for index, letter in enumerate(word):
            letter_col = base_col + index * (letter_width + letter_gap)
            self.draw_letter(letter, base_row, letter_col)

    def update_digits(self, years, months, days, hours, minutes, seconds):
        params = self.display_parameters
        start_col = params['start_col']
        width = params['width']
        height = params['height']
        gap = params['gap']
        space = params['space']

        self.clear_digits()

        # Clear and update years digits
        self.display_digit(params['first_row'], start_col, height, width, years // 10)
        self.display_digit(params['first_row'], start_col + width + gap, height, width, years % 10)

        # Clear and update months digits
        base_col = start_col + (2 * width) + gap + space
        self.display_digit(params['first_row'], base_col, height, width, months // 10)
        self.display_digit(params['first_row'], base_col + width + gap, height, width, months % 10)

        # Clear and update days digits
        base_col = start_col + (4 * width) + (2 * gap) + (2 * space)
        self.display_digit(params['first_row'], base_col, height, width, days // 10)
        self.display_digit(params['first_row'], base_col + width + gap, height, width, days % 10)

        # Clear and update hours digits
        self.display_digit(params['second_row'], start_col, height, width, hours // 10)
        self.display_digit(params['second_row'], start_col + width + gap, height, width, hours % 10)

        # Clear and update minutes digits
        base_col = start_col + (2 * width) + gap + space
        self.display_digit(params['second_row'], base_col, height, width, minutes // 10)
        self.display_digit(params['second_row'], base_col + width + gap, height, width, minutes % 10)

        # Clear and update seconds digits
        base_col = start_col + (4 * width) + (2 * gap) + (2 * space)
        self.display_digit(params['second_row'], base_col, height, width, seconds // 10)
        self.display_digit(params['second_row'], base_col + width + gap, height, width, seconds % 10)

        self.draw_letters()
        self.update()

    def clear_digits(self):
        self.dots = {}

    def change_dot_color(self, row, col, color=RED):
        self.dots[(row, col)] = color
