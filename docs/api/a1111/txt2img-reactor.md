# Text to Image with ReActor

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
        "reactor": {
          "args": [
            "base64 encoded image content",     #0
            true,                               #1 Enable ReActor
            "0",                                #2 Comma separated face number(s) from swap-source image
            "0",                                #3 Comma separated face number(s) for target image (result)
            ",/runpod-volume/stable-diffusion-webui/models/insightface/inswapper_128.onnx", #4 model path
            "CodeFormer",                       #5 Restore Face: None; CodeFormer; GFPGAN
            1,                                  #6 Restore visibility value
            true,                               #7 Restore face -> Upscale
            "lollypop",                         #8 Upscaler (type 'None' if doesn't need), see full list here: http://127.0.0.1:7860/sdapi/v1/script-info -> reactor -> sec.8,
            2,                                  #9 Upscaler scale value
            1,                                  #10 Upscaler visibility (if scale = 1)
            false,                              #11 Swap in source image
            true,                               #12 Swap in generated image
            1,                                  #13 Console Log Level (0 - min, 1 - med or 2 - max)
            0,                                  #14 Gender Detection (Source) (0 - No, 1 - Female Only, 2 - Male Only)
            0,                                  #15 Gender Detection (Target) (0 - No, 1 - Female Only, 2 - Male Only)
            false,                              #16 Save the original image(s) made before swapping
            0.8,                                #17 CodeFormer Weight (0 = maximum effect, 1 = minimum effect), 0.5 - by default
            false,                              #18 Source Image Hash Check, True - by default
            false,                              #19 Target Image Hash Check, False - by default
            "CUDA",                             #20 #20 CPU or CUDA (if you have it), CPU - by default,
            true,                               #21 Face Mask Correction
            0,                                  #22 Select Source, 0 - Image, 1 - Face Model
            null                                #23 Filename of the face model (from "models/reactor/faces"), e.g. elena.safetensors
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