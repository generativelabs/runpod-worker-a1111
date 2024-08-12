#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/options"
            },
            "payload": {
                "sd_model_checkpoint": "deliberate_v2"
            }
        }
    }

    post_request(payload)
