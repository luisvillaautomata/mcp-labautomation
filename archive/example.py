import byonoy_devices as byonoy
import time

# Get library version
version = byonoy.library_version()
print(f"Library version: {version.major}.{version.minor}.{version.patch}")

# Get the number of available devices
num_devices = byonoy.available_devices_count()
print("Number of available devices:", num_devices)

if num_devices > 0:
    # Get the available devices
    devices = byonoy.available_devices()

    #Uncomment to enable logging
    # byonoy.enable_logging(True)

    for device_dict in devices:
        print("Device: type =", device_dict.type, ", sn =", device_dict.sn, ", vid =", device_dict.vid, ", pid =", device_dict.pid)

    # Open the first device
    result_code, device_handle = byonoy.open_device(devices[0])
    if result_code == byonoy.ErrorCode.NO_ERROR:
        print("Device opened successfully.")
    else:
        print("Error opening device:", result_code)

    print("Device handle", device_handle)

    result_code, device_info = byonoy.get_device_information(device_handle)
    print("Device info result:", result_code)
    print("Serialnumber: ", device_info.sn)
    print("Reference number: ", device_info.ref_no)
    print("Version: ", device_info.version)
    print("Type:", device_info.type)

    result_code, device_status = byonoy.get_device_status(device_handle)
    print("Device status result:", result_code)
    print("Device status:", device_status)

    result_code, device_error = byonoy.get_device_error(device_handle)
    if (result_code == byonoy.ErrorCode.NO_ERROR):
        print("Current device error:", device_error)
    else:
        print("Failed to get the device_error with error:", result_code)

    if byonoy.device_uptime_supported(device_handle):
        result_code, device_uptime = byonoy.get_device_uptime(device_handle)
        print("Device uptime result:", result_code)
        print("Device uptime:", device_uptime)
    else:
        print("Uptime not supported")

    if byonoy.device_slot_status_supported(device_handle):
        result_code, device_slot = byonoy.get_device_slot_status(device_handle)
        print("Device slot result:", result_code)
        print("Device slot:", device_slot)
    else:
        print("Slot status not supported")

    if byonoy.device_parts_aligned_supported(device_handle):
        result_code, device_parts_aligned = byonoy.get_device_parts_aligned(device_handle)
        print("Device parts aligned result:", result_code)
        print("Device parts aligned:", device_parts_aligned)
    else:
        print("Parts aligned not supported")

    if byonoy.device_readout_orientation_supported(device_handle):
        result_code, device_readout_orientation = byonoy.get_device_readout_orientation(device_handle)
        print("Device readout orientation result:", result_code)
        print("Device readout orientation:", device_readout_orientation)
    else:
        print("Readout orientation not supported")

    if byonoy.device_temperature_supported(device_handle):
        result_code, device_temperature = byonoy.get_device_temperature(device_handle)
        print("Device temperature result:", result_code)
        print("Device temperature:", device_temperature)
    else:
        print("Temperature not supported")

    if byonoy.device_humidity_supported(device_handle):
        result_code, device_humidity = byonoy.get_device_humidity(device_handle)
        print("Device humidity result:", result_code)
        print("Device humidity:", device_humidity)
    else:
        print("Humidity not supported")

    if byonoy.abs96_available_wavelengths_supported(device_handle):
        result_code, abs_wavelengths = byonoy.abs96_get_available_wavelengths(device_handle)
        print("Abs wavelength result:", result_code)
        print("Abs wavelength:", abs_wavelengths)

        if byonoy.abs96_measurement_supported(device_handle):
            if (len(abs_wavelengths) > 1):
                config = byonoy.Abs96MultipleMeasurementConfig()
                config.sample_wavelengths = abs_wavelengths
                result_code = byonoy.abs96_initialize_multiple_measurement(device_handle, config)
                print("Abs initialize measurement result:", result_code)
                if (result_code == byonoy.ErrorCode.NO_ERROR):
                    # Sleep 15 sec to insert the plate.
                    time.sleep(15)
                    result_code, values = byonoy.abs96_multiple_measure(device_handle, config)
                    print("Abs measurement result:", result_code)
                    if (result_code == byonoy.ErrorCode.NO_ERROR):
                        print("Abs measurement:", values)
            else:
                config = byonoy.Abs96SingleMeasurementConfig()
                config.sample_wavelength = abs_wavelengths[0]
                result_code = byonoy.abs96_initialize_single_measurement(device_handle, config)
                print("Abs initialize measurement result:", result_code)
                if (result_code == byonoy.ErrorCode.NO_ERROR):
                    # Sleep 15 sec to insert the plate.
                    time.sleep(15)
                    result_code, values = byonoy.abs96_single_measure(device_handle, config)
                    print("Abs measurement result:", result_code)
                    if (result_code == byonoy.ErrorCode.NO_ERROR):
                        print("Abs measurement:", values)
        else:
            print("Abs measurement not supported")
    else:
        print("Abs wavelength not supported")

    if byonoy.abs96_modules_supported(device_handle):
        result_code, modules = byonoy.abs96_get_modules(device_handle)
        print("Abs modules result:", result_code)
        print("Abs modules:", modules)

    if byonoy.lum96_measurement_supported(device_handle):
        config = byonoy.Lum96MeasurementConfig()
        config.mode = byonoy.Lum96IntegrationMode.SENSITIVE
        config.selected_wells = [True] * 96
        result_code, values = byonoy.lum96_measure(device_handle, config)
        print("Lum measurement result:", result_code)
        if (result_code == byonoy.ErrorCode.NO_ERROR):
            print("Lum measurement:", values)
    else:
        print("Lum measurement not supported")

    # Free the resources
    byonoy.free_device(device_handle)
