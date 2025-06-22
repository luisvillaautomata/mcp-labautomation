from mcp.server.fastmcp import FastMCP
import byonoy_devices as byonoy
from typing import List, Optional, Any, Dict

# Create an MCP server
mcp = FastMCP("Byonoy Luminescence Reader")

# Global state to hold device handle and information
device_state: Dict[str, Any] = {
    "handle": None,
    "info": None,
}

def _ensure_device_connected() -> Optional[str]:
    """Helper function to check for a device connection."""
    if device_state["handle"] is None:
        return "Error: Device not connected. Please connect first."
    return None

@mcp.tool()
def get_library_version() -> Dict[str, int]:
    """Gets the Byonoy library version."""
    version = byonoy.library_version()
    return {
        "major": version.major,
        "minor": version.minor,
        "patch": version.patch
    }

@mcp.tool()
def connect_device() -> str:
    """
    Finds and connects to the first available Lum96-compatible device.
    """
    if device_state["handle"] is not None:
        return "Error: A device is already connected."

    if byonoy.available_devices_count() == 0:
        return "Error: No Byonoy devices found."

    devices = byonoy.available_devices()
    for device_dict in devices:
        result_code, handle = byonoy.open_device(device_dict)
        if result_code == byonoy.ErrorCode.NO_ERROR:
            if byonoy.lum96_measurement_supported(handle):
                device_state["handle"] = handle
                res_code, dev_info = byonoy.get_device_information(handle)
                if res_code == byonoy.ErrorCode.NO_ERROR:
                    device_state["info"] = {
                        "sn": dev_info.sn,
                        "ref_no": dev_info.ref_no,
                        "version": dev_info.version,
                        "type": dev_info.type,
                    }
                    return f"Lum96 device connected successfully. Info: {device_state['info']}"
                else:
                    byonoy.free_device(handle)
                    device_state["handle"] = None
                    return f"Error: Failed to get device information: {res_code}"
            else:
                byonoy.free_device(handle)
    
    return "Error: No Lum96-compatible device found."

@mcp.tool()
def disconnect_device() -> str:
    """
    Disconnects the currently connected device.
    """
    error = _ensure_device_connected()
    if error:
        return error
    
    byonoy.free_device(device_state["handle"])
    device_state["handle"] = None
    device_state["info"] = None
    return "Device disconnected successfully."

@mcp.tool()
def get_device_info() -> Any:
    """
    Gets information of the connected device.
    """
    error = _ensure_device_connected()
    if error:
        return error
    return device_state["info"]

@mcp.tool()
def get_device_status() -> Any:
    """
    Gets the status of the connected device.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    result_code, device_status = byonoy.get_device_status(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get device status: {result_code}"
    return {"status": str(device_status)}

@mcp.tool()
def get_device_error() -> Any:
    """
    Gets the last error of the connected device.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    result_code, device_error = byonoy.get_device_error(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get device error: {result_code}"
    return {"error": str(device_error)}

@mcp.tool()
def get_device_uptime() -> Any:
    """
    Gets the uptime of the device, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_uptime_supported(handle):
        return "Error: Uptime not supported by this device."
    
    result_code, uptime = byonoy.get_device_uptime(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get uptime: {result_code}"
    return {"uptime_seconds": uptime}

@mcp.tool()
def get_device_slot_status() -> Any:
    """
    Gets the device slot status, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_slot_status_supported(handle):
        return "Error: Slot status not supported by this device."
    
    result_code, slot_status = byonoy.get_device_slot_status(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get slot status: {result_code}"
    return {"slot_status": str(slot_status)}

@mcp.tool()
def get_device_parts_aligned() -> Any:
    """
    Gets the device parts aligned status, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_parts_aligned_supported(handle):
        return "Error: Parts aligned status not supported by this device."
    
    result_code, parts_aligned = byonoy.get_device_parts_aligned(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get parts aligned status: {result_code}"
    return {"parts_aligned": parts_aligned}

@mcp.tool()
def get_device_readout_orientation() -> Any:
    """
    Gets the device readout orientation, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_readout_orientation_supported(handle):
        return "Error: Readout orientation not supported by this device."
    
    result_code, orientation = byonoy.get_device_readout_orientation(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get readout orientation: {result_code}"
    return {"readout_orientation": str(orientation)}

@mcp.tool()
def get_device_temperature() -> Any:
    """
    Gets the device temperature, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_temperature_supported(handle):
        return "Error: Temperature reading not supported by this device."
    
    result_code, temp = byonoy.get_device_temperature(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get temperature: {result_code}"
    return {"temperature_celsius": temp}

@mcp.tool()
def get_device_humidity() -> Any:
    """
    Gets the device humidity, if supported.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    if not byonoy.device_humidity_supported(handle):
        return "Error: Humidity reading not supported by this device."
    
    result_code, humidity = byonoy.get_device_humidity(handle)
    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Failed to get humidity: {result_code}"
    return {"relative_humidity_percent": humidity}

@mcp.tool()
def measure(mode: str = "SENSITIVE", selected_wells: Optional[List[bool]] = None) -> Any:
    """
    Performs a luminescence measurement on the Lum96 device.
    'mode' can be 'SENSITIVE' or 'FAST'.
    'selected_wells' is an optional list of 96 booleans.
    """
    error = _ensure_device_connected()
    if error:
        return error
    handle = device_state["handle"]
    
    config = byonoy.Lum96MeasurementConfig()
    
    if mode.upper() == "SENSITIVE":
        config.mode = byonoy.Lum96IntegrationMode.SENSITIVE
    elif mode.upper() == "FAST":
        config.mode = byonoy.Lum96IntegrationMode.FAST
    else:
        return "Error: Invalid measurement mode. Use 'SENSITIVE' or 'FAST'."
        
    if selected_wells is not None:
        if len(selected_wells) != 96:
            return "Error: selected_wells must be a list of 96 booleans."
        config.selected_wells = selected_wells
    else:
        config.selected_wells = [True] * 96

    result_code, values = byonoy.lum96_measure(handle, config)

    if result_code != byonoy.ErrorCode.NO_ERROR:
        return f"Error: Measurement failed with error: {result_code}"

    return {"measurement": values}

def main():
    """Entry point for the MCP server."""
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
