# Contributing to Recon3D-MultiView

Thank you for your interest in contributing! We welcome contributions from everyone. Please follow these guidelines to ensure a smooth collaboration.

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## How to Contribute

### 1. Fork & Clone
```bash
git clone <your-fork-url>
cd Recon3D-MultiView
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### 3. Make Changes
- Keep commits focused and atomic
- Write clear, descriptive commit messages
- Follow PEP 8 for Python code

### 4. Testing
Test your changes thoroughly:
```bash
python -m pytest tests/
```

### 5. Submit a Pull Request
- Provide a clear description of changes
- Reference related issues
- Ensure all tests pass

## Code Standards

- **Python**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- **Comments**: Add docstrings to functions and classes
- **Naming**: Use descriptive variable and function names
- **Type Hints**: Include type annotations where possible

## Reporting Issues

- Check existing issues to avoid duplicates
- Provide clear steps to reproduce
- Include relevant logs and system information
- Suggest solutions if you have ideas

## Development Setup

```bash
pip install -r requirements.txt
# Install development dependencies if available
pip install -r requirements-dev.txt
```

## Questions?

Feel free to open an issue or discussion for questions about the project.

---

Thank you for contributing! 🎉
