import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class Speedometer(QWidget):
    
            
        def __init__(self, speed):
            super().__init__()

            self.speed = speed
            self.initUI()

        def initUI(self):
            self.setWindowTitle('Speedometer')
           
            
            layout = QVBoxLayout()
            self.setLayout(layout)

            # Create figure and canvas
            self.fig, self.ax = plt.subplots(figsize=(5, 5))  # Adjust the figure size
            canvas = FigureCanvas(self.fig)
            layout.addWidget(canvas)

            # Draw speedometer
            self.draw_speedometer()

            canvas.draw()

        def draw_speedometer(self):
            ax = self.ax
            fig = self.fig

            # Create the angle array to cover a full circle
            angles = np.linspace(230, -50, 25)  # 12 points from 230 to -45 degrees for full circle

            # Radius of the gauge
            radius = 6

            # Create the gauge background
            for angle in angles:
                x = [0, radius * np.cos(np.radians(angle))]
                y = [0, radius * np.sin(np.radians(angle))]
                ax.plot(x, y, color='#444444', lw=2)

            # Add the speed ticks and labels up to 220 km/h
            for i, angle in enumerate(angles):
                x = radius * np.cos(np.radians(angle))
                y = radius * np.sin(np.radians(angle))
                speed = i * 10  # Calculate speed for the label
                ax.text(x, y, f'{speed}', ha='center', va='center', fontsize=12, color='green')

            # Plot the speed pointer
            max_speed = 240  # Maximum speed on the speedometer gauge
            pointer_angle = np.radians(230 - self.speed * int((280 / max_speed)))  # Adjust scaling for the maximum speed
            x_pointer = [0, radius * np.cos(pointer_angle)]
            y_pointer = [0, radius * np.sin(pointer_angle)]
            ax.plot(x_pointer, y_pointer, color='red', linewidth=5)

            # Add speed text (slightly lower)
            ax.text(0, -5, f'{self.speed} km/h', ha='center', va='bottom', fontsize=30, color='white')

            # Remove the axes
            ax.axis('off')

            # Set the background color
            fig.patch.set_facecolor('#202020')
            ax.set_facecolor('#202020')

            # Set aspect ratio to be equal
            ax.set_aspect('equal')

def main():
    app = QApplication(sys.argv)
    speed = 150 # Set the desired speed value here (up to 220 km/h)
    ex = Speedometer(speed)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
