#!/usr/bin/env python3

import json
import yaml

FILENAME = "inventory.yaml"

with open(FILENAME) as f:
    content = yaml.safe_load(f)

print(json.dumps(content))
