# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import member_info_send_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.member_info_send_response import MemberInfoSendResponse

__all__ = ["MemberInfoResource", "AsyncMemberInfoResource"]


class MemberInfoResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MemberInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsky/x-ray-webhook-python#accessing-raw-response-data-eg-headers
        """
        return MemberInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemberInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsky/x-ray-webhook-python#with_streaming_response
        """
        return MemberInfoResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        host: str,
        member_id: int,
        nickname: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberInfoSendResponse:
        """
        Updates member information

        Args:
          host: Naval district host name

          member_id: Member ID

          nickname: Member nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/member_info",
            body=maybe_transform(
                {
                    "host": host,
                    "member_id": member_id,
                    "nickname": nickname,
                },
                member_info_send_params.MemberInfoSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberInfoSendResponse,
        )


class AsyncMemberInfoResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMemberInfoResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsky/x-ray-webhook-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemberInfoResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemberInfoResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsky/x-ray-webhook-python#with_streaming_response
        """
        return AsyncMemberInfoResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        host: str,
        member_id: int,
        nickname: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemberInfoSendResponse:
        """
        Updates member information

        Args:
          host: Naval district host name

          member_id: Member ID

          nickname: Member nickname

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/member_info",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "member_id": member_id,
                    "nickname": nickname,
                },
                member_info_send_params.MemberInfoSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemberInfoSendResponse,
        )


class MemberInfoResourceWithRawResponse:
    def __init__(self, member_info: MemberInfoResource) -> None:
        self._member_info = member_info

        self.send = to_raw_response_wrapper(
            member_info.send,
        )


class AsyncMemberInfoResourceWithRawResponse:
    def __init__(self, member_info: AsyncMemberInfoResource) -> None:
        self._member_info = member_info

        self.send = async_to_raw_response_wrapper(
            member_info.send,
        )


class MemberInfoResourceWithStreamingResponse:
    def __init__(self, member_info: MemberInfoResource) -> None:
        self._member_info = member_info

        self.send = to_streamed_response_wrapper(
            member_info.send,
        )


class AsyncMemberInfoResourceWithStreamingResponse:
    def __init__(self, member_info: AsyncMemberInfoResource) -> None:
        self._member_info = member_info

        self.send = async_to_streamed_response_wrapper(
            member_info.send,
        )
