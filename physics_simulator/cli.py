"""Small CLI for running simple demos."""
import click
import matplotlib
# CLI shouldn't fail on headless CI if user runs examples in CI; leave backend to user,
# but tests set Agg where appropriate.
from .simulations.free_fall import simulate_free_fall
from .simulations.projectile import simulate_projectile
from .simulations.pendulum import simulate_pendulum
from .visualization import plot_motion, animate_2d, pendulum_xy

@click.group()
def cli():
    """Physics Simulator CLI: run small demos and visualizations."""
    pass

@cli.command("free-fall")
@click.option("--height", type=float, default=10.0, help="Initial height (m)")
@click.option("--v0", type=float, default=0.0, help="Initial vertical velocity (m/s)")
@click.option("--dt", type=float, default=0.01, help="Time step (s)")
@click.option("--air", type=float, default=0.0, help="Linear air resistance coefficient")
def run_free_fall(height, v0, dt, air):
    t, y, v = simulate_free_fall(h0=height, v0=v0, dt=dt, air_resistance=air)
    plot_motion(t, y, ylabel="Height (m)", title="Free Fall")

@cli.command("projectile")
@click.option("--speed", type=float, default=20.0, help="Launch speed (m/s)")
@click.option("--angle", type=float, default=45.0, help="Launch angle (deg)")
@click.option("--dt", type=float, default=0.01, help="Time step (s)")
@click.option("--air", type=float, default=0.0, help="Linear air resistance coefficient")
def run_projectile(speed, angle, dt, air):
    t, x, y, vx, vy = simulate_projectile(speed=speed, angle_deg=angle, dt=dt, air_resistance=air)
    # animate 2D
    try:
        animate_2d(t, x, y, title=f"Projectile: {speed} m/s @ {angle}°")
    except Exception:
        # fallback to static plot if animation backend fails
        plot_motion(t, y, ylabel="y (m)", title="Projectile height vs time")

@cli.command("pendulum")
@click.option("--theta", type=float, default=0.2, help="Initial angle (rad)")
@click.option("--length", type=float, default=1.0, help="Pendulum length (m)")
@click.option("--tmax", type=float, default=10.0, help="Total time (s)")
@click.option("--dt", type=float, default=0.01, help="Time step (s)")
@click.option("--nonlinear/--small-angle", default=True, help="Use full nonlinear equation if set")
def run_pendulum(theta, length, tmax, dt, nonlinear):
    t, theta_arr, omega = simulate_pendulum(theta0=theta, length=length, dt=dt, t_max=tmax, full_nonlinear=nonlinear)
    x, y = pendulum_xy(theta_arr, length)
    try:
        animate_2d(t, x, y, title="Pendulum")
    except Exception:
        plot_motion(t, theta_arr, ylabel="Angle (rad)", title="Pendulum angle vs time")

if __name__ == "__main__":
    cli()
