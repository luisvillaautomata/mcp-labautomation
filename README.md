<<<<<<< HEAD
# Python SDK Example

This example demonstrates the basic usage of the Byonoy Device Library in Python.

## Setup

Install the Python dependencies, preferably into a virtual environment.

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run

Make sure the device is attached, then run the example client script.

```
python example.py
```

The script should list some information about the attached devices. Depending on the attached device type the script will then perform a measurement.

## Mock Data

The library itself does not provide simulated devices, but through the magic of Python we can make an ad-hoc mock device by replacing the relevant library calls. See `mock.py` for a slightly stripped down version of `example.py` with all the relevant functions mocked.
=======
# mcp-labautomation
 Repo for MCP Build Day for Lab Automation
>>>>>>> 38ff7c779f914b8551854be15a59a7df155b06ab
