import re
import time


def get_today() -> str:
    return time.strftime("%Y-%m-%d")


def camel_to_snake(name: str) -> str:
    return re.sub(
        r"([a-z0-9])([A-Z])", r"\1_\2", re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    ).lower()
