# Get Latent Upscale Modes

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/latent-upscale-modes"
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
  "delayTime": 102,
  "executionTime": 50,
  "id": "sync-3af73110-258d-4c61-b74a-59e5dea03a31-e1",
  "output": [
    {
      "name": "Latent"
    },
    {
      "name": "Latent (antialiased)"
    },
    {
      "name": "Latent (bicubic)"
    },
    {
      "name": "Latent (bicubic antialiased)"
    },
    {
      "name": "Latent (nearest)"
    },
    {
      "name": "Latent (nearest-exact)"
    }
  ],
  "status": "COMPLETED"
}
```