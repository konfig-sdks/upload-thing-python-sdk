# coding: utf-8

"""
    UploadThing REST API

    UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a \"better S3\", but in our opinion, none found the right compromise of ownership, flexibility and safety.

    The version of the OpenAPI document: 6.4.0
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from upload_thing_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from upload_thing_python_sdk.api_response import AsyncGeneratorResponse
from upload_thing_python_sdk import api_client, exceptions
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

from upload_thing_python_sdk.model.err_internal_server_error import ErrInternalServerError as ErrInternalServerErrorSchema
from upload_thing_python_sdk.model.err_unauthorized import ErrUnauthorized as ErrUnauthorizedSchema
from upload_thing_python_sdk.model.file_get_file_urls_request_custom_ids import FileGetFileUrlsRequestCustomIds as FileGetFileUrlsRequestCustomIdsSchema
from upload_thing_python_sdk.model.file_get_file_urls_response import FileGetFileUrlsResponse as FileGetFileUrlsResponseSchema
from upload_thing_python_sdk.model.err_bad_request import ErrBadRequest as ErrBadRequestSchema
from upload_thing_python_sdk.model.file_get_file_urls_request import FileGetFileUrlsRequest as FileGetFileUrlsRequestSchema
from upload_thing_python_sdk.model.file_get_file_urls_request_files import FileGetFileUrlsRequestFiles as FileGetFileUrlsRequestFilesSchema
from upload_thing_python_sdk.model.file_get_file_urls_request_file_keys import FileGetFileUrlsRequestFileKeys as FileGetFileUrlsRequestFileKeysSchema

from upload_thing_python_sdk.type.err_bad_request import ErrBadRequest
from upload_thing_python_sdk.type.file_get_file_urls_request_custom_ids import FileGetFileUrlsRequestCustomIds
from upload_thing_python_sdk.type.file_get_file_urls_request import FileGetFileUrlsRequest
from upload_thing_python_sdk.type.file_get_file_urls_request_files import FileGetFileUrlsRequestFiles
from upload_thing_python_sdk.type.err_internal_server_error import ErrInternalServerError
from upload_thing_python_sdk.type.file_get_file_urls_request_file_keys import FileGetFileUrlsRequestFileKeys
from upload_thing_python_sdk.type.err_unauthorized import ErrUnauthorized
from upload_thing_python_sdk.type.file_get_file_urls_response import FileGetFileUrlsResponse

from ...api_client import Dictionary
from upload_thing_python_sdk.pydantic.err_internal_server_error import ErrInternalServerError as ErrInternalServerErrorPydantic
from upload_thing_python_sdk.pydantic.err_unauthorized import ErrUnauthorized as ErrUnauthorizedPydantic
from upload_thing_python_sdk.pydantic.file_get_file_urls_request_files import FileGetFileUrlsRequestFiles as FileGetFileUrlsRequestFilesPydantic
from upload_thing_python_sdk.pydantic.file_get_file_urls_request_file_keys import FileGetFileUrlsRequestFileKeys as FileGetFileUrlsRequestFileKeysPydantic
from upload_thing_python_sdk.pydantic.file_get_file_urls_response import FileGetFileUrlsResponse as FileGetFileUrlsResponsePydantic
from upload_thing_python_sdk.pydantic.file_get_file_urls_request_custom_ids import FileGetFileUrlsRequestCustomIds as FileGetFileUrlsRequestCustomIdsPydantic
from upload_thing_python_sdk.pydantic.err_bad_request import ErrBadRequest as ErrBadRequestPydantic
from upload_thing_python_sdk.pydantic.file_get_file_urls_request import FileGetFileUrlsRequest as FileGetFileUrlsRequestPydantic

# Header params
XUploadthingVersionSchema = schemas.StrSchema
XUploadthingFePackageSchema = schemas.StrSchema
XUploadthingBeAdapterSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
        'x-uploadthing-version': typing.Union[XUploadthingVersionSchema, str, ],
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'x-uploadthing-fe-package': typing.Union[XUploadthingFePackageSchema, str, ],
        'x-uploadthing-be-adapter': typing.Union[XUploadthingBeAdapterSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_uploadthing_version = api_client.HeaderParameter(
    name="x-uploadthing-version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XUploadthingVersionSchema,
    required=True,
)
request_header_x_uploadthing_fe_package = api_client.HeaderParameter(
    name="x-uploadthing-fe-package",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XUploadthingFePackageSchema,
)
request_header_x_uploadthing_be_adapter = api_client.HeaderParameter(
    name="x-uploadthing-be-adapter",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XUploadthingBeAdapterSchema,
)
# body param
SchemaForRequestBodyApplicationJson = FileGetFileUrlsRequestSchema


request_body_file_get_file_urls_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = FileGetFileUrlsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FileGetFileUrlsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FileGetFileUrlsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrBadRequestSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrBadRequest


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrBadRequest


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrUnauthorizedSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrUnauthorized


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrUnauthorized


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrInternalServerErrorSchema


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: ErrInternalServerError


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: ErrInternalServerError


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_file_urls_mapped_args(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _body = {}
        if files is not None:
            _body["files"] = files
        if file_keys is not None:
            _body["fileKeys"] = file_keys
        if custom_ids is not None:
            _body["customIds"] = custom_ids
        args.body = _body
        if x_uploadthing_version is not None:
            _header_params["x-uploadthing-version"] = x_uploadthing_version
        if x_uploadthing_fe_package is not None:
            _header_params["x-uploadthing-fe-package"] = x_uploadthing_fe_package
        if x_uploadthing_be_adapter is not None:
            _header_params["x-uploadthing-be-adapter"] = x_uploadthing_be_adapter
        args.header = _header_params
        return args

    async def _aget_file_urls_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_uploadthing_version,
            request_header_x_uploadthing_fe_package,
            request_header_x_uploadthing_be_adapter,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/getFileUrl',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_file_get_file_urls_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_file_urls_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_uploadthing_version,
            request_header_x_uploadthing_fe_package,
            request_header_x_uploadthing_be_adapter,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/getFileUrl',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_file_get_file_urls_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetFileUrlsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @api_client.DeprecationWarningOnce(prefix="file")
    async def aget_file_urls(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_file_urls_mapped_args(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
        )
        return await self._aget_file_urls_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="file")
    def get_file_urls(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_file_urls_mapped_args(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
        )
        return self._get_file_urls_oapg(
            body=args.body,
            header_params=args.header,
        )

class GetFileUrls(BaseApi):

    @api_client.DeprecationWarningOnce(prefix="file")
    async def aget_file_urls(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> FileGetFileUrlsResponsePydantic:
        raw_response = await self.raw.aget_file_urls(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
            **kwargs,
        )
        if validate:
            return FileGetFileUrlsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FileGetFileUrlsResponsePydantic, raw_response.body)
    
    
    @api_client.DeprecationWarningOnce(prefix="file")
    def get_file_urls(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
        validate: bool = False,
    ) -> FileGetFileUrlsResponsePydantic:
        raw_response = self.raw.get_file_urls(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
        )
        if validate:
            return FileGetFileUrlsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(FileGetFileUrlsResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @api_client.DeprecationWarningOnce(prefix="file")
    async def apost(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_file_urls_mapped_args(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
        )
        return await self._aget_file_urls_oapg(
            body=args.body,
            header_params=args.header,
            **kwargs,
        )
    
    @api_client.DeprecationWarningOnce(prefix="file")
    def post(
        self,
        x_uploadthing_version: str,
        files: typing.Optional[FileGetFileUrlsRequestFiles] = None,
        file_keys: typing.Optional[FileGetFileUrlsRequestFileKeys] = None,
        custom_ids: typing.Optional[FileGetFileUrlsRequestCustomIds] = None,
        x_uploadthing_fe_package: typing.Optional[str] = None,
        x_uploadthing_be_adapter: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_file_urls_mapped_args(
            x_uploadthing_version=x_uploadthing_version,
            files=files,
            file_keys=file_keys,
            custom_ids=custom_ids,
            x_uploadthing_fe_package=x_uploadthing_fe_package,
            x_uploadthing_be_adapter=x_uploadthing_be_adapter,
        )
        return self._get_file_urls_oapg(
            body=args.body,
            header_params=args.header,
        )

