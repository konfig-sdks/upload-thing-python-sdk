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


class MultipartUploadURLs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "fileName",
            "urls",
            "ContentDisposition",
            "chunkSize",
            "pollingUrl",
            "uploadId",
            "chunkCount",
            "fileUrl",
            "pollingJwt",
            "customId",
            "fileType",
            "key",
        }
        
        class properties:
            key = schemas.StrSchema
            fileName = schemas.StrSchema
            fileType = schemas.StrSchema
            fileUrl = schemas.StrSchema
            
            
            class ContentDisposition(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INLINE(cls):
                    return cls("inline")
                
                @schemas.classproperty
                def ATTACHMENT(cls):
                    return cls("attachment")
            pollingJwt = schemas.StrSchema
            pollingUrl = schemas.StrSchema
            
            
            class customId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'customId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def urls() -> typing.Type['MultipartUploadURLsUrls']:
                return MultipartUploadURLsUrls
            uploadId = schemas.StrSchema
            chunkSize = schemas.NumberSchema
            chunkCount = schemas.NumberSchema
            __annotations__ = {
                "key": key,
                "fileName": fileName,
                "fileType": fileType,
                "fileUrl": fileUrl,
                "ContentDisposition": ContentDisposition,
                "pollingJwt": pollingJwt,
                "pollingUrl": pollingUrl,
                "customId": customId,
                "urls": urls,
                "uploadId": uploadId,
                "chunkSize": chunkSize,
                "chunkCount": chunkCount,
            }
    
    fileName: MetaOapg.properties.fileName
    urls: 'MultipartUploadURLsUrls'
    ContentDisposition: MetaOapg.properties.ContentDisposition
    chunkSize: MetaOapg.properties.chunkSize
    pollingUrl: MetaOapg.properties.pollingUrl
    uploadId: MetaOapg.properties.uploadId
    chunkCount: MetaOapg.properties.chunkCount
    fileUrl: MetaOapg.properties.fileUrl
    pollingJwt: MetaOapg.properties.pollingJwt
    customId: MetaOapg.properties.customId
    fileType: MetaOapg.properties.fileType
    key: MetaOapg.properties.key
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileType"]) -> MetaOapg.properties.fileType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fileUrl"]) -> MetaOapg.properties.fileUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ContentDisposition"]) -> MetaOapg.properties.ContentDisposition: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pollingJwt"]) -> MetaOapg.properties.pollingJwt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pollingUrl"]) -> MetaOapg.properties.pollingUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customId"]) -> MetaOapg.properties.customId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urls"]) -> 'MultipartUploadURLsUrls': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploadId"]) -> MetaOapg.properties.uploadId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chunkSize"]) -> MetaOapg.properties.chunkSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["chunkCount"]) -> MetaOapg.properties.chunkCount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key", "fileName", "fileType", "fileUrl", "ContentDisposition", "pollingJwt", "pollingUrl", "customId", "urls", "uploadId", "chunkSize", "chunkCount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileName"]) -> MetaOapg.properties.fileName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileType"]) -> MetaOapg.properties.fileType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fileUrl"]) -> MetaOapg.properties.fileUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ContentDisposition"]) -> MetaOapg.properties.ContentDisposition: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pollingJwt"]) -> MetaOapg.properties.pollingJwt: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pollingUrl"]) -> MetaOapg.properties.pollingUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customId"]) -> MetaOapg.properties.customId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> 'MultipartUploadURLsUrls': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploadId"]) -> MetaOapg.properties.uploadId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chunkSize"]) -> MetaOapg.properties.chunkSize: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["chunkCount"]) -> MetaOapg.properties.chunkCount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key", "fileName", "fileType", "fileUrl", "ContentDisposition", "pollingJwt", "pollingUrl", "customId", "urls", "uploadId", "chunkSize", "chunkCount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        fileName: typing.Union[MetaOapg.properties.fileName, str, ],
        urls: 'MultipartUploadURLsUrls',
        ContentDisposition: typing.Union[MetaOapg.properties.ContentDisposition, str, ],
        chunkSize: typing.Union[MetaOapg.properties.chunkSize, decimal.Decimal, int, float, ],
        pollingUrl: typing.Union[MetaOapg.properties.pollingUrl, str, ],
        uploadId: typing.Union[MetaOapg.properties.uploadId, str, ],
        chunkCount: typing.Union[MetaOapg.properties.chunkCount, decimal.Decimal, int, float, ],
        fileUrl: typing.Union[MetaOapg.properties.fileUrl, str, ],
        pollingJwt: typing.Union[MetaOapg.properties.pollingJwt, str, ],
        customId: typing.Union[MetaOapg.properties.customId, None, str, ],
        fileType: typing.Union[MetaOapg.properties.fileType, str, ],
        key: typing.Union[MetaOapg.properties.key, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MultipartUploadURLs':
        return super().__new__(
            cls,
            *args,
            fileName=fileName,
            urls=urls,
            ContentDisposition=ContentDisposition,
            chunkSize=chunkSize,
            pollingUrl=pollingUrl,
            uploadId=uploadId,
            chunkCount=chunkCount,
            fileUrl=fileUrl,
            pollingJwt=pollingJwt,
            customId=customId,
            fileType=fileType,
            key=key,
            _configuration=_configuration,
            **kwargs,
        )

from upload_thing_python_sdk.model.multipart_upload_urls_urls import MultipartUploadURLsUrls
