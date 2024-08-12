#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "GET",
                "endpoint": "/sdapi/v1/schedulers"
            },
            "payload": {}
        }
    }

    post_request(payload)
