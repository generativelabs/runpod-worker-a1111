# Get Embeddings

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/embeddings"
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
  "delayTime": 62181,
  "executionTime": 347,
  "id": "sync-d1678b5f-210f-4aee-844d-7ace54432661",
  "output": {
    "loaded": {},
    "skipped": {}
  },
  "status": "COMPLETED"
}
```