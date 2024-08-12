# Image to Image with ControlNet

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
      "prompt": "an astronaut riding a horse",
      "negative_prompt": "",
      "seed": -1,
      "batch_size": 1,
      "denoising_strength": 0.75,
      "steps": 30,
      "cfg_scale": 7,
      "width": 480,
      "height": 640,
      "sampler_name": "DPM++ SDE",
      "sampler_index": "DPM++ SDE",
      "scheduler": "karras",
      "restore_faces": false,
      "alwayson_scripts": {
        "controlnet": {
          "args": [
            {
              "module": "canny",
              "model": "control_v11p_sd15_canny",
              "weight": 1,
              "resize_mode": "Crop and Resize",
              "lowvram": false,
              "processor_res": 512,
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
    "delayTime": 133343,
    "executionTime": 17088,
    "id": "sync-34bbbbd5-520c-4056-8bf1-82cd770d984d",
    "output": {
        "images": [
            "base64 encoded result image",
            "base64 encoded controlnet image"
        ],
      "info": "{\"prompt\": \"at the ocean\", \"all_prompts\": [\"at the ocean\"], \"negative_prompt\": \"\", \"all_negative_prompts\": [\"\"], \"seed\": 3445164620, \"all_seeds\": [3445164620], \"subseed\": 2000360919, \"all_subseeds\": [2000360919], \"subseed_strength\": 0, \"width\": 480, \"height\": 640, \"sampler_name\": \"DPM++ SDE Karras\", \"cfg_scale\": 7.0, \"steps\": 30, \"batch_size\": 1, \"restore_faces\": false, \"face_restoration_model\": null, \"sd_model_hash\": \"9aba26abdf\", \"seed_resize_from_w\": -1, \"seed_resize_from_h\": -1, \"denoising_strength\": 0.75, \"extra_generation_params\": {\"ControlNet 0\": \"preprocessor: canny, model: control_v11p_sd15_canny, weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 75, 75)\"}, \"index_of_first_image\": 0, \"infotexts\": [\"at the ocean\\nSteps: 30, Sampler: DPM++ SDE Karras, CFG scale: 7.0, Seed: 3445164620, Size: 480x640, Model hash: 9aba26abdf, Model: deliberate_v2, Denoising strength: 0.75, ControlNet 0: \\\"preprocessor: canny, model: control_v11p_sd15_canny, weight: 1, starting/ending: (0, 1), resize mode: Crop and Resize, pixel perfect: False, control mode: Balanced, preprocessor params: (512, 75, 75)\\\", Version: 1.5.1\"], \"styles\": [], \"job_timestamp\": \"20230801195301\", \"clip_skip\": 1, \"is_using_inpainting_conditioning\": false}",
      "parameters": {
        "alwayson_scripts": {
          "controlnet": {
            "args": [
              {
                "control_mode": "Balanced",
                "guidance": 1,
                "guidance_end": 1,
                "guidance_start": 0,
                "lowvram": false,
                "model": "control_v11p_sd15_canny",
                "module": "canny",
                "pixel_perfect": false,
                "processor_res": 512,
                "resize_mode": "Crop and Resize",
                "threshold_a": 75,
                "threshold_b": 75,
                "weight": 1
              }
            ]
          }
        },
        "batch_size": 1,
        "cfg_scale": 7,
        "denoising_strength": 0.75,
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
        "width": 480
      }
    },
  "status": "COMPLETED"
}
```