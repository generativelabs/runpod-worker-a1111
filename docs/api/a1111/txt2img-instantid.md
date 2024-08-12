# Text to Image with InstantID

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/txt2img"
    },
    "payload": {
      "override_settings":{
        "sd_model_checkpoint":"turboDiffusionXL_v112",
        "sd_vae":"Automatic"
      },
      "prompt": "watercolor painting, vibrant, beautiful, painterly, detailed, textural, artistic",
      "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
      "seed": -1,
      "batch_size": 1,
      "steps": 15,
      "cfg_scale": 5,
      "width": 960,
      "height": 1280,
      "sampler_name": "DPM++ SDE",
      "sampler_index": "DPM++ SDE",
      "scheduler": "karras",
      "restore_faces": false,
      "alwayson_scripts": {
        "controlnet": {
          "args": [
            {
              "input_image": "base64 encoded image content",
              "module": "instant_id_face_embedding",
              "model": "ip-adapter_instant_id_sdxl",
              "weight": 1,
              "resize_mode": "Crop and Resize",
              "lowvram": false,
              "processor_res": 1024,
              "threshold_a": 75,
              "threshold_b": 75,
              "guidance": 1,
              "guidance_start": 0,
              "guidance_end": 1,
              "control_mode": "Balanced",
              "pixel_perfect": false
            },
            {
              "input_image": "base64 encoded image content",
              "module": "instant_id_face_keypoints",
              "model": "control_instant_id_sdxl",
              "weight": 1,
              "resize_mode": "Crop and Resize",
              "lowvram": false,
              "processor_res": 1024,
              "threshold_a": 75,
              "threshold_b": 75,
              "guidance": 1,
              "guidance_start": 0,
              "guidance_end": 1,
              "control_mode": "Balanced",
              "pixel_perfect": false
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
            "base64 encoded result image",
            "base64 encoded result image",
            "base64 encoded result image"
        ]
    },
  "status": "COMPLETED"
}
```