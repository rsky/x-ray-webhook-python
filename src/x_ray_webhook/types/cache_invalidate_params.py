# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CacheInvalidateParams"]


class CacheInvalidateParams(TypedDict, total=False):
    key: Required[str]
    """Resource key to invalidate"""

    timestamp: Required[float]
    """The UNIX timestamp (in milliseconds) when the new resource was received."""
