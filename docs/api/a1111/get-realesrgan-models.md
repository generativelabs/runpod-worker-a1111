# Get Real-ESRGAN Models

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/realesrgan-models"
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
  "delayTime": 89,
  "executionTime": 343,
  "id": "sync-b0d703b0-7e2e-4184-b6ab-60f564653c3b",
  "output": [
    {
      "name": "R-ESRGAN General 4xV3",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth",
      "scale": 4
    },
    {
      "name": "R-ESRGAN General WDN 4xV3",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-wdn-x4v3.pth",
      "scale": 4
    },
    {
      "name": "R-ESRGAN AnimeVideo",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-animevideov3.pth",
      "scale": 4
    },
    {
      "name": "R-ESRGAN 4x+",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth",
      "scale": 4
    },
    {
      "name": "R-ESRGAN 4x+ Anime6B",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth",
      "scale": 4
    },
    {
      "name": "R-ESRGAN 2x+",
      "path": "https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth",
      "scale": 2
    }
  ],
  "status": "COMPLETED"
}
```