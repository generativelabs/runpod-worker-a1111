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
                "override_settings":{
                    "sd_model_checkpoint":"turboDiffusionXL_v112",
                    "CLIP_stop_at_last_layers": 1
                },
                "prompt": "a male, comic, graphic illustration, comic art, graphic novel art, vibrant, highly detailed, comic book background",
                "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green,  topless, no shirt, shirtless, exposed stomach, belly button, (deformed, distorted, disfigured:1.3), poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, (mutated hands and fingers:1.4), disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, watermark, stock image, signature, logo, brand, naked, nsfw, nipples, breasts, underwear, bikini, stomach, belly button,",
                "seed": -1,
                "batch_size": 1,
                "steps": 8,
                "cfg_scale": 5,
                "width": 960,
                "height": 1280,
                "hr_scale": 1.6,
                "enable_hr": True,
                "hr_prompt": "",
                "hr_upscaler": "R-ESRGAN 4x+",
                "denoising_strength": 0.05,
                "hr_negative_prompt": "",
                "hr_second_pass_steps": 0,
                "sampler_name": "DPM++ SDE",
                "sampler_index": "DPM++ SDE",
                "scheduler": "karras",
                "restore_faces": False,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "input_image": image_content,
                                "module": "instant_id_face_embedding",
                                "model": "ip-adapter_instant_id_sdxl",
                                "weight": 0.9,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 1024,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            },
                            {
                                "input_image": image_content,
                                "module": "instant_id_face_keypoints",
                                "model": "control_instant_id_sdxl",
                                "weight": 0.9,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 1024,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            }
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
