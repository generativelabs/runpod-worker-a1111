#!/usr/bin/env python3
import json
from util import purge_queue


if __name__ == '__main__':
    r = purge_queue()

    print(r.status_code)
    print(json.dumps(r.json(), indent=4, default=str))
