from dataclasses import dataclass

@dataclass
class DeviceGet:
    channels: str
    applications: str
    networkSettings: str
    displaySettings: str
