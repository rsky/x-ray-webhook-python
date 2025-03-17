# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import api_data_send_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.api_data_send_response import APIDataSendResponse

__all__ = ["APIDataResource", "AsyncAPIDataResource"]


class APIDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-ray-webhook-python#accessing-raw-response-data-eg-headers
        """
        return APIDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-ray-webhook-python#with_streaming_response
        """
        return APIDataResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        member_id: float,
        request: api_data_send_params.Request,
        response: api_data_send_params.Response,
        log: api_data_send_params.Log | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDataSendResponse:
        """
        Receive KanColle API request and response

        Args:
          member_id: Member ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api_data",
            body=maybe_transform(
                {
                    "member_id": member_id,
                    "request": request,
                    "response": response,
                    "log": log,
                },
                api_data_send_params.APIDataSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDataSendResponse,
        )


class AsyncAPIDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/x-ray-webhook-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/x-ray-webhook-python#with_streaming_response
        """
        return AsyncAPIDataResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        member_id: float,
        request: api_data_send_params.Request,
        response: api_data_send_params.Response,
        log: api_data_send_params.Log | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIDataSendResponse:
        """
        Receive KanColle API request and response

        Args:
          member_id: Member ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api_data",
            body=await async_maybe_transform(
                {
                    "member_id": member_id,
                    "request": request,
                    "response": response,
                    "log": log,
                },
                api_data_send_params.APIDataSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIDataSendResponse,
        )


class APIDataResourceWithRawResponse:
    def __init__(self, api_data: APIDataResource) -> None:
        self._api_data = api_data

        self.send = to_raw_response_wrapper(
            api_data.send,
        )


class AsyncAPIDataResourceWithRawResponse:
    def __init__(self, api_data: AsyncAPIDataResource) -> None:
        self._api_data = api_data

        self.send = async_to_raw_response_wrapper(
            api_data.send,
        )


class APIDataResourceWithStreamingResponse:
    def __init__(self, api_data: APIDataResource) -> None:
        self._api_data = api_data

        self.send = to_streamed_response_wrapper(
            api_data.send,
        )


class AsyncAPIDataResourceWithStreamingResponse:
    def __init__(self, api_data: AsyncAPIDataResource) -> None:
        self._api_data = api_data

        self.send = async_to_streamed_response_wrapper(
            api_data.send,
        )
