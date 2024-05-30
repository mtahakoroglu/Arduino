import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import time

# Serial port configuration
ser = serial.Serial('COM8', 57600, timeout=1)  # Adjust the COM port and baud rate as necessary

# Deques to hold the last 20 seconds of data
time_len = 20  # seconds
data_len = 50 * time_len  # Assuming 200 Hz sampling rate
times = deque(maxlen=data_len)

accX = deque(maxlen=data_len)
accY = deque(maxlen=data_len)
accZ = deque(maxlen=data_len)

gyroX = deque(maxlen=data_len)
gyroY = deque(maxlen=data_len)
gyroZ = deque(maxlen=data_len)

angleX = deque(maxlen=data_len)
angleY = deque(maxlen=data_len)
angleZ = deque(maxlen=data_len)

# Initialize figure and subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Function to update the data
def update_data(frame):
    line = ser.readline().decode(errors='ignore').strip()
    if line:
        print("Received data:", line)
        try:
            data = line.split('\t')
            if len(data) >= 11:  # Ensure there is enough data in the line
                temp = float(data[0].split(': ')[1])
                time_stamp = float(data[1].split(': ')[1])

                times.append(time_stamp)

                accX.append(float(data[2].split(': ')[1]))
                accY.append(float(data[3].split(': ')[1]))
                accZ.append(float(data[4].split(': ')[1]))

                gyroX.append(float(data[5].split(': ')[1]))
                gyroY.append(float(data[6].split(': ')[1]))
                gyroZ.append(float(data[7].split(': ')[1]))

                angleX.append(float(data[8].split(': ')[1]))
                angleY.append(float(data[9].split(': ')[1]))
                angleZ.append(float(data[10].split(': ')[1]))

                # Update plots
                ax1.cla()
                ax1.plot(times, accX, label='accX (g)')
                ax1.plot(times, accY, label='accY (g)')
                ax1.plot(times, accZ, label='accZ (g)')
                ax1.legend(loc='upper left')
                ax1.set_title('Acceleration Data')
                
                ax2.cla()
                ax2.plot(times, gyroX, label='gyroX (°/s)')
                ax2.plot(times, gyroY, label='gyroY (°/s)')
                ax2.plot(times, gyroZ, label='gyroZ (°/s)')
                ax2.legend(loc='upper left')
                ax2.set_title('Gyroscope Data')
                
                ax3.cla()
                ax3.plot(times, angleX, label='angleX (°)')
                ax3.plot(times, angleY, label='angleY (°)')
                ax3.plot(times, angleZ, label='angleZ (°)')
                ax3.legend(loc='upper left')
                ax3.set_title('Euler Angles')
            else:
                print("Incomplete data received.")
        except ValueError as e:
            print("Error parsing data:", e)

# Function to handle key press
def on_key(event):
    if event.key == 'escape':
        plt.close()  # This will close the plot window
        ser.close()  # This will close the serial port
        print("Data acquisition terminated.")

fig.canvas.mpl_connect('key_press_event', on_key)

ani = animation.FuncAnimation(fig, update_data, interval=50)
plt.show()
