from pydantic import BaseModel, validator

class DeviceGetRequest(BaseModel):
    channels: str
    applications: str
    networkSettings: str
    displaySettings: str
    @validator('channels', 'applications', 'networkSettings', 'displaySettings')
    def not_empty(cls, v):
        if v is None or v.strip() == '':
            raise ValueError('Field cannot be empty or null')
        return v
