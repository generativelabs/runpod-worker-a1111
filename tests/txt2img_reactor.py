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
                    "reactor": {
                        "args": [
                            image_content,                      #0
                            True,                               #1 Enable ReActor
                            '0',                                #2 Comma separated face number(s) from swap-source image
                            '0',                                #3 Comma separated face number(s) for target image (result)
                            '/runpod-volume/stable-diffusion-webui/models/insightface/inswapper_128.onnx', #4 model path
                            'CodeFormer',                       #5 Restore Face: None; CodeFormer; GFPGAN
                            1,                                  #6 Restore visibility value
                            True,                               #7 Restore face -> Upscale
                            'lollypop',                         #8 Upscaler (type 'None' if doesn't need), see full list here: http://127.0.0.1:7860/sdapi/v1/script-info -> reactor -> sec.8
                            2,                                  #9 Upscaler scale value
                            1,                                  #10 Upscaler visibility (if scale = 1)
                            False,                              #11 Swap in source image
                            True,                               #12 Swap in generated image
                            1,                                  #13 Console Log Level (0 - min, 1 - med or 2 - max)
                            0,                                  #14 Gender Detection (Source) (0 - No, 1 - Female Only, 2 - Male Only)
                            0,                                  #15 Gender Detection (Target) (0 - No, 1 - Female Only, 2 - Male Only)
                            False,                              #16 Save the original image(s) made before swapping
                            0.8,                                #17 CodeFormer Weight (0 = maximum effect, 1 = minimum effect), 0.5 - by default
                            False,                              #18 Source Image Hash Check, True - by default
                            False,                              #19 Target Image Hash Check, False - by default
                            'CUDA',                             #20 #20 CPU or CUDA (if you have it), CPU - by default,
                            True,                               #21 Face Mask Correction
                            0,                                  #22 Select Source, 0 - Image, 1 - Face Model, 2 - Source Folder
                            #None,                               #23 Filename of the face model (from "models/reactor/faces"), e.g. elena.safetensors
                            #'/workspace/PATH_TO_FACES_IMAGES',  #24 The path to the folder containing source faces images, don't forger to set #22 to 2
                            #None,                               #25 skip it for API
                            #True,                               #26 Randomly select an image from the path
                            #True                                #27 Force Upscale even if no face found
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
