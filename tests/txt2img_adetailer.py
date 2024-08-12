#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/txt2img"
            },
            "payload": {
                "prompt": "(8k, best quality, masterpiece, highly detailed:1.1),realistic photo of fantastic happy man,modern clothing,cinematic lightning,film grain,dynamic pose,bokeh,dof",
                "negative_prompt": "ng_deepnegative_v1_75t,(badhandv4:1.2),(worst quality:2),(low quality:2),(normal quality:2),lowres,(bad anatomy),(bad hands),((monochrome)),((grayscale)),(verybadimagenegative_v1.3:0.8),negative_hand-neg,badhandv4,nude,naked,(strabismus),cross-eye,heterochromia,((blurred))",
                "seed": -1,
                "batch_size": 1,
                "steps": 30,
                "cfg_scale": 7,
                "width": 512,
                "height": 512,
                "sampler_name": "DPM++ SDE",
                "sampler_index": "DPM++ SDE",
                "scheduler": "karras",
                "restore_faces": False,
                "alwayson_scripts": {
                    "ADetailer": {
                        "args": [
                            True,
                            False,
                            {
                                "ad_model": "face_yolov8n.pt",
                                "ad_prompt": "",
                                "ad_negative_prompt": "",
                                "ad_confidence": 0.3,
                                "ad_mask_k_largest": 0,
                                "ad_mask_min_ratio": 0.0,
                                "ad_mask_max_ratio": 1.0,
                                "ad_dilate_erode": 32,
                                "ad_x_offset": 0,
                                "ad_y_offset": 0,
                                "ad_mask_merge_invert": "None",
                                "ad_mask_blur": 4,
                                "ad_denoising_strength": 0.4,
                                "ad_inpaint_only_masked": True,
                                "ad_inpaint_only_masked_padding": 0,
                                "ad_use_inpaint_width_height": False,
                                "ad_inpaint_width": 512,
                                "ad_inpaint_height": 512,
                                "ad_use_steps": True,
                                "ad_steps": 28,
                                "ad_use_cfg_scale": False,
                                "ad_cfg_scale": 7.0,
                                "ad_use_sampler": False,
                                "ad_sampler": "DPM++ SDE Karras",
                                "ad_use_noise_multiplier": False,
                                "ad_noise_multiplier": 1.0,
                                "ad_use_clip_skip": False,
                                "ad_clip_skip": 1,
                                "ad_restore_face": False,
                                "ad_controlnet_model": "None",
                                "ad_controlnet_module": "None",
                                "ad_controlnet_weight": 1.0,
                                "ad_controlnet_guidance_start": 0.0,
                                "ad_controlnet_guidance_end": 1.0
                            }
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
