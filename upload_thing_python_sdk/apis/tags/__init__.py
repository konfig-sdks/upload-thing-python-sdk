# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from upload_thing_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    FILE = "File"
    SERVER_CALLBACK = "ServerCallback"
    USAGE_INFO = "UsageInfo"
    MULTIPART = "Multipart"
    CALLBACK = "Callback"
    UPLOAD = "Upload"
