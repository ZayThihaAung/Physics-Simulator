# Contributing

Thank you for your interest in Physics-Simulator!

Getting started
1. Fork the repo and create a branch: `git checkout -b feat/some-feature`
2. Open an issue to discuss large changes.
3. Add tests under `tests/` for new behavior.
4. Follow PEP8 and include docstrings for public functions.

Running tests
```bash
pip install -r requirements.txt
pytest -q
```

Development tips
- Use `matplotlib`'s non-interactive backend in CI/tests (already done in tests).
- Keep simulation functions pure (return arrays rather than plotting directly) for testability.

Code of conduct
- Be respectful and constructive in interactions.
