# Refresh Embeddings

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/refresh-embeddings"
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
  "delayTime": 60060,
  "executionTime": 788,
  "id": "sync-7a18dee0-2191-4781-8ae2-6a5d07c8308e-e1",
  "status": "COMPLETED"
}
```