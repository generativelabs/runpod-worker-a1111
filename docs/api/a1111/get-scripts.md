# Get Scripts

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/scripts"
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
  "delayTime": 92,
  "executionTime": 359,
  "id": "sync-886be7f0-fe75-4c21-9178-dd924f679c67",
  "output": {
    "img2img": [],
    "txt2img": []
  },
  "status": "COMPLETED"
}
```