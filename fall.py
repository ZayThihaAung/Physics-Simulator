import math
import time
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import messagebox

# Window Set up
root = tk.Tk()
root.resizable(False, False)
root.title("Free Fall Simulator")
root.geometry("430x300")

tk.Label(root, text="Welcome to Free Fall Simulator!", font=("Helvetica", 16)).pack(pady=20)
tk.Label(root, text="This simulator calculates the time and velocity of a free-falling object.", font=("Helvetica", 10)).pack(pady=10)
tk.Label(root, text="Enter the height (m)", font=('Arial', 9)).pack(pady=5)

input = tk.Entry(root)
input.pack(pady=5, fill="x")

def Freefallsimulator():
  try: 
    height = float(input.get())
    gravity = 9.81 # Standard Value

    fall_time = math.sqrt((2*height)/gravity)
    velocity = gravity * fall_time

    interval = 0.1
    t = 0
    position = []
    Time = []
    # Putting data to the array to plot on the graph
    while t <= fall_time:
        y = height -0.5 * gravity * t**2  # Position at time t
        position.append(max(y,0))
        Time.append(t)
        time.sleep(0.1)
        t += interval
    
    # Packaging the plot lists
    figs, axis = plt.subplots()
    animated_plot, = axis.plot([], [], marker='o', linestyle='--', color='blue', label="Free Fall Path")
    
    # Decerate the graph
    axis.set_xlim(min(Time), max(Time))
    axis.set_ylim(min(position), max(position))
    axis.set_xlabel("Time (s)")
    axis.set_ylabel("Distance or Height (m)")
    axis.set_title("Free Falling Body")
    axis.legend()
    axis.grid()

    messagebox.showinfo("Simulation Complete", f"The object hit the ground in {fall_time:.2f} seconds with a velocity of {velocity:.2f} m/s. 💥")

    # Where the animation takes place
    def update(frames):
      animated_plot.set_data(Time[:frames], position[:frames])
      return animated_plot,

    # Activate the animation
    anim = animation.FuncAnimation(
       fig=figs,
       func=update,
       frames=50,
       interval=25,
    )
    plt.show()

  except ValueError:
    messagebox.showerror("Error", "Please enter the valid information.")

calculate_btn = tk.Button(root, text="Simulate!", font=("Helvetica", 12), command=Freefallsimulator, 
                          bg="#0B706A", fg="white", padx=10, pady=5)
calculate_btn.pack(pady=20)

root.mainloop()