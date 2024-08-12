API_SCHEMA = {
    'method': {
        'type': str,
        'required': True,
        'constraints': lambda method: method in [
            'GET',
            'POST'
        ]
    },
    'endpoint': {
        'type': str,
        'required': True,
        'constraints': lambda endpoint: endpoint in [
            'sdapi/v1/txt2img',
            'sdapi/v1/img2img',
            'sdapi/v1/interrogate',
            'sdapi/v1/options',
            'sdapi/v1/samplers',
            'sdapi/v1/schedulers',
            'sdapi/v1/upscalers',
            'sdapi/v1/latent-upscale-modes',
            'sdapi/v1/sd-models',
            'sdapi/v1/sd-vae',
            'sdapi/v1/hypernetworks',
            'sdapi/v1/face-restorers',
            'sdapi/v1/realesrgan-models',
            'sdapi/v1/prompt-styles',
            'sdapi/v1/embeddings',
            'sdapi/v1/refresh-embeddings',
            'sdapi/v1/refresh-checkpoints',
            'sdapi/v1/refresh-vae',
            'sdapi/v1/memory',
            'sdapi/v1/scripts',
            'sdapi/v1/script-info',
            'sdapi/v1/extensions',
            'sdapi/v1/loras',
            'sdapi/v1/refresh-loras',
            'controlnet/model_list',
            'v1/download',
            'v1/sync'
        ]
    }
}
