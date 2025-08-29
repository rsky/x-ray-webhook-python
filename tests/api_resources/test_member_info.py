# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_ray_webhook import XRayWebhook, AsyncXRayWebhook
from x_ray_webhook.types import MemberInfoSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberInfo:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: XRayWebhook) -> None:
        member_info = client.member_info.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        )
        assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: XRayWebhook) -> None:
        response = client.member_info.with_raw_response.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member_info = response.parse()
        assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: XRayWebhook) -> None:
        with client.member_info.with_streaming_response.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member_info = response.parse()
            assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemberInfo:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncXRayWebhook) -> None:
        member_info = await async_client.member_info.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        )
        assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncXRayWebhook) -> None:
        response = await async_client.member_info.with_raw_response.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        member_info = await response.parse()
        assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncXRayWebhook) -> None:
        async with async_client.member_info.with_streaming_response.send(
            host="w01y.kancolle-server.com",
            member_id=123456789,
            nickname="Admiral 56",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            member_info = await response.parse()
            assert_matches_type(MemberInfoSendResponse, member_info, path=["response"])

        assert cast(Any, response.is_closed) is True
