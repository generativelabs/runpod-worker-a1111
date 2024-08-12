# File Download

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/v1/download"
    },
    "payload": {
      "source_url": "https://huggingface.co/ashleykleynhans/upscalers/resolve/main/4x-UltraSharp.pth",
      "download_path": "/workspace/stable-diffusion-webui/models/ESRGAN/4x-UltraSharp.pth"
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
  "delayTime": 1176,
  "executionTime": 3037,
  "id": "sync-04f1f343-bef6-49a2-9d0c-97be633a82c8-e1",
  "output": {
    "download_path": "/workspace/stable-diffusion-webui/models/ESRGAN/4x-UltraSharp.pth",
    "msg": "Download successful",
    "source_url": "https://huggingface.co/ashleykleynhans/upscalers/resolve/main/4x-UltraSharp.pth"
  },
  "status": "COMPLETED"
}
```