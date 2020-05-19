import json
# dumps command
# converts python to json format

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)