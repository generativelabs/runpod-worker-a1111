# Get Memory

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/memory"
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
  "delayTime": 1076,
  "executionTime": 339,
  "id": "sync-4930ae5f-aaa6-4310-93b4-44e8a8e82371",
  "output": {
    "cuda": {
      "active": {
        "current": 2170419200,
        "peak": 2170419200
      },
      "allocated": {
        "current": 2170419200,
        "peak": 2170419200
      },
      "events": {
        "oom": 0,
        "retries": 0
      },
      "inactive": {
        "current": 44173312,
        "peak": 56532480
      },
      "reserved": {
        "current": 2214592512,
        "peak": 2214592512
      },
      "system": {
        "free": 22676176896,
        "total": 25393692672,
        "used": 2717515776
      }
    },
    "ram": {
      "free": 265675436032,
      "total": 270193479680,
      "used": 4518043648
    }
  },
  "status": "COMPLETED"
}
```