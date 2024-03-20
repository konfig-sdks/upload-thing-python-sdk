<div align="left">

[![Visit Uploadthing](./header.png)](https://uploadthing.com)

# Uploadthing<a id="uploadthing"></a>

UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a \"better S3\", but in our opinion, none found the right compromise of ownership, flexibility and safety.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`uploadthing.callback.mark_upload_failed`](#uploadthingcallbackmark_upload_failed)
  * [`uploadthing.file.get_file_urls`](#uploadthingfileget_file_urls)
  * [`uploadthing.file.list_files`](#uploadthingfilelist_files)
  * [`uploadthing.file.mark_for_deletion`](#uploadthingfilemark_for_deletion)
  * [`uploadthing.file.rename_files`](#uploadthingfilerename_files)
  * [`uploadthing.file.request_presigned_url`](#uploadthingfilerequest_presigned_url)
  * [`uploadthing.file.request_presigned_urls`](#uploadthingfilerequest_presigned_urls)
  * [`uploadthing.file.update_file_name`](#uploadthingfileupdate_file_name)
  * [`uploadthing.multipart.complete_upload`](#uploadthingmultipartcomplete_upload)
  * [`uploadthing.server_callback.get_data`](#uploadthingserver_callbackget_data)
  * [`uploadthing.server_callback.set_data`](#uploadthingserver_callbackset_data)
  * [`uploadthing.upload.request_presigned_urls`](#uploadthinguploadrequest_presigned_urls)
  * [`uploadthing.usage_info.get_usage_info`](#uploadthingusage_infoget_usage_info)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=UploadThing&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from upload_thing_python_sdk import UploadThing, ApiException

uploadthing = UploadThing(
    api_key_auth="YOUR_API_KEY",
)

try:
    mark_upload_failed_response = uploadthing.callback.mark_upload_failed(
        file_key="string_example",
        x_uploadthing_version="6.4.0",
        upload_id="string_example",
        x_uploadthing_fe_package="@uploadthing/react",
        x_uploadthing_be_adapter="express",
    )
    print(mark_upload_failed_response)
except ApiException as e:
    print("Exception when calling CallbackApi.mark_upload_failed: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
        pprint(e.body["data"])
    if e.status == 401:
        pprint(e.body["error"])
        pprint(e.body["data"])
    if e.status == 500:
        pprint(e.body["error"])
        pprint(e.body["data"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from upload_thing_python_sdk import UploadThing, ApiException

uploadthing = UploadThing(
    api_key_auth="YOUR_API_KEY",
)


async def main():
    try:
        mark_upload_failed_response = await uploadthing.callback.amark_upload_failed(
            file_key="string_example",
            x_uploadthing_version="6.4.0",
            upload_id="string_example",
            x_uploadthing_fe_package="@uploadthing/react",
            x_uploadthing_be_adapter="express",
        )
        print(mark_upload_failed_response)
    except ApiException as e:
        print("Exception when calling CallbackApi.mark_upload_failed: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["error"])
            pprint(e.body["data"])
        if e.status == 401:
            pprint(e.body["error"])
            pprint(e.body["data"])
        if e.status == 500:
            pprint(e.body["error"])
            pprint(e.body["data"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from upload_thing_python_sdk import UploadThing, ApiException

uploadthing = UploadThing(
    api_key_auth="YOUR_API_KEY",
)

try:
    mark_upload_failed_response = uploadthing.callback.raw.mark_upload_failed(
        file_key="string_example",
        x_uploadthing_version="6.4.0",
        upload_id="string_example",
        x_uploadthing_fe_package="@uploadthing/react",
        x_uploadthing_be_adapter="express",
    )
    pprint(mark_upload_failed_response.body)
    pprint(mark_upload_failed_response.body["success"])
    pprint(mark_upload_failed_response.headers)
    pprint(mark_upload_failed_response.status)
    pprint(mark_upload_failed_response.round_trip_time)
except ApiException as e:
    print("Exception when calling CallbackApi.mark_upload_failed: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["error"])
        pprint(e.body["data"])
    if e.status == 401:
        pprint(e.body["error"])
        pprint(e.body["data"])
    if e.status == 500:
        pprint(e.body["error"])
        pprint(e.body["data"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `uploadthing.callback.mark_upload_failed`<a id="uploadthingcallbackmark_upload_failed"></a>

Mark an upload as failed, or abort a multipart upload. This will free up resources and revert the storage quota.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mark_upload_failed_response = uploadthing.callback.mark_upload_failed(
    file_key="string_example",
    x_uploadthing_version="6.4.0",
    upload_id="string_example",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_key: `str`<a id="file_key-str"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### upload_id: `Optional[str]`<a id="upload_id-optionalstr"></a>

The uploadId, only applicable for multipart uploads.

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CallbackMarkUploadFailedRequest`](./upload_thing_python_sdk/type/callback_mark_upload_failed_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CallbackMarkUploadFailedResponse`](./upload_thing_python_sdk/pydantic/callback_mark_upload_failed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/failureCallback` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.get_file_urls`<a id="uploadthingfileget_file_urls"></a>

Get a list of URLs for given file keys. This API is deprecated, use `https://utfs.io/f/FILE_KEY`.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_urls_response = uploadthing.file.get_file_urls(
    x_uploadthing_version="6.4.0",
    files=["string_example"],
    file_keys=["string_example"],
    custom_ids=["string_example"],
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### files: [`FileGetFileUrlsRequestFiles`](./upload_thing_python_sdk/type/file_get_file_urls_request_files.py)<a id="files-filegetfileurlsrequestfilesupload_thing_python_sdktypefile_get_file_urls_request_filespy"></a>

##### file_keys: [`FileGetFileUrlsRequestFileKeys`](./upload_thing_python_sdk/type/file_get_file_urls_request_file_keys.py)<a id="file_keys-filegetfileurlsrequestfilekeysupload_thing_python_sdktypefile_get_file_urls_request_file_keyspy"></a>

##### custom_ids: [`FileGetFileUrlsRequestCustomIds`](./upload_thing_python_sdk/type/file_get_file_urls_request_custom_ids.py)<a id="custom_ids-filegetfileurlsrequestcustomidsupload_thing_python_sdktypefile_get_file_urls_request_custom_idspy"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileGetFileUrlsRequest`](./upload_thing_python_sdk/type/file_get_file_urls_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileGetFileUrlsResponse`](./upload_thing_python_sdk/pydantic/file_get_file_urls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/getFileUrl` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.list_files`<a id="uploadthingfilelist_files"></a>

List files for the current app. Response is paginated.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_files_response = uploadthing.file.list_files(
    limit=500,
    offset=0,
    x_uploadthing_version="6.4.0",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

The maximum number of files to retrieve.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

The number of files to skip.

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileListFilesRequest`](./upload_thing_python_sdk/type/file_list_files_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileListFilesResponse`](./upload_thing_python_sdk/pydantic/file_list_files_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/listFiles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.mark_for_deletion`<a id="uploadthingfilemark_for_deletion"></a>

Mark files for deletion. The files will be deleted at the storage provider shortly after.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mark_for_deletion_response = uploadthing.file.mark_for_deletion(
    x_uploadthing_version="6.4.0",
    files=["string_example"],
    file_keys=["string_example"],
    custom_ids=["string_example"],
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### files: [`FileMarkForDeletionRequestFiles`](./upload_thing_python_sdk/type/file_mark_for_deletion_request_files.py)<a id="files-filemarkfordeletionrequestfilesupload_thing_python_sdktypefile_mark_for_deletion_request_filespy"></a>

##### file_keys: [`FileMarkForDeletionRequestFileKeys`](./upload_thing_python_sdk/type/file_mark_for_deletion_request_file_keys.py)<a id="file_keys-filemarkfordeletionrequestfilekeysupload_thing_python_sdktypefile_mark_for_deletion_request_file_keyspy"></a>

##### custom_ids: [`FileMarkForDeletionRequestCustomIds`](./upload_thing_python_sdk/type/file_mark_for_deletion_request_custom_ids.py)<a id="custom_ids-filemarkfordeletionrequestcustomidsupload_thing_python_sdktypefile_mark_for_deletion_request_custom_idspy"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileMarkForDeletionRequest`](./upload_thing_python_sdk/type/file_mark_for_deletion_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileMarkForDeletionResponse`](./upload_thing_python_sdk/pydantic/file_mark_for_deletion_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/deleteFile` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.rename_files`<a id="uploadthingfilerename_files"></a>

Rename files.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rename_files_response = uploadthing.file.rename_files(
    updates=[
        {
            "new_name": "new_name_example",
        }
    ],
    x_uploadthing_version="6.4.0",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### updates: [`FileRenameFilesRequestUpdates`](./upload_thing_python_sdk/type/file_rename_files_request_updates.py)<a id="updates-filerenamefilesrequestupdatesupload_thing_python_sdktypefile_rename_files_request_updatespy"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileRenameFilesRequest`](./upload_thing_python_sdk/type/file_rename_files_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileRenameFilesResponse`](./upload_thing_python_sdk/pydantic/file_rename_files_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/renameFiles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.request_presigned_url`<a id="uploadthingfilerequest_presigned_url"></a>

Request a presigned GET url for a private file.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_presigned_url_response = uploadthing.file.request_presigned_url(
    x_uploadthing_version="6.4.0",
    file_key="string_example",
    custom_id="string_example",
    expires_in=0,
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### file_key: `str`<a id="file_key-str"></a>

##### custom_id: `str`<a id="custom_id-str"></a>

##### expires_in: `Union[int, float]`<a id="expires_in-unionint-float"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileRequestPresignedUrlRequest`](./upload_thing_python_sdk/type/file_request_presigned_url_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileRequestPresignedUrlResponse`](./upload_thing_python_sdk/pydantic/file_request_presigned_url_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/requestFileAccess` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.request_presigned_urls`<a id="uploadthingfilerequest_presigned_urls"></a>

Request presigned URLs for file uploads without file routes. NOTE: This spec complies with SDK versions ^6.4. Response may vary for older versions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_presigned_urls_response = uploadthing.file.request_presigned_urls(
    files=[
        {
            "name": "name_example",
            "size": 0,
            "type": "type_example",
        }
    ],
    content_disposition="inline",
    x_uploadthing_version="6.4.0",
    acl="public-read",
    metadata=None,
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### files: [`FileRequestPresignedUrlsRequestFiles`](./upload_thing_python_sdk/type/file_request_presigned_urls_request_files.py)<a id="files-filerequestpresignedurlsrequestfilesupload_thing_python_sdktypefile_request_presigned_urls_request_filespy"></a>

##### content_disposition: `str`<a id="content_disposition-str"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### acl: `str`<a id="acl-str"></a>

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./upload_thing_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-noneupload_thing_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileRequestPresignedUrlsRequest`](./upload_thing_python_sdk/type/file_request_presigned_urls_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileRequestPresignedUrlsResponse`](./upload_thing_python_sdk/pydantic/file_request_presigned_urls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/uploadFiles` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.file.update_file_name`<a id="uploadthingfileupdate_file_name"></a>

Use /renameFiles instead.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_file_name_response = uploadthing.file.update_file_name(
    updates=[
        {
            "new_name": "new_name_example",
        }
    ],
    x_uploadthing_version="6.4.0",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### updates: [`FileUpdateFileNameRequestUpdates`](./upload_thing_python_sdk/type/file_update_file_name_request_updates.py)<a id="updates-fileupdatefilenamerequestupdatesupload_thing_python_sdktypefile_update_file_name_request_updatespy"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FileUpdateFileNameRequest`](./upload_thing_python_sdk/type/file_update_file_name_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`FileUpdateFileNameResponse`](./upload_thing_python_sdk/pydantic/file_update_file_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/renameFile` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.multipart.complete_upload`<a id="uploadthingmultipartcomplete_upload"></a>

Complete a multipart upload. This will finalize the upload and make the file available for download.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
complete_upload_response = uploadthing.multipart.complete_upload(
    file_key="string_example",
    upload_id="string_example",
    etags=[
        {
            "tag": "tag_example",
            "part_number": 3.14,
        }
    ],
    x_uploadthing_version="6.4.0",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_key: `str`<a id="file_key-str"></a>

##### upload_id: `str`<a id="upload_id-str"></a>

##### etags: [`MultipartCompleteUploadRequestEtags`](./upload_thing_python_sdk/type/multipart_complete_upload_request_etags.py)<a id="etags-multipartcompleteuploadrequestetagsupload_thing_python_sdktypemultipart_complete_upload_request_etagspy"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MultipartCompleteUploadRequest`](./upload_thing_python_sdk/type/multipart_complete_upload_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MultipartCompleteUploadResponse`](./upload_thing_python_sdk/pydantic/multipart_complete_upload_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/completeMultipart` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.server_callback.get_data`<a id="uploadthingserver_callbackget_data"></a>

Poll for server callback data. This is used to retrieve the data returned from `onUploadComplete` callback.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_data_response = uploadthing.server_callback.get_data(
    authorization="authorization_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization: `str`<a id="authorization-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ServerCallbackGetDataResponse`](./upload_thing_python_sdk/pydantic/server_callback_get_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serverCallback` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.server_callback.set_data`<a id="uploadthingserver_callbackset_data"></a>

Set server callback data. This is used to set the data returned from `onUploadComplete` callback.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_data_response = uploadthing.server_callback.set_data(
    file_key="string_example",
    x_uploadthing_version="6.4.0",
    callback_data=None,
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_key: `str`<a id="file_key-str"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### callback_data: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./upload_thing_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="callback_data-unionbool-date-datetime-dict-float-int-list-str-noneupload_thing_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServerCallbackSetDataRequest`](./upload_thing_python_sdk/type/server_callback_set_data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServerCallbackSetDataResponse`](./upload_thing_python_sdk/pydantic/server_callback_set_data_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serverCallback` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.upload.request_presigned_urls`<a id="uploadthinguploadrequest_presigned_urls"></a>

Request presigned URLs for file uploads through based on your file router. NOTE: This spec complies with SDK versions ^6.4. Response may vary for older versions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
request_presigned_urls_response = uploadthing.upload.request_presigned_urls(
    callback_url="string_example",
    callback_slug="string_example",
    files=[
        {
            "name": "name_example",
            "size": 0,
        }
    ],
    route_config=["string_example"],
    x_uploadthing_version="6.4.0",
    metadata=None,
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### callback_url: `str`<a id="callback_url-str"></a>

##### callback_slug: `str`<a id="callback_slug-str"></a>

##### files: [`UploadRequestPresignedUrlsRequestFiles`](./upload_thing_python_sdk/type/upload_request_presigned_urls_request_files.py)<a id="files-uploadrequestpresignedurlsrequestfilesupload_thing_python_sdktypeupload_request_presigned_urls_request_filespy"></a>

##### route_config: `RouteConfig`<a id="route_config-routeconfig"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./upload_thing_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-noneupload_thing_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UploadRequestPresignedUrlsRequest`](./upload_thing_python_sdk/type/upload_request_presigned_urls_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UploadRequestPresignedUrlsResponse`](./upload_thing_python_sdk/pydantic/upload_request_presigned_urls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/prepareUpload` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `uploadthing.usage_info.get_usage_info`<a id="uploadthingusage_infoget_usage_info"></a>

Retrieve usage info for the app associated with the provided API key.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_usage_info_response = uploadthing.usage_info.get_usage_info(
    x_uploadthing_version="6.4.0",
    x_uploadthing_fe_package="@uploadthing/react",
    x_uploadthing_be_adapter="express",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### x_uploadthing_version: `str`<a id="x_uploadthing_version-str"></a>

##### x_uploadthing_fe_package: `str`<a id="x_uploadthing_fe_package-str"></a>

##### x_uploadthing_be_adapter: `str`<a id="x_uploadthing_be_adapter-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`UsageInfoGetUsageInfoResponse`](./upload_thing_python_sdk/pydantic/usage_info_get_usage_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/getUsageInfo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
