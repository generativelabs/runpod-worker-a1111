# Using a Webhook

You can add a `webhook` field to your payload that
contains the URI for your webhook callbacks, and then the
Serverless Endpoint will POST the response JSON to that
URI.

## Example payload to trigger webhook callback

```json
{
  "webhook": "https://76e6-45-222-21-223.ngrok.io/",
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/txt2img"
    },
    "payload": {
      "prompt": "an astronaut riding a horse",
      "negative_prompt": "",
      "seed": -1,
      "batch_size": 1,
      "steps": 30,
      "cfg_scale": 7,
      "width": 512,
      "height": 512,
      "sampler_name": "DPM++ SDE Karras",
      "sampler_index": "DPM++ SDE Karras",
      "restore_faces": False
    }
  }
}
```

## Example Webhook callback payload

```json
{
    "delayTime": 67461,
    "executionTime": 21171,
    "id": "sync-102c2af4-8ea7-4abb-a9ec-c2a56cf80a16",
    "input": {
        "api": {
            "endpoint": "/sdapi/v1/txt2img",
            "method": "POST"
        },
        "payload": {
            "batch_size": 1,
            "cfg_scale": 7,
            "height": 512,
            "negative_prompt": "",
            "prompt": "an astronaut riding a horse",
            "restore_faces": false,
            "sampler_index": "DPM++ SDE Karras",
            "sampler_name": "DPM++ SDE Karras",
            "seed": -1,
            "steps": 30,
            "width": 512
        }
    },
    "output": {
        "images": [
            "basee64 encoded image"
        ],
        "info": "{\"prompt\": \"an astronaut riding a horse\", \"all_prompts\": [\"an astronaut riding a horse\"], \"negative_prompt\": \"\", \"all_negative_prompts\": [\"\"], \"seed\": 476701233, \"all_seeds\": [476701233], \"subseed\": 4037325508, \"all_subseeds\": [4037325508], \"subseed_strength\": 0, \"width\": 512, \"height\": 512, \"sampler_name\": \"DPM++ SDE Karras\", \"cfg_scale\": 7.0, \"steps\": 30, \"batch_size\": 1, \"restore_faces\": false, \"face_restoration_model\": null, \"sd_model_hash\": null, \"seed_resize_from_w\": -1, \"seed_resize_from_h\": -1, \"denoising_strength\": 0, \"extra_generation_params\": {}, \"index_of_first_image\": 0, \"infotexts\": [\"an astronaut riding a horse\\nSteps: 30, Sampler: DPM++ SDE Karras, CFG scale: 7.0, Seed: 476701233, Size: 512x512, Model: deliberate_v2, Denoising strength: 0, Version: 1.5.1\"], \"styles\": [], \"job_timestamp\": \"20230728121717\", \"clip_skip\": 1, \"is_using_inpainting_conditioning\": false}",
        "parameters": {
            "alwayson_scripts": {},
            "batch_size": 1,
            "cfg_scale": 7,
            "denoising_strength": 0,
            "do_not_save_grid": false,
            "do_not_save_samples": false,
            "enable_hr": false,
            "eta": null,
            "firstphase_height": 0,
            "firstphase_width": 0,
            "height": 512,
            "hr_negative_prompt": "",
            "hr_prompt": "",
            "hr_resize_x": 0,
            "hr_resize_y": 0,
            "hr_sampler_name": null,
            "hr_scale": 2,
            "hr_second_pass_steps": 0,
            "hr_upscaler": null,
            "n_iter": 1,
            "negative_prompt": "",
            "override_settings": null,
            "override_settings_restore_afterwards": true,
            "prompt": "an astronaut riding a horse",
            "restore_faces": false,
            "s_churn": 0,
            "s_min_uncond": 0,
            "s_noise": 1,
            "s_tmax": null,
            "s_tmin": 0,
            "sampler_index": "DPM++ SDE Karras",
            "sampler_name": "DPM++ SDE Karras",
            "save_images": false,
            "script_args": [],
            "script_name": null,
            "seed": -1,
            "seed_resize_from_h": -1,
            "seed_resize_from_w": -1,
            "send_images": true,
            "steps": 30,
            "styles": null,
            "subseed": -1,
            "subseed_strength": 0,
            "tiling": false,
            "width": 512
        }
    },
    "status": "COMPLETED",
    "webhook": "https://76e6-45-222-21-223.ngrok.io/"
}
```