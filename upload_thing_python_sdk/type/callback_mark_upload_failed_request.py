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


class RequiredCallbackMarkUploadFailedRequest(TypedDict):
    fileKey: str

class OptionalCallbackMarkUploadFailedRequest(TypedDict, total=False):
    # The uploadId, only applicable for multipart uploads.
    uploadId: typing.Optional[str]

class CallbackMarkUploadFailedRequest(RequiredCallbackMarkUploadFailedRequest, OptionalCallbackMarkUploadFailedRequest):
    pass
