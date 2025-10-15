import hashlib
import re

from cs_qualif_step2.core.domain.device.device import Device
from cs_qualif_step2.core.domain.device.device_id import DeviceId
from cs_qualif_step2.core.domain.device.exception.invalid_mac_adress import InvalidMacAddress
from cs_qualif_step2.core.domain.device.exception.invalid_time_zone import InvalidTimeZone
from cs_qualif_step2.core.application.dto.device_config import DeviceConfig


class DeviceFactory:
    def create_device(self, device_config: DeviceConfig) -> Device:
        if not re.match(r'^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$', device_config.macAddress):
            raise InvalidMacAddress("Invalid MAC address format")

        acceptedTimeZones = []
        try:
           with open(r"C:\Users\sebas\Documents\Github\ecole\cs-qualif-step2\cs_qualif_step2\core\domain\device\acceptedTimeZones.txt", 'r') as file:
               for line in file:
                   acceptedTimeZones.append(line.strip())
        except FileNotFoundError:
           print("Error: The file 'acceptedTimeZones.txt' was not found.")
        except Exception as e:
           print(f"An error occurred: {e}")

        if (device_config.timezone not in acceptedTimeZones):
            raise InvalidTimeZone("Invalid Time Zone")

        device_id = DeviceId.generate()

        return Device(
            device_id=device_id,
            macAddress=device_config.macAddress,
            model=device_config.model,
            firmwareVersion=device_config.firmwareVersion,
            serialNumber=device_config.serialNumber,
            displayName=device_config.displayName,
            location=device_config.location,
            timezone=device_config.timezone
        )
