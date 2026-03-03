import math
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import messagebox

# Window Set up
root = tk.Tk()
root.resizable(False, False)
root.title("2D Projectile Motion Simulator")
root.geometry("550x300")

tk.Label(root, text="Welcome to 2D Projectile Motion Simulator!", font=("Helvetica", 16)).pack(pady=20)
tk.Label(root, text="This simulator visualizes the trajectory of a projectile based on initial velocity and angle.", font=("Helvetica", 10)).pack(pady=10)
tk.Label(root, text="Enter the initial velocity (m/s)", font=('Arial', 9)).pack(pady=5)
input = tk.Entry(root)
input.pack(pady=5, fill="x")
tk.Label(root, text="Enter the launch angle (degrees)", font=('Arial', 9)).pack(pady=5)
angle_input = tk.Entry(root)
angle_input.pack(pady=5, fill="x")

def simulator() :
  try :
    v_not = float(input.get())
    angle_deg = float(angle_input.get())
    angle = math.radians(angle_deg)  # convert degrees -> radians explicitly
    g = 9.8
    # horizontal (X) and vertical (Y) components
    v_x = v_not * math.cos(angle)
    v_y = v_not * math.sin(angle)
    # clamp tiny horizontal velocity caused by floating-point rounding near 90°
    if angle_deg == 90:
      v_x = 0.0
    # Total flight time
    t = (2 * v_y) / g
    # Max Height (v_y^2 / (2g)) and Range (v^2 * sin(2a) / g)
    max_h = (v_y ** 2) / (2 * g)
    R = (v_not ** 2) * math.sin(2 * angle) / g
    messagebox.showinfo("Projectile Motion", f"Max Height {max_h:g}, Range {R:g}")
    
    postition_x = []
    postition_y = []
    interval = 0.05
    times = 0.0
    while times <= t:
      x = v_x * times
      y = v_y * times - 0.5 * g * times ** 2
      postition_x.append(x)
      postition_y.append(y)
      times += interval

    figs, axis = plt.subplots()
    animated_plot, = axis.plot([], [], marker = "o", linestyle="-", color = "green", label="Trajectory Path")

    # Auto-scale axes with a small margin so full trajectory is visible
    x_min = 0
    # prefer analytical range to avoid tiny numeric noise at near-vertical angles
    x_max = max(R, max(postition_x) if postition_x else 0.0)
    y_min = min(0, min(postition_y))
    y_max = max(postition_y) if postition_y else 1
    x_margin = (x_max - x_min) * 0.05
    y_margin = (y_max - y_min) * 0.05
    axis.set_xlim(x_min - x_margin, x_max + x_margin)
    axis.set_ylim(y_min - y_margin, y_max + y_margin)
    axis.set_xlabel("Horizontal Distance (m)")
    axis.set_ylabel("Vertical Distance (m)")
    axis.set_title("Projectile Motion Simulator")
    axis.legend()
    axis.grid()
    def update(i):
      animated_plot.set_data(postition_x[: i + 1], postition_y[: i + 1])
      return animated_plot,

    frames_count = len(postition_x)
    if v_not >= 110:
      base_ms = 110
    if v_not <= 100 or angle_deg <= 30:
      base_ms = 20

    interval_time = max(10, int(base_ms * (20/ max(v_not, 1))))
    anim = animation.FuncAnimation(
      fig=figs,
      func=update,
      frames=frames_count,
      interval=interval_time,
      blit=True
    )
    plt.show()
  
  except ValueError:
    messagebox.showerror("Input Error", "Please enter valid numeric values for velocity and angle.")

calculate_btn = tk.Button(root, text="Simulate!", font=("Helvetica", 12), command=simulator, 
                          bg="#0B706A", fg="white", padx=10, pady=5)
calculate_btn.pack(pady=20)
root.mainloop()