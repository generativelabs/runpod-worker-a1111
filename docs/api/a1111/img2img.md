# Image to Image

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/img2img"
    },
    "payload": {
      "init_images": [
        "base64 encoded image content"
      ],
      "override_settings": {
        "sd_model_checkpoint": "sd_xl_base_1.0",
        "sd_vae": "sdxl_vae.safetensors"
      },
      "override_settings_restore_afterwards": true,
      "refiner_checkpoint": "sd_xl_refiner_1.0",
      "refiner_switch_at": 0.8,
      "prompt": "at the ocean",
      "negative_prompt": "",
      "seed": -1,
      "batch_size": 1,
      "denoising_strength": 0.75,
      "steps": 30,
      "cfg_scale": 10,
      "width": 1024,
      "height": 1024,
      "sampler_name": "DPM++ SDE",
      "sampler_index": "DPM++ SDE",
      "scheduler": "karras",
      "restore_faces": true
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
    "delayTime": 89760,
    "executionTime": 22799,
    "id": "sync-388eb08c-db56-464a-a89f-f9e6099e90b7",
    "output": {
        "images": [
            "base64 encoded result image"
        ],
      "info": "{\"prompt\": \"at the ocean\", \"all_prompts\": [\"at the ocean\"], \"negative_prompt\": \"\", \"all_negative_prompts\": [\"\"], \"seed\": 1629676606, \"all_seeds\": [1629676606], \"subseed\": 3939751520, \"all_subseeds\": [3939751520], \"subseed_strength\": 0, \"width\": 480, \"height\": 640, \"sampler_name\": \"DPM++ SDE Karras\", \"cfg_scale\": 10.0, \"steps\": 30, \"batch_size\": 1, \"restore_faces\": true, \"face_restoration_model\": \"CodeFormer\", \"sd_model_hash\": \"9aba26abdf\", \"seed_resize_from_w\": -1, \"seed_resize_from_h\": -1, \"denoising_strength\": 0.55, \"extra_generation_params\": {}, \"index_of_first_image\": 0, \"infotexts\": [\"at the ocean\\nSteps: 30, Sampler: DPM++ SDE Karras, CFG scale: 10.0, Seed: 1629676606, Face restoration: CodeFormer, Size: 480x640, Model hash: 9aba26abdf, Model: deliberate_v2, Denoising strength: 0.55, Version: 1.5.1\"], \"styles\": [], \"job_timestamp\": \"20230801194629\", \"clip_skip\": 1, \"is_using_inpainting_conditioning\": false}",
      "parameters": {
        "alwayson_scripts": {},
        "batch_size": 1,
        "cfg_scale": 10,
        "denoising_strength": 0.55,
        "do_not_save_grid": false,
        "do_not_save_samples": false,
        "eta": null,
        "height": 640,
        "image_cfg_scale": null,
        "include_init_images": false,
        "init_images": null,
        "initial_noise_multiplier": null,
        "inpaint_full_res": true,
        "inpaint_full_res_padding": 0,
        "inpainting_fill": 0,
        "inpainting_mask_invert": 0,
        "mask": null,
        "mask_blur": null,
        "mask_blur_x": 4,
        "mask_blur_y": 4,
        "n_iter": 1,
        "negative_prompt": "",
        "override_settings": null,
        "override_settings_restore_afterwards": true,
        "prompt": "at the ocean",
        "resize_mode": 0,
        "restore_faces": true,
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
        "width": 480
      }
    },
  "status": "COMPLETED"
}
```