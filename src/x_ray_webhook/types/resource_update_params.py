# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ResourceUpdateParams"]


class ResourceUpdateParams(TypedDict, total=False):
    key: Required[str]
    """Key of the updated resource"""

    timestamp: Required[int]
    """The UNIX timestamp (in milliseconds) when the new resource was received"""
