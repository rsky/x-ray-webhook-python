# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from x_ray_webhook import XRayReceiver, AsyncXRayReceiver
from x_ray_webhook.types import APIDataCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: XRayReceiver) -> None:
        api_data = client.api_data.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        )
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: XRayReceiver) -> None:
        api_data = client.api_data.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
            log={
                "bucket": "x-ray-log",
                "key": "sortie_log/2025/02/22/222222_222222_kcsapi_api_req_sortie_battle.json.br",
            },
        )
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: XRayReceiver) -> None:
        response = client.api_data.with_raw_response.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_data = response.parse()
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: XRayReceiver) -> None:
        with client.api_data.with_streaming_response.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_data = response.parse()
            assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAPIData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncXRayReceiver) -> None:
        api_data = await async_client.api_data.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        )
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncXRayReceiver) -> None:
        api_data = await async_client.api_data.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
            log={
                "bucket": "x-ray-log",
                "key": "sortie_log/2025/02/22/222222_222222_kcsapi_api_req_sortie_battle.json.br",
            },
        )
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncXRayReceiver) -> None:
        response = await async_client.api_data.with_raw_response.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_data = await response.parse()
        assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncXRayReceiver) -> None:
        async with async_client.api_data.with_streaming_response.create(
            member_id=123456789,
            request={
                "method": "GET",
                "parameters": {
                    "key1": "bar",
                    "key2": "bar",
                },
                "url": "http://w01y.kancolle-server.com/kcsapi/api_get_member/basic",
            },
            response={
                "data": {
                    "member_id": "bar",
                    "nickname": "bar",
                },
                "timestamp": 1740262942,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_data = await response.parse()
            assert_matches_type(APIDataCreateResponse, api_data, path=["response"])

        assert cast(Any, response.is_closed) is True
