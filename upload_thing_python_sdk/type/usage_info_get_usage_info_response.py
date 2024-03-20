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


class RequiredUsageInfoGetUsageInfoResponse(TypedDict):
    # Total bytes used counting towards the quota. For free apps this means the total bytes used by all free apps, for paid apps this will be the same as `appTotalBytes`.
    totalBytes: typing.Union[int, float]

    # Total bytes used by this app.
    appTotalBytes: typing.Union[int, float]

    # Total number of files uploaded by this app.
    filesUploaded: typing.Union[int, float]

    # The allocated storage quota for the app in bytes.
    limitBytes: typing.Union[int, float]

class OptionalUsageInfoGetUsageInfoResponse(TypedDict, total=False):
    pass

class UsageInfoGetUsageInfoResponse(RequiredUsageInfoGetUsageInfoResponse, OptionalUsageInfoGetUsageInfoResponse):
    pass
