TXT2IMG_SCHEMA = {
    'prompt': {
        'type': str,
        'required': True
    },
    'negative_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'styles': {
        'type': list,
        'required': False,
        'default': []
    },
    'seed': {
        'type': int,
        'required': False,
        'default': -1
    },
    'subseed': {
        'type': int,
        'required': False,
        'default': -1
    },
    'subseed_strength': {
        'type': int,
        'required': False,
        'default': 0
    },
    'seed_resize_from_h': {
        'type': int,
        'required': False,
        'default': -1
    },
    'seed_resize_from_w': {
        'type': int,
        'required': False,
        'default': -1
    },
    'sampler_name': {
        'type': str,
        'required': False,
        'default': 'Euler a',
        'constraints': lambda sampler_name: sampler_name in [
            'DPM++ 2M',
            'DPM++ SDE',
            'DPM++ 2M SDE',
            'DPM++ 2M SDE Heun',
            'DPM++ 2S a',
            'DPM++ 3M SDE',
            'Euler a',
            'Euler',
            'LMS',
            'Heun',
            'DPM2',
            'DPM2 a',
            'DPM fast',
            'DPM adaptive',
            'Restart',
            'DDIM',
            'PLMS',
            'UniPC',
            'LCM'
        ]
    },
    'scheduler': {
        'type': str,
        'required': False,
        'default': 'Euler a',
        'constraints': lambda scheduler: scheduler in [
            'automatic',
            'uniform',
            'karras',
            'exponential',
            'polyexponential',
            'sgm_uniform'
        ]
    },
    'batch_size': {
        'type': int,
        'required': False,
        'default': 1
    },
    'n_iter': {
        'type': int,
        'required': False,
        'default': 1
    },
    'steps': {
        'type': int,
        'required': False,
        'default': 20
    },
    'cfg_scale': {
        'type': float,
        'required': False,
        'default': 7
    },
    'width': {
        'type': int,
        'required': False,
        'default': 512
    },
    'height': {
        'type': int,
        'required': False,
        'default': 512
    },
    'restore_faces': {
        'type': bool,
        'required': False,
        'default': False
    },
    'tiling': {
        'type': bool,
        'required': False,
        'default': False
    },
    'do_not_save_samples': {
        'type': bool,
        'required': False,
        'default': False
    },
    'do_not_save_grid': {
        'type': bool,
        'required': False,
        'default': False
    },
    'eta': {
        'type': int,
        'required': False,
        'default': 0
    },
    'denoising_strength': {
        'type': float,
        'required': False,
        'default': 0
    },
    's_min_uncond': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_churn': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_tmax': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_tmin': {
        'type': int,
        'required': False,
        'default': 0
    },
    's_noise': {
        'type': int,
        'required': False,
        'default': 0
    },
    'override_settings': {
        'type': dict,
        'required': False,
        'default': {}
    },
    'override_settings_restore_afterwards': {
        'type': bool,
        'required': False,
        'default': True
    },
    'refiner_checkpoint': {
        'type': str,
        'required': False,
        'default': ''
    },
    'refiner_switch_at': {
        'type': float,
        'required': False,
        'default': 0
    },
    'disable_extra_networks': {
        'type': bool,
        'required': False,
        'default': False
    },
    'comments': {
        'type': dict,
        'required': False,
        'default': {}
    },
    'enable_hr': {
        'type': bool,
        'required': False,
        'default': False
    },
    'firstphase_width': {
        'type': int,
        'required': False,
        'default': 0
    },
    'firstphase_height': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_scale': {
        'type': float,
        'required': False,
        'default': 2
    },
    'hr_upscaler': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_second_pass_steps': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_resize_x': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_resize_y': {
        'type': int,
        'required': False,
        'default': 0
    },
    'hr_checkpoint_name': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_sampler_name': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'hr_negative_prompt': {
        'type': str,
        'required': False,
        'default': ''
    },
    'sampler_index': {
        'type': str,
        'required': False,
        'default': 'Euler a',
        'constraints': lambda sampler_index: sampler_index in [
            'DPM++ 2M',
            'DPM++ SDE',
            'DPM++ 2M SDE',
            'DPM++ 2M SDE Heun',
            'DPM++ 2S a',
            'DPM++ 3M SDE',
            'Euler a',
            'Euler',
            'LMS',
            'Heun',
            'DPM2',
            'DPM2 a',
            'DPM fast',
            'DPM adaptive',
            'Restart',
            'DDIM',
            'PLMS',
            'UniPC',
            'LCM'
        ]
    },
    'script_name': {
        'type': str,
        'required': False,
        'default': ''
    },
    'script_args': {
        'type': list,
        'required': False,
        'default': []
    },
    'send_images': {
        'type': bool,
        'required': False,
        'default': True
    },
    'save_images': {
        'type': bool,
        'required': False,
        'default': False
    },
    'alwayson_scripts': {
        'type': dict,
        'required': False,
        'default': {}
    }
}
