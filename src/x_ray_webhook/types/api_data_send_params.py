# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["APIDataSendParams", "Request", "Response", "Log"]


class APIDataSendParams(TypedDict, total=False):
    member_id: Required[int]
    """Member ID"""

    request: Required[Request]

    response: Required[Response]

    log: Log


class Request(TypedDict, total=False):
    parameters: Required[Dict[str, str]]
    """Request parameters"""

    url: Required[str]
    """Request URL"""


class Response(TypedDict, total=False):
    data: Required[Union[Dict[str, Optional[object]], Iterable[Dict[str, Optional[object]]], None]]
    """api_data"""

    timestamp: Required[int]
    """The UNIX timestamp (in milliseconds) when the response was received."""


class Log(TypedDict, total=False):
    bucket: Required[str]
    """S3 bucket name"""

    key: Required[str]
    """S3 object key"""
