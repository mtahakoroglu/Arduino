import serial
import pygame
import math
from pygame.locals import *

# Initialize Pygame
pygame.init()
# Open serial port
ser = serial.Serial('COM8', 57600)  # Change 'COMX' to the appropriate port

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Plane Rotation")
font = pygame.font.Font(None, 36)

# Define a 3D point representing the center of the plane
center_x, center_y = width // 2, height // 2

# Define the size of the plane
plane_width, plane_height, plane_thickness = 200, 100, 20

# Define the vertices of the plane (rectangular prism)
plane_vertices = [
    (-plane_width // 2, -plane_height // 2, -plane_thickness // 2),
    (plane_width // 2, -plane_height // 2, -plane_thickness // 2),
    (plane_width // 2, plane_height // 2, -plane_thickness // 2),
    (-plane_width // 2, plane_height // 2, -plane_thickness // 2),
    (-plane_width // 2, -plane_height // 2, plane_thickness // 2),
    (plane_width // 2, -plane_height // 2, plane_thickness // 2),
    (plane_width // 2, plane_height // 2, plane_thickness // 2),
    (-plane_width // 2, plane_height // 2, plane_thickness // 2),
]

# Define the indices of the plane faces
plane_faces = [
    (0, 1, 2, 3),
    (4, 5, 6, 7),
    (0, 1, 5, 4),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (3, 0, 4, 7),
]

# Define the arrow for yaw direction
arrow_length = 40
arrow_width = 5

# Define initial Euler angles (in degrees)
roll, pitch, yaw = 0, 0, 0

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Read Euler angles from serial
    try:
        data = ser.readline().decode(errors='ignore').strip()
        print("Received data:", data)
        _, roll, _, pitch, _, yaw = data.split()
        roll, pitch, yaw = map(float, [roll, pitch, yaw])
        # print("Roll:", roll, "Pitch:", pitch, "Yaw:", yaw)
    except ValueError:
        continue

    # Clear the screen
    screen.fill(BLACK)

    # Convert Euler angles from degrees to radians
    roll_rad = math.radians(roll)
    pitch_rad = math.radians(pitch)
    yaw_rad = math.radians(yaw)

    # Calculate rotation matrices for roll, pitch, and yaw
    rotation_matrix_roll = [
        [1, 0, 0],
        [0, math.cos(roll_rad), -math.sin(roll_rad)],
        [0, math.sin(roll_rad), math.cos(roll_rad)]
    ]

    rotation_matrix_pitch = [
        [math.cos(pitch_rad), 0, math.sin(pitch_rad)],
        [0, 1, 0],
        [-math.sin(pitch_rad), 0, math.cos(pitch_rad)]
    ]

    rotation_matrix_yaw = [
        [math.cos(yaw_rad), -math.sin(yaw_rad), 0],
        [math.sin(yaw_rad), math.cos(yaw_rad), 0],
        [0, 0, 1]
    ]

    # Apply rotation matrices to the plane vertices
    rotated_vertices = []
    for vertex in plane_vertices:
        x = vertex[0]
        y = vertex[1]
        z = vertex[2]

        # Apply roll rotation
        x_roll = x * rotation_matrix_roll[0][0] + y * rotation_matrix_roll[0][1] + z * rotation_matrix_roll[0][2]
        y_roll = x * rotation_matrix_roll[1][0] + y * rotation_matrix_roll[1][1] + z * rotation_matrix_roll[1][2]
        z_roll = x * rotation_matrix_roll[2][0] + y * rotation_matrix_roll[2][1] + z * rotation_matrix_roll[2][2]

        # Apply pitch rotation
        x_pitch = x_roll * rotation_matrix_pitch[0][0] + y_roll * rotation_matrix_pitch[0][1] + z_roll * rotation_matrix_pitch[0][2]
        y_pitch = x_roll * rotation_matrix_pitch[1][0] + y_roll * rotation_matrix_pitch[1][1] + z_roll * rotation_matrix_pitch[1][2]
        z_pitch = x_roll * rotation_matrix_pitch[2][0] + y_roll * rotation_matrix_pitch[2][1] + z_roll * rotation_matrix_pitch[2][2]

        # Apply yaw rotation
        x_yaw = x_pitch * rotation_matrix_yaw[0][0] + y_pitch * rotation_matrix_yaw[0][1] + z_pitch * rotation_matrix_yaw[0][2]
        y_yaw = x_pitch * rotation_matrix_yaw[1][0] + y_pitch * rotation_matrix_yaw[1][1] + z_pitch * rotation_matrix_yaw[1][2]
        z_yaw = x_pitch * rotation_matrix_yaw[2][0] + y_pitch * rotation_matrix_yaw[2][1] + z_pitch * rotation_matrix_yaw[2][2]

        rotated_vertices.append((center_x + int(x_yaw), center_y - int(y_yaw)))

    # Draw the rotated plane faces
    for face in plane_faces:
        vertices = [rotated_vertices[i] for i in face]
        pygame.draw.polygon(screen, GREEN, vertices)
        # Draw edges of the plane
        for i in range(len(vertices)):
            start_point = vertices[i]
            end_point = vertices[(i + 1) % len(vertices)]
            pygame.draw.line(screen, WHITE, start_point, end_point, 2)

    # Draw arrow for yaw direction
    arrow_tip = (center_x + arrow_length * math.cos(yaw_rad), center_y - arrow_length * math.sin(yaw_rad))
    arrow_base = (center_x + int(rotated_vertices[7][0] - rotated_vertices[0][0]), center_y - int(rotated_vertices[7][1] - rotated_vertices[0][1]))
    pygame.draw.line(screen, RED, arrow_tip, arrow_base, arrow_width)

    # Update the display
    pygame.display.update()

# Close serial port and quit Pygame
ser.close()
pygame.quit()
