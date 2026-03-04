# Physics-Simulator

[![CI](https://github.com/ZayThihaAung/Physics-Simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/ZayThihaAung/Physics-Simulator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Physics-Simulator demonstrates and animates common undergraduate physics motions:
- Free fall (with optional air resistance)
- Projectile motion (with gravity and optional drag)
- Simple pendulum (small-angle and full dynamics)

The project focuses on clarity and education: simulation functions return time-series arrays so results can be plotted, analyzed, or used in teaching material.

Features
- Small, well-documented simulation functions (numpy)
- Matplotlib-based plotting and animation helpers
- Command-line interface for quick demos
- Unit tests and CI with GitHub Actions
- Easily extendable for more systems (damped oscillators, springs, etc.)

Quick start
```bash
git clone https://github.com/ZayThihaAung/Physics-Simulator.git
cd Physics-Simulator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Run example animations:
python -m physics_simulator.cli free-fall --height 50
python -m physics_simulator.cli projectile --speed 20 --angle 40
python -m physics_simulator.cli pendulum --length 1.0
```

Python usage
```python
from physics_simulator.simulations.free_fall import simulate_free_fall
from physics_simulator.visualization import plot_motion

t, y = simulate_free_fall(h0=20.0, dt=0.01)
plot_motion(t, y, ylabel="Height (m)", title="Free fall")
```

Project structure
```
Physics-Simulator/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── physics_simulator/
│   ├── __init__.py
│   ├── cli.py
│   ├── visualization.py
│   └── simulations/
│       ├── __init__.py
│       ├── free_fall.py
│       ├── projectile.py
│       └── pendulum.py
├── examples/
│   └── run_all.py
└── tests/
    ├── test_free_fall.py
    ├── test_projectile.py
    └── test_pendulum.py
```

Contributing
See CONTRIBUTING.md — issues, PRs, and examples are welcome. If you add features, include tests and update README usage.

License
MIT — see LICENSE.
