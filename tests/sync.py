#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/v1/sync"
            },
            "payload": {
                "hf_token": "hf_xxxxxxxxxxxxxxxxxxxxxx",
                "repo_id": "ashleykleynhans/a1111",
                "sync_path": "/workspace/stable-diffusion-webui/models"
            }
        }
    }

    post_request(payload)
