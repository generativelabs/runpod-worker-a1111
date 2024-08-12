# Interrogate

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/sdapi/v1/interrogate"
    },
    "payload": {
      "image": "base64 encoded image content",
      "model": "deepdanbooru"
    }
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
  "delayTime": 41634,
  "executionTime": 8822,
  "id": "sync-cd686d39-f318-4f29-9f81-8837902a6cf9-e1",
  "output": {
    "caption": "1boy, bald, beard, black hair, face, facial hair, fat, glasses, indoors, male focus, mustache, old, old man, realistic, solo, wrinkled skin"
  },
  "status": "COMPLETED"
}
```