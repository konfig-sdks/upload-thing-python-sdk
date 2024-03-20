import typing_extensions

from upload_thing_python_sdk.paths import PathValues
from upload_thing_python_sdk.apis.paths.server_callback import ServerCallback
from upload_thing_python_sdk.apis.paths.list_files import ListFiles
from upload_thing_python_sdk.apis.paths.rename_files import RenameFiles
from upload_thing_python_sdk.apis.paths.rename_file import RenameFile
from upload_thing_python_sdk.apis.paths.delete_file import DeleteFile
from upload_thing_python_sdk.apis.paths.get_file_url import GetFileUrl
from upload_thing_python_sdk.apis.paths.get_usage_info import GetUsageInfo
from upload_thing_python_sdk.apis.paths.complete_multipart import CompleteMultipart
from upload_thing_python_sdk.apis.paths.failure_callback import FailureCallback
from upload_thing_python_sdk.apis.paths.request_file_access import RequestFileAccess
from upload_thing_python_sdk.apis.paths.prepare_upload import PrepareUpload
from upload_thing_python_sdk.apis.paths.upload_files import UploadFiles

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.SERVER_CALLBACK: ServerCallback,
        PathValues.LIST_FILES: ListFiles,
        PathValues.RENAME_FILES: RenameFiles,
        PathValues.RENAME_FILE: RenameFile,
        PathValues.DELETE_FILE: DeleteFile,
        PathValues.GET_FILE_URL: GetFileUrl,
        PathValues.GET_USAGE_INFO: GetUsageInfo,
        PathValues.COMPLETE_MULTIPART: CompleteMultipart,
        PathValues.FAILURE_CALLBACK: FailureCallback,
        PathValues.REQUEST_FILE_ACCESS: RequestFileAccess,
        PathValues.PREPARE_UPLOAD: PrepareUpload,
        PathValues.UPLOAD_FILES: UploadFiles,
    }
)

path_to_api = PathToApi(
    {
        PathValues.SERVER_CALLBACK: ServerCallback,
        PathValues.LIST_FILES: ListFiles,
        PathValues.RENAME_FILES: RenameFiles,
        PathValues.RENAME_FILE: RenameFile,
        PathValues.DELETE_FILE: DeleteFile,
        PathValues.GET_FILE_URL: GetFileUrl,
        PathValues.GET_USAGE_INFO: GetUsageInfo,
        PathValues.COMPLETE_MULTIPART: CompleteMultipart,
        PathValues.FAILURE_CALLBACK: FailureCallback,
        PathValues.REQUEST_FILE_ACCESS: RequestFileAccess,
        PathValues.PREPARE_UPLOAD: PrepareUpload,
        PathValues.UPLOAD_FILES: UploadFiles,
    }
)
