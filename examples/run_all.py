"""
Run all demos sequentially. Useful for local exploration.
"""
from physics_simulator.simulations.free_fall import simulate_free_fall
from physics_simulator.simulations.projectile import simulate_projectile
from physics_simulator.simulations.pendulum import simulate_pendulum
from physics_simulator.visualization import plot_motion, animate_2d, pendulum_xy

def demo_free_fall():
    t, y, v = simulate_free_fall(h0=20.0, dt=0.02)
    plot_motion(t, y, ylabel="Height (m)", title="Free Fall Demo")

def demo_projectile():
    t, x, y, vx, vy = simulate_projectile(speed=25.0, angle_deg=30.0, dt=0.02)
    animate_2d(t, x, y, title="Projectile Demo")

def demo_pendulum():
    t, theta, omega = simulate_pendulum(theta0=0.5, length=1.0, dt=0.02, t_max=8.0)
    x, y = pendulum_xy(theta, 1.0)
    animate_2d(t, x, y, title="Pendulum Demo")

if __name__ == "__main__":
    demo_free_fall()
    demo_projectile()
    demo_pendulum()
