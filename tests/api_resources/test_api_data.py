# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_ray_webhook import XRayWebhook, AsyncXRayWebhook
from x_ray_webhook.types import APIDataSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: XRayWebhook) -> None:
        api_data = client.api_data.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        )
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: XRayWebhook) -> None:
        api_data = client.api_data.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
            log={
                "bucket": "x-ray-log",
                "key": "sortie_log/2025/02/22/222222_222222_kcsapi_api_req_sortie_battle.json.br",
            },
        )
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: XRayWebhook) -> None:
        response = client.api_data.with_raw_response.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_data = response.parse()
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: XRayWebhook) -> None:
        with client.api_data.with_streaming_response.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_data = response.parse()
            assert_matches_type(APIDataSendResponse, api_data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIData:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncXRayWebhook) -> None:
        api_data = await async_client.api_data.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        )
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncXRayWebhook) -> None:
        api_data = await async_client.api_data.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
            log={
                "bucket": "x-ray-log",
                "key": "sortie_log/2025/02/22/222222_222222_kcsapi_api_req_sortie_battle.json.br",
            },
        )
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncXRayWebhook) -> None:
        response = await async_client.api_data.with_raw_response.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_data = await response.parse()
        assert_matches_type(APIDataSendResponse, api_data, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncXRayWebhook) -> None:
        async with async_client.api_data.with_streaming_response.send(
            member_id=123456789,
            request={
                "parameters": {
                    "key1": "value1",
                    "key2": "value2",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942000,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_data = await response.parse()
            assert_matches_type(APIDataSendResponse, api_data, path=["response"])

        assert cast(Any, response.is_closed) is True
