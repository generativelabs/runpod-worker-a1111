# Refresh Loras

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/refresh-loras"
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
  "delayTime": 1406,
  "executionTime": 345,
  "id": "sync-29d03cb7-7585-4fff-a484-4d35347edd4d",
  "status": "COMPLETED"
}
```