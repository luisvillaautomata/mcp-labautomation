# Installation Guide

## Quick Start

### Using uv (Recommended)

```bash
# Install directly from GitHub
uv pip install git+https://github.com/luisvillaautomata/mcp-labautomation.git

# Verify installation
byonoy-mcp --help
```

### Using pip

```bash
# Install directly from GitHub
pip install git+https://github.com/luisvillaautomata/mcp-labautomation.git

# Verify installation
byonoy-mcp --help
```

## Development Installation

If you want to contribute or modify the code:

```bash
# Clone the repository
git clone https://github.com/luisvillaautomata/mcp-labautomation.git
cd mcp-labautomation

# Install in development mode with dev dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .
flake8 .
```

## Requirements

- Python 3.10 or higher
- Byonoy device drivers installed
- Physical Byonoy Lum96 device connected

## Usage

After installation, you can:

1. **Run as an MCP server:**
   ```bash
   byonoy-mcp
   ```

2. **Import as a Python library:**
   ```python
   from byonoy_luminescence_reader import mcp
   
   # Use the MCP server tools
   result = mcp.tools.connect_device()
   ```

## Troubleshooting

If you encounter issues:

1. Make sure you have Python 3.10+ installed
2. Verify Byonoy device drivers are installed
3. Check that your device is connected
4. Try installing in a fresh virtual environment

For more help, see the main README.md or open an issue on GitHub. 