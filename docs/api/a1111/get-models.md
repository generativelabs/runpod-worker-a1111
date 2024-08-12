# Get Models

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/sd-models"
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
  "executionTime": 337,
  "id": "sync-05d5edb3-6161-4a3f-97db-662a7dbd51fb",
  "output": [
    {
      "config": null,
      "filename": "/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/deliberate_v2.safetensors",
      "hash": null,
      "model_name": "deliberate_v2",
      "sha256": null,
      "title": "deliberate_v2.safetensors"
    },
    {
      "config": null,
      "filename": "/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/disneyPixarCartoon_v10.safetensors",
      "hash": null,
      "model_name": "disneyPixarCartoon_v10",
      "sha256": null,
      "title": "disneyPixarCartoon_v10.safetensors"
    },
    {
      "config": null,
      "filename": "/runpod-volume/stable-diffusion-webui/models/Stable-diffusion/pixarStyleModel_v10.safetensors",
      "hash": null,
      "model_name": "pixarStyleModel_v10",
      "sha256": null,
      "title": "pixarStyleModel_v10.safetensors"
    }
  ],
  "status": "COMPLETED"
}
```