import boto3
from typing import Literal

_cache: dict = {}


def get_client(service_name: Literal['dynamodb'] = "dynamodb"):
    if service_name not in _cache:
        _cache[service_name] = boto3.client(service_name)

    return _cache[service_name]
