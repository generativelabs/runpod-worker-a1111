# Text to Image

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/txt2img"
    },
    "payload": {
      "override_settings": {
        "sd_model_checkpoint": "sd_xl_base_1.0",
        "sd_vae": "sdxl_vae.safetensors"
      },
      "override_settings_restore_afterwards": true,
      "refiner_checkpoint": "sd_xl_refiner_1.0",
      "refiner_switch_at": 0.8,
      "prompt": "an astronaut riding a horse",
      "negative_prompt": "",
      "seed": -1,
      "batch_size": 1,
      "steps": 30,
      "cfg_scale": 7,
      "width": 1024,
      "height": 1024,
      "sampler_name": "DPM++ SDE",
      "sampler_index": "DPM++ SDE",
      "scheduler": "karras",
      "restore_faces": false
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
        ],
      "info": "{\"prompt\": \"an astronaut riding a horse\", \"all_prompts\": [\"an astronaut riding a horse\"], \"negative_prompt\": \"\", \"all_negative_prompts\": [\"\"], \"seed\": 2750444522, \"all_seeds\": [2750444522], \"subseed\": 1304004720, \"all_subseeds\": [1304004720], \"subseed_strength\": 0, \"width\": 512, \"height\": 512, \"sampler_name\": \"DPM++ SDE Karras\", \"cfg_scale\": 7.0, \"steps\": 30, \"batch_size\": 1, \"restore_faces\": false, \"face_restoration_model\": null, \"sd_model_hash\": \"9aba26abdf\", \"seed_resize_from_w\": -1, \"seed_resize_from_h\": -1, \"denoising_strength\": 0, \"extra_generation_params\": {}, \"index_of_first_image\": 0, \"infotexts\": [\"an astronaut riding a horse\\nSteps: 30, Sampler: DPM++ SDE Karras, CFG scale: 7.0, Seed: 2750444522, Size: 512x512, Model hash: 9aba26abdf, Model: deliberate_v2, Denoising strength: 0, Version: 1.5.1\"], \"styles\": [], \"job_timestamp\": \"20230801194341\", \"clip_skip\": 1, \"is_using_inpainting_conditioning\": false}",
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
  "status": "COMPLETED"
}
```