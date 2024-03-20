# coding: utf-8

"""
    UploadThing REST API

    UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a \"better S3\", but in our opinion, none found the right compromise of ownership, flexibility and safety.

    The version of the OpenAPI document: 6.4.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import upload_thing_python_sdk
from upload_thing_python_sdk.paths.delete_file import post
from upload_thing_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDeleteFile(ApiTestMixin, unittest.TestCase):
    """
    DeleteFile unit test stubs
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
