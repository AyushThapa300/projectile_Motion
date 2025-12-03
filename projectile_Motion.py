import math
import numpy as np
import matplotlib.pyplot as plt

def projectile_with_air_resistance():
    print("\n--- Projectile Motion with Air Resistance ---")

    # User Inputs
    v0 = float(input("Enter initial velocity (m/s): "))
    angle_deg = float(input("Enter launch angle (degrees): "))
    mass = float(input("Enter mass of the projectile (kg): "))
    area = float(input("Enter cross-sectional area (m²): "))
    Cd = float(input("Enter drag coefficient [0.47 for sphere]: "))
    rho = float(input("Enter air density (kg/m³) [1.225 for sea level]: "))
    dt = float(input("Enter time step (s) [e.g., 0.01]: "))
    g = 9.81  # gravity

    angle_rad = math.radians(angle_deg)

    # Initial velocity components
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)

    # Initial position
    x = 0
    y = 0

    # Lists to store trajectory
    X = [x]
    Y = [y]

    # Euler integration loop
    while y >= 0:
        v = math.sqrt(vx**2 + vy**2)
        Fd = 0.5 * Cd * rho * area * v**2

        # Air resistance components
        Fdx = Fd * (vx / v)
        Fdy = Fd * (vy / v)

        # Acceleration components
        ax = -Fdx / mass
        ay = -g - (Fdy / mass)

        # Update velocity
        vx += ax * dt
        vy += ay * dt

        # Update position
        x += vx * dt
        y += vy * dt

        X.append(x)
        Y.append(y)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(X, Y, label="With Air Resistance", color='blue')

    # Optional: Plot ideal trajectory (no air resistance)
    t_total = (2 * v0 * math.sin(angle_rad)) / g
    t = np.linspace(0, t_total, num=300)
    x_ideal = v0 * np.cos(angle_rad) * t
    y_ideal = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2
    plt.plot(x_ideal, y_ideal, '--', color='red', label="Ideal (No Air Resistance)")

    plt.title("Projectile Motion with and without Air Resistance")
    plt.xlabel("Horizontal Distance (m)")
    plt.ylabel("Vertical Height (m)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main call
if __name__ == "__main__":
    projectile_with_air_resistance()
