import matplotlib.pyplot as plt
import numpy as np

# Sensor layout
layout_type = "circular"                                     # "circular", "spiral", "random","rectangle"
num_sensors = 6
radius = 50  # Radius of the circular layout
width = 40   # Width of the square layout
height = 60  # Height of the rectangle layout
num_phases = 5000  # Number of random phases to simulate coverage area

# Equal phasing for all sensors
phases = np.zeros(num_sensors)

# Generate sensor positions based on layout type
if layout_type == "circular":
    angles = np.linspace(0, 2*np.pi, num_sensors, endpoint=False)
    x = radius * np.cos(angles)
    y = radius * np.sin(angles)
elif layout_type == "spiral":
    theta = np.linspace(0, 5*np.pi, num_sensors) + np.random.normal(0, 0.1, num_sensors)
    radius = np.linspace(0, radius, num_sensors)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
elif layout_type == "random":
    np.random.seed(42)  # For reproducibility
    x = np.random.uniform(-radius, radius, num_sensors)
    y = np.random.uniform(-radius, radius, num_sensors)
elif layout_type == "rectangle":
    side_x = int(np.sqrt(num_sensors * (width / height)))
    side_y = int(num_sensors / side_x)
    x = np.linspace(-width/2, width/2, side_x)
    y = np.linspace(-height/2, height/2, side_y)
    x, y = np.meshgrid(x, y)
    x = x.flatten()
    y = y.flatten()
else:
    raise ValueError("Invalid layout type.")

# Plot sensor positions
plt.figure()
plt.plot(x, y, '*')
plt.grid()
plt.title('Sensor Layout: ' + layout_type.capitalize())
plt.xlabel('x')
plt.ylabel('y')

# Verify vertical looking angle
vertical_angles = np.arctan2(y, x) * 180 / np.pi
average_vertical_angle = np.mean(vertical_angles)
print("Average Vertical Looking Angle:", average_vertical_angle)

# Simulate coverage area by testing random phases
positions = np.zeros((num_phases, 2))

for i in range(num_phases):
    random_phases = np.random.uniform(0, 2*np.pi, num_sensors)
    dx = x[1:] - x[0]
    dy = y[1:] - y[0]
    R = np.array([dx, dy]).T
    B = np.matmul(R.T, R)
    b = np.matmul(R.T, random_phases[1:] - random_phases[0])
    try:
        r = np.linalg.solve(B.T.dot(B), B.T.dot(b))
    except np.linalg.LinAlgError:
        print("Error: Singular matrix. Skipping iteration.")
        continue
    positions[i, :] = r.T

# Plot coverage area
plt.figure()
plt.plot(positions[:, 0], positions[:, 1], '.')
plt.grid(True)
plt.xlabel('dcosx sin(theta)cos(phi)')
plt.ylabel('dcosy sin(theta)sin(phi)')
plt.title('Coverage Area: ' + layout_type.capitalize())

plt.show()