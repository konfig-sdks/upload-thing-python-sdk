# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from upload_thing_python_sdk.paths.get_file_url import Api

from upload_thing_python_sdk.paths import PathValues

path = PathValues.GET_FILE_URL