# Byonoy Luminescence Reader MCP Server

A Model Context Protocol (MCP) server for controlling Byonoy Lum96 luminescence readers. This package provides a standardized interface for integrating Byonoy devices into MCP-compatible applications.

## Features

- Connect to Byonoy Lum96-compatible devices
- Perform luminescence measurements in SENSITIVE or FAST modes
- Get device information, status, and error details
- Monitor device temperature, humidity, and uptime
- Support for selective well measurements
- Full MCP protocol compliance

## Installation

### Using uv (Recommended)

```bash
# Install from GitHub
uv pip install git+https://github.com/luisvillaautomata/mcp-labautomation.git

# Or install in development mode
git clone https://github.com/luisvillaautomata/mcp-labautomation.git
cd mcp-labautomation
uv pip install -e .
```

### Using pip

```bash
pip install git+https://github.com/luisvillaautomata/mcp-labautomation.git
```

## Prerequisites

- Python 3.10 or higher
- Byonoy device drivers installed
- Physical Byonoy Lum96 device connected

## Usage

### As an MCP Server

The package can be used as an MCP server that other applications can connect to:

```bash
# Run the MCP server
byonoy-mcp

# Or run directly with Python
python -m byonoy_luminescence_reader.server
```

### As a Python Library

```python
from byonoy_luminescence_reader import mcp
import byonoy_devices as byonoy

# The MCP server provides tools for device control
# Connect to device
result = mcp.tools.connect_device()
print(result)

# Get device information
info = mcp.tools.get_device_info()
print(info)

# Perform a measurement
measurement = mcp.tools.measure(mode="SENSITIVE")
print(measurement)
```

## Available Tools

- `get_library_version()` - Get Byonoy library version
- `connect_device()` - Connect to first available Lum96 device
- `disconnect_device()` - Disconnect current device
- `get_device_info()` - Get device information
- `get_device_status()` - Get device status
- `get_device_error()` - Get last device error
- `get_device_uptime()` - Get device uptime
- `get_device_temperature()` - Get device temperature
- `get_device_humidity()` - Get device humidity
- `measure(mode, selected_wells)` - Perform luminescence measurement

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/luisvillaautomata/mcp-labautomation.git
cd mcp-labautomation

# Install in development mode with dev dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Formatting

```bash
black .
flake8 .
```

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions, please use the GitHub issues page.
