# coding: utf-8

"""
    UploadThing REST API

    UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a \"better S3\", but in our opinion, none found the right compromise of ownership, flexibility and safety.

    The version of the OpenAPI document: 6.4.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from upload_thing_python_sdk import schemas  # noqa: F401


class FileRenameFilesRequestUpdates(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['FileRenameFilesRequestUpdatesItem']:
            return FileRenameFilesRequestUpdatesItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['FileRenameFilesRequestUpdatesItem'], typing.List['FileRenameFilesRequestUpdatesItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FileRenameFilesRequestUpdates':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'FileRenameFilesRequestUpdatesItem':
        return super().__getitem__(i)

from upload_thing_python_sdk.model.file_rename_files_request_updates_item import FileRenameFilesRequestUpdatesItem
