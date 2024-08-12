# Get Script Info

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/script-info"
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
  "delayTime": 1152,
  "executionTime": 350,
  "id": "sync-a4dbea02-2210-4bda-a436-53a6ec5bdc0a",
  "output": [],
  "status": "COMPLETED"
}
```