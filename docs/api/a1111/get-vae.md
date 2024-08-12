# Get VAE

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/sd-vae"
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
  "executionTime": 336,
  "id": "sync-33f33e48-6814-497f-85ba-bb1e26f9d248",
  "output": [
    {
      "filename": "/runpod-volume/stable-diffusion-webui/models/VAE/vae-ft-mse-840000-ema-pruned.safetensors",
      "model_name": "vae-ft-mse-840000-ema-pruned.safetensors"
    }
  ],
  "status": "COMPLETED"
}
```