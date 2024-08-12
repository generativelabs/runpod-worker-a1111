#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/txt2img"
            },
            "payload": {
                "prompt": "an astronaut riding a green horse",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "steps": 30,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "sampler_name": "DPM++ SDE",
                "sampler_index": "DPM++ SDE",
                "scheduler": "karras",
                "restore_faces": False
            }
        }
    }

    post_request(payload)
