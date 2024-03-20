import typing_extensions

from upload_thing_python_sdk.apis.tags import TagValues
from upload_thing_python_sdk.apis.tags.file_api import FileApi
from upload_thing_python_sdk.apis.tags.server_callback_api import ServerCallbackApi
from upload_thing_python_sdk.apis.tags.usage_info_api import UsageInfoApi
from upload_thing_python_sdk.apis.tags.multipart_api import MultipartApi
from upload_thing_python_sdk.apis.tags.callback_api import CallbackApi
from upload_thing_python_sdk.apis.tags.upload_api import UploadApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.FILE: FileApi,
        TagValues.SERVER_CALLBACK: ServerCallbackApi,
        TagValues.USAGE_INFO: UsageInfoApi,
        TagValues.MULTIPART: MultipartApi,
        TagValues.CALLBACK: CallbackApi,
        TagValues.UPLOAD: UploadApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.FILE: FileApi,
        TagValues.SERVER_CALLBACK: ServerCallbackApi,
        TagValues.USAGE_INFO: UsageInfoApi,
        TagValues.MULTIPART: MultipartApi,
        TagValues.CALLBACK: CallbackApi,
        TagValues.UPLOAD: UploadApi,
    }
)
