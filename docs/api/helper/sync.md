# Huggingface Sync

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/v1/sync"
    },
    "payload": {
      "hf_token": "hf_xxxxxxxxxxxxxxxxxxxxxx",
      "repo_id": "ashleykleynhans/a1111",
      "sync_path": "/workspace/stable-diffusion-webui/models"
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
  "delayTime": 1176,
  "executionTime": 3037,
  "id": "sync-04f1f343-bef6-49a2-9d0c-97be633a82c8-e1",
  "output": {
    "synced_count": 1,
    "synced_files": [
      "/workspace/stable-diffusion-webui/models/ControlNet/ip-adapter_xl.pth"
    ]
  },
  "status": "COMPLETED"
}
```