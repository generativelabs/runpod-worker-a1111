#!/usr/bin/env python3
import json
from util import cancel_task

JOB_ID = 'sync-a0d66cad-1f31-4782-8a36-b69dfd370e56-e1'


if __name__ == '__main__':
    r = cancel_task(JOB_ID)

    print(r.status_code)
    print(json.dumps(r.json(), indent=4, default=str))
