# Get ControlNet Models

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/controlnet/model_list"
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
  "delayTime": 66695,
  "executionTime": 366,
  "id": "sync-13aa36bf-6686-46ed-bd0b-aed12ca5b0bd",
  "output": {
    "model_list": [
      "control_v11p_sd15_canny [d14c016b]",
      "control_v11p_sd15_lineart [43d4be0d]",
      "control_v11p_sd15_openpose [cab727d4]"
    ]
  },
  "status": "COMPLETED"
}
```