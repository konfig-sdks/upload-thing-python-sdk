# coding: utf-8

"""
    UploadThing REST API

    UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a \"better S3\", but in our opinion, none found the right compromise of ownership, flexibility and safety.

    The version of the OpenAPI document: 6.4.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from upload_thing_python_sdk.pydantic.file_get_file_urls_response_data import FileGetFileUrlsResponseData

class FileGetFileUrlsResponse(BaseModel):
    data: FileGetFileUrlsResponseData = Field(alias='data')
    class Config:
        arbitrary_types_allowed = True
