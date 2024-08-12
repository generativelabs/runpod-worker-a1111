#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/img2img"
            },
            "payload": {
                "init_images": [
                    image_content
                ],
                "override_settings": {
                    "sd_model_checkpoint": "deliberate_v2",
                    "sd_vae": "vae-ft-mse-840000-ema-pruned.safetensors"
                },
                "prompt": "at the ocean",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "denoising_strength": 0.55,
                "steps": 30,
                "cfg_scale": 10,
                "width": 480,
                "height": 640,
                "sampler_name": "DPM++ SDE",
                "sampler_index": "DPM++ SDE",
                "scheduler": "karras",
                "restore_faces": True
            }
        }
    }

    post_request(payload)
