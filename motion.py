import math
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import messagebox
# This simulation is done with matplotlid which offers only graphs
# a pendulum completes every swings in excalty the same time
# Frequecy (f) = 1 / period which is number oscillation (swing) in 1 second
# Period depends on the length of pendulum
# Oscillation = 10, time_taken = 2
# so, T = 10/2 = 5 s

# Window Set up
root = tk.Tk()
root.resizable(False, False)
root.title("Simple Pendulum Motion Simulator")
root.geometry("540x300")
tk.Label(root, text="Welcome to Simple Pendulum Motion Simulator!", font=("Helvetica", 14)).pack(pady=20)
tk.Label(root, text="This simulator calculates the period and angular displacement of a simple pendulum.", font=("Helvetica", 10)).pack(pady=10)

tk.Label(root, text="Enter the lenght of pendulum (m)", font=('Arial', 9)).pack(pady=5)
input_1 = tk.Entry(root)
input_1.pack(pady=5, fill="x")
tk.Label(root, text="Enter the initial angle (degree)", font=('Arial', 9)).pack(pady=5)
input_2 = tk.Entry(root)
input_2.pack(pady=5, fill="x")

def task() :  
  position = []
  times = []
  try:
    length = float(input_1.get())
    theda_0 = float(input_2.get())
    theda_0 = math.radians(theda_0)
    pi_value = math.pi
    gravity = 9.81

    # Period of a Pendulum (Time for one full swing)
    time_taken = 2 * pi_value * math.sqrt(length/gravity)

    interval = 0.1
    t = 0 

    while t <= time_taken:
      times.append(max(t, 0))
      # Angular Displacement (Position at any time)
      displacement = math.cos(math.sqrt(gravity / length) * t)
      position.append(displacement)
      time.sleep(0.1)
      t += interval

    messagebox.showinfo("Simulation Complete", f"The pendulum completed one full swing in {time_taken:.2f} seconds.")
    
    figs, axis = plt.subplots()
    animated_plot, = axis.plot([], [], marker="o", color='b')

    # Decerate the graph
    axis.set_xlim(min(times), max(times))
    axis.set_ylim(min(position), max(position))
    axis.set_xlabel("Time (s)")
    axis.set_ylabel("Anuglar Displacement (radians)")
    axis.set_title("Simple Pendulum Motion")
    axis.grid()

    def update(frames):
      animated_plot.set_data(times[:frames], position[:frames])
      return animated_plot,

    anim = animation.FuncAnimation(
       fig=figs,
       func=update,
       frames=60,
       interval=24,
    )
    plt.show()
    
  except ValueError:
    messagebox.showerror("Error", "Please enter the valid information.")

calculate_btn = tk.Button(root, text="Simulate!", font=("Helvetica", 12), command=task, 
                          bg="#0B706A", fg="white", padx=10, pady=5)
calculate_btn.pack(pady=20)
root.mainloop()