# Get Hypernetworks

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/hypernetworks"
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
  "delayTime": 1056,
  "executionTime": 333,
  "id": "sync-e7d63eff-dad6-4dc5-9327-34d21f200254",
  "output": [],
  "status": "COMPLETED"
}
```