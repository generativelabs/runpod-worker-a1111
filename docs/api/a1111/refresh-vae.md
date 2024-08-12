# Refresh VAE

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/refresh-vae"
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
  "delayTime": 1343,
  "executionTime": 85,
  "id": "sync-f365e0bf-5804-479b-b3f0-1fb4ea1a7f6b-e1",
  "status": "COMPLETED"
}
```