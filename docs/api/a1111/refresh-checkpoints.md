# Refresh Checkpoints

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/refresh-checkpoints"
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
  "delayTime": 1226,
  "executionTime": 374,
  "id": "sync-f97be427-1209-4812-a683-ba65f722b376",
  "status": "COMPLETED"
}
```