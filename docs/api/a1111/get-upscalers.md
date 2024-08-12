# Get Upscalers

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/upscalers"
    },
    "payload": {}
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
  "delayTime": 90,
  "executionTime": 344,
  "id": "sync-fd580c71-0f25-4f1b-9188-9f3e8450ae83",
  "output": [
    {
      "model_name": null,
      "model_path": null,
      "model_url": null,
      "name": "None",
      "scale": 4
    },
    {
      "model_name": null,
      "model_path": null,
      "model_url": null,
      "name": "Lanczos",
      "scale": 4
    },
    {
      "model_name": null,
      "model_path": null,
      "model_url": null,
      "name": "Nearest",
      "scale": 4
    },
    {
      "model_name": "ESRGAN_4x",
      "model_path": "https://github.com/cszn/KAIR/releases/download/v1.0/ESRGAN.pth",
      "model_url": null,
      "name": "ESRGAN_4x",
      "scale": 4
    },
    {
      "model_name": null,
      "model_path": null,
      "model_url": null,
      "name": "LDSR",
      "scale": 4
    },
    {
      "model_name": null,
      "model_path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth",
      "model_url": null,
      "name": "R-ESRGAN 4x+",
      "scale": 4
    },
    {
      "model_name": null,
      "model_path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth",
      "model_url": null,
      "name": "R-ESRGAN 4x+ Anime6B",
      "scale": 4
    },
    {
      "model_name": "ScuNET GAN",
      "model_path": "https://github.com/cszn/KAIR/releases/download/v1.0/scunet_color_real_gan.pth",
      "model_url": null,
      "name": "ScuNET GAN",
      "scale": 4
    },
    {
      "model_name": "ScuNET GAN",
      "model_path": "https://github.com/cszn/KAIR/releases/download/v1.0/scunet_color_real_psnr.pth",
      "model_url": null,
      "name": "ScuNET PSNR",
      "scale": 4
    },
    {
      "model_name": "SwinIR 4x",
      "model_path": "https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/003_realSR_BSRGAN_DFOWMFC_s64w8_SwinIR-L_x4_GAN.pth",
      "model_url": null,
      "name": "SwinIR 4x",
      "scale": 4
    }
  ],
  "status": "COMPLETED"
}
```