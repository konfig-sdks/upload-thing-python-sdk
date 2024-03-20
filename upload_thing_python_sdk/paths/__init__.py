# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from upload_thing_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    SERVER_CALLBACK = "/serverCallback"
    LIST_FILES = "/listFiles"
    RENAME_FILES = "/renameFiles"
    RENAME_FILE = "/renameFile"
    DELETE_FILE = "/deleteFile"
    GET_FILE_URL = "/getFileUrl"
    GET_USAGE_INFO = "/getUsageInfo"
    COMPLETE_MULTIPART = "/completeMultipart"
    FAILURE_CALLBACK = "/failureCallback"
    REQUEST_FILE_ACCESS = "/requestFileAccess"
    PREPARE_UPLOAD = "/prepareUpload"
    UPLOAD_FILES = "/uploadFiles"
