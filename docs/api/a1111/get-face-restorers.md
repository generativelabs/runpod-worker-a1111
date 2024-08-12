# Get Face Restorers

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/face-restorers"
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
  "delayTime": 1177,
  "executionTime": 349,
  "id": "sync-4cd071c7-924a-4b2b-a4ca-4b6292cf93f0",
  "output": [
    {
      "cmd_dir": "/runpod-volume/stable-diffusion-webui/models/Codeformer",
      "name": "CodeFormer"
    },
    {
      "cmd_dir": null,
      "name": "GFPGAN"
    }
  ],
  "status": "COMPLETED"
}
```