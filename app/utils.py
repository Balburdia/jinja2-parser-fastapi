"""Utility methods to help with data validation."""
import json
from typing import Dict

import yaml


def validate_json(s: str) -> Dict:
    """Load and validate a JSON-formatted string.

    :param s: JSON-formatted string.
    :return: dictionary representation of the JSON input.
    """
    try:
        values = json.loads(s)
    except ValueError as e:
        raise ValueError(f"Value error in JSON: {e}") from e

    return values


def validate_yaml(s: str) -> Dict:
    """Load and validate a YAML-formatted string.

    :param s: YAML-formatted string.
    :return: dictionary representation of the YAML input.
    """
    try:
        values = yaml.safe_load(s)
    except (ValueError, yaml.YAMLError, TypeError) as e:
        raise ValueError(f"Value error in YAML: {e}") from e

    return values
