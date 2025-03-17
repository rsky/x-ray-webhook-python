# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["APIDataCreateParams", "Request", "Response", "Log"]


class APIDataCreateParams(TypedDict, total=False):
    member_id: Required[float]
    """Member ID"""

    request: Required[Request]

    response: Required[Response]

    log: Log


class Request(TypedDict, total=False):
    method: Required[Literal["GET", "POST"]]
    """Request method"""

    parameters: Required[Dict[str, Optional[object]]]
    """Request parameters"""

    url: Required[str]
    """Request URL"""


class Response(TypedDict, total=False):
    data: Required[Union[Dict[str, Optional[object]], Iterable[Dict[str, Optional[object]]], None]]
    """api_data"""

    timestamp: Required[float]
    """The UNIX timestamp (in seconds) when the response was received."""


class Log(TypedDict, total=False):
    bucket: Required[str]
    """S3 bucket name"""

    key: Required[str]
    """S3 object key"""
