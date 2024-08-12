# Get Extensions

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/extensions"
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
  "delayTime": 995,
  "executionTime": 116,
  "id": "sync-c40a46b1-3b53-4d44-8499-b70ed55c64db-e1",
  "output": [
    {
      "branch": "main",
      "commit_date": "1713351463",
      "commit_hash": "1edd58886014a8fdea73cfcc30dfac84f4684926",
      "enabled": true,
      "name": "adetailer",
      "remote": "https://github.com/Bing-su/adetailer.git",
      "version": "1edd5888"
    },
    {
      "branch": "main",
      "commit_date": "1713732680",
      "commit_hash": "b4b5bfefb0d29d23f6b308f6369c4a989e74b112",
      "enabled": true,
      "name": "sd-webui-controlnet",
      "remote": "https://github.com/Mikubill/sd-webui-controlnet.git",
      "version": "b4b5bfef"
    },
    {
      "branch": "main",
      "commit_date": "1713501132",
      "commit_hash": "d2e78be2b3c1bbd01dd62c76d58b23ccb4a27022",
      "enabled": true,
      "name": "sd-webui-reactor",
      "remote": "https://github.com/Gourieff/sd-webui-reactor.git",
      "version": "d2e78be2"
    }
  ],
  "status": "COMPLETED"
}
```