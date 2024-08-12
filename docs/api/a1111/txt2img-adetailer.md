# Text to Image with ADetailer

## Request

```json
{
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
      "restore_faces": false,
      "alwayson_scripts": {
        "ADetailer": {
          "args": [
            true,
            false,
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
              "ad_inpaint_only_masked": true,
              "ad_inpaint_only_masked_padding": 0,
              "ad_use_inpaint_width_height": false,
              "ad_inpaint_width": 512,
              "ad_inpaint_height": 512,
              "ad_use_steps": true,
              "ad_steps": 28,
              "ad_use_cfg_scale": false,
              "ad_cfg_scale": 7.0,
              "ad_use_sampler": false,
              "ad_sampler": "DPM++ SDE Karras",
              "ad_use_noise_multiplier": false,
              "ad_noise_multiplier": 1.0,
              "ad_use_clip_skip": false,
              "ad_clip_skip": 1,
              "ad_restore_face": false,
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
```

## Response

### RUN

```json
{
  "id": "83bbc301-5dcd-4236-9293-a65cdd681858",
  "status": "IN_QUEUE"
}
```

### RUNSYNC

```json
{
    "delayTime": 91153,
    "executionTime": 11080,
    "id": "sync-65929d7f-8115-48a7-bd84-198e2330bc85",
    "output": {
        "images": [
            "base64 encoded result image"
        ]
    },
    "status": "COMPLETED"
}
```