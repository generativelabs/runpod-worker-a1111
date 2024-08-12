#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/interrogate"
            },
            "payload": {
                "image": image_content,
                "model": "deepdanbooru"
            }
        }
    }

    post_request(payload)
