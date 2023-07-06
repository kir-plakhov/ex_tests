# mypy: ignore-errors
from datetime import datetime
from enum import Enum
from ipaddress import IPv4Address, IPv6Address
from typing import Optional, Union
from uuid import UUID
from pydantic import BaseModel, Field, NonNegativeInt, constr, validator


# class EventType(str, Enum):
#     form_send = 'form_send'
#     caf_form = 'caf_form'
#     caf_nav = 'caf_nav'
#     scroll = 'scroll'
#     page_open = 'page_open'
#     page_close = 'page_close'
#     pa_enter = 'pa_enter'
#     valid_event_types: set[str] = {et.value for et in EventType}


# class ValidationMixin:
#     @validator('*', pre=True)
#     def convert_to_none(cls, v):
#         """Convert string value "None" into python None."""
#         return None if v == 'None' else v
#     @validator('event_type', pre=True)
#     def validate_event_type(cls, v):
#         """Validate event type."""
#         if v in valid_event_types:
#             raise ValueError(f'Wrong event_type: {v}')
#         return v


class IAFSourceMessage(BaseModel): # ValidationMixin,
    track_uid: Optional[UUID]
    user_uid: Optional[UUID]
    session_uid: Optional[UUID] = Field(default=None, alias='session_id')
    google_id: Optional[str] = Field(default=None, alias='ga_id')
    ip_address: Union[IPv4Address, IPv6Address]
    user_fingerprint: constr(min_length=2, max_length=32)
    page_url: str = Field(default='default')
    event_type: constr(min_length=2, max_length=10)
    referrer_url: str = Field(default='')
    event_timestamp: NonNegativeInt = Field(alias='server_timestamp')
    client_timestamp: NonNegativeInt = Field(alias='timestamp')
    unstructured_data: dict = Field(default_factory=dict)


class Config:
    allow_population_by_field_name = True
