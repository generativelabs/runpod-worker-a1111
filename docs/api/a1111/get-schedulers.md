# Get Schedulers

## Request

```json
{
  "input": {
    "api": {
      "method": "GET",
      "endpoint": "/sdapi/v1/schedulers"
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
  "delayTime": 94818,
  "executionTime": 75,
  "id": "sync-05e0174a-68f8-450c-ac07-85a8199f659e-e1",
  "output": [
    {
      "aliases": null,
      "default_rho": -1,
      "label": "Automatic",
      "name": "automatic",
      "need_inner_model": false
    },
    {
      "aliases": null,
      "default_rho": -1,
      "label": "Uniform",
      "name": "uniform",
      "need_inner_model": true
    },
    {
      "aliases": null,
      "default_rho": 7,
      "label": "Karras",
      "name": "karras",
      "need_inner_model": false
    },
    {
      "aliases": null,
      "default_rho": -1,
      "label": "Exponential",
      "name": "exponential",
      "need_inner_model": false
    },
    {
      "aliases": null,
      "default_rho": 1,
      "label": "Polyexponential",
      "name": "polyexponential",
      "need_inner_model": false
    },
    {
      "aliases": [
        "SGMUniform"
      ],
      "default_rho": -1,
      "label": "SGM Uniform",
      "name": "sgm_uniform",
      "need_inner_model": true
    }
  ],
  "status": "COMPLETED"
}
```