# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from upload_thing_python_sdk.paths.prepare_upload import Api

from upload_thing_python_sdk.paths import PathValues

path = PathValues.PREPARE_UPLOAD