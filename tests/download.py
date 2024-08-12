#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/v1/download"
            },
            "payload": {
                "source_url": "https://huggingface.co/ashleykleynhans/upscalers/resolve/main/4x-UltraSharp.pth",
                "download_path": "/workspace/stable-diffusion-webui/models/ESRGAN/4x-UltraSharp.pth"
            }
        }
    }

    post_request(payload)
