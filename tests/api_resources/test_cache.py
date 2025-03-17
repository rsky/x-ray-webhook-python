# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_ray_webhook import XRayReceiver, AsyncXRayReceiver
from x_ray_webhook.types import CacheInvalidateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCache:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_invalidate(self, client: XRayReceiver) -> None:
        cache = client.cache.invalidate(
            key="assets/ships/0001/full.webp",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_invalidate(self, client: XRayReceiver) -> None:
        response = client.cache.with_raw_response.invalidate(
            key="assets/ships/0001/full.webp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = response.parse()
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_invalidate(self, client: XRayReceiver) -> None:
        with client.cache.with_streaming_response.invalidate(
            key="assets/ships/0001/full.webp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = response.parse()
            assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCache:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_invalidate(self, async_client: AsyncXRayReceiver) -> None:
        cache = await async_client.cache.invalidate(
            key="assets/ships/0001/full.webp",
        )
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_invalidate(self, async_client: AsyncXRayReceiver) -> None:
        response = await async_client.cache.with_raw_response.invalidate(
            key="assets/ships/0001/full.webp",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cache = await response.parse()
        assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_invalidate(self, async_client: AsyncXRayReceiver) -> None:
        async with async_client.cache.with_streaming_response.invalidate(
            key="assets/ships/0001/full.webp",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cache = await response.parse()
            assert_matches_type(CacheInvalidateResponse, cache, path=["response"])

        assert cast(Any, response.is_closed) is True
