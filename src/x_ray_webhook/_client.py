# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import api_data, resource, member_info
    from .resources.api_data import APIDataResource, AsyncAPIDataResource
    from .resources.resource import ResourceResource, AsyncResourceResource
    from .resources.member_info import MemberInfoResource, AsyncMemberInfoResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "XRayWebhook",
    "AsyncXRayWebhook",
    "Client",
    "AsyncClient",
]


class XRayWebhook(SyncAPIClient):
    # client options
    client_id: str
    client_secret: str

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous XRayWebhook client instance."""
        self.client_id = client_id

        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("X_RAY_WEBHOOK_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8082/webhook"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def api_data(self) -> APIDataResource:
        from .resources.api_data import APIDataResource

        return APIDataResource(self)

    @cached_property
    def resource(self) -> ResourceResource:
        from .resources.resource import ResourceResource

        return ResourceResource(self)

    @cached_property
    def member_info(self) -> MemberInfoResource:
        from .resources.member_info import MemberInfoResource

        return MemberInfoResource(self)

    @cached_property
    def with_raw_response(self) -> XRayWebhookWithRawResponse:
        return XRayWebhookWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> XRayWebhookWithStreamedResponse:
        return XRayWebhookWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "Cf-Access-Client-Id": self.client_id,
            "Cf-Access-Client-Secret": self.client_secret,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncXRayWebhook(AsyncAPIClient):
    # client options
    client_id: str
    client_secret: str

    def __init__(
        self,
        *,
        client_id: str,
        client_secret: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncXRayWebhook client instance."""
        self.client_id = client_id

        self.client_secret = client_secret

        if base_url is None:
            base_url = os.environ.get("X_RAY_WEBHOOK_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost:8082/webhook"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def api_data(self) -> AsyncAPIDataResource:
        from .resources.api_data import AsyncAPIDataResource

        return AsyncAPIDataResource(self)

    @cached_property
    def resource(self) -> AsyncResourceResource:
        from .resources.resource import AsyncResourceResource

        return AsyncResourceResource(self)

    @cached_property
    def member_info(self) -> AsyncMemberInfoResource:
        from .resources.member_info import AsyncMemberInfoResource

        return AsyncMemberInfoResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncXRayWebhookWithRawResponse:
        return AsyncXRayWebhookWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncXRayWebhookWithStreamedResponse:
        return AsyncXRayWebhookWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "Cf-Access-Client-Id": self.client_id,
            "Cf-Access-Client-Secret": self.client_secret,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            client_id=client_id or self.client_id,
            client_secret=client_secret or self.client_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class XRayWebhookWithRawResponse:
    _client: XRayWebhook

    def __init__(self, client: XRayWebhook) -> None:
        self._client = client

    @cached_property
    def api_data(self) -> api_data.APIDataResourceWithRawResponse:
        from .resources.api_data import APIDataResourceWithRawResponse

        return APIDataResourceWithRawResponse(self._client.api_data)

    @cached_property
    def resource(self) -> resource.ResourceResourceWithRawResponse:
        from .resources.resource import ResourceResourceWithRawResponse

        return ResourceResourceWithRawResponse(self._client.resource)

    @cached_property
    def member_info(self) -> member_info.MemberInfoResourceWithRawResponse:
        from .resources.member_info import MemberInfoResourceWithRawResponse

        return MemberInfoResourceWithRawResponse(self._client.member_info)


class AsyncXRayWebhookWithRawResponse:
    _client: AsyncXRayWebhook

    def __init__(self, client: AsyncXRayWebhook) -> None:
        self._client = client

    @cached_property
    def api_data(self) -> api_data.AsyncAPIDataResourceWithRawResponse:
        from .resources.api_data import AsyncAPIDataResourceWithRawResponse

        return AsyncAPIDataResourceWithRawResponse(self._client.api_data)

    @cached_property
    def resource(self) -> resource.AsyncResourceResourceWithRawResponse:
        from .resources.resource import AsyncResourceResourceWithRawResponse

        return AsyncResourceResourceWithRawResponse(self._client.resource)

    @cached_property
    def member_info(self) -> member_info.AsyncMemberInfoResourceWithRawResponse:
        from .resources.member_info import AsyncMemberInfoResourceWithRawResponse

        return AsyncMemberInfoResourceWithRawResponse(self._client.member_info)


class XRayWebhookWithStreamedResponse:
    _client: XRayWebhook

    def __init__(self, client: XRayWebhook) -> None:
        self._client = client

    @cached_property
    def api_data(self) -> api_data.APIDataResourceWithStreamingResponse:
        from .resources.api_data import APIDataResourceWithStreamingResponse

        return APIDataResourceWithStreamingResponse(self._client.api_data)

    @cached_property
    def resource(self) -> resource.ResourceResourceWithStreamingResponse:
        from .resources.resource import ResourceResourceWithStreamingResponse

        return ResourceResourceWithStreamingResponse(self._client.resource)

    @cached_property
    def member_info(self) -> member_info.MemberInfoResourceWithStreamingResponse:
        from .resources.member_info import MemberInfoResourceWithStreamingResponse

        return MemberInfoResourceWithStreamingResponse(self._client.member_info)


class AsyncXRayWebhookWithStreamedResponse:
    _client: AsyncXRayWebhook

    def __init__(self, client: AsyncXRayWebhook) -> None:
        self._client = client

    @cached_property
    def api_data(self) -> api_data.AsyncAPIDataResourceWithStreamingResponse:
        from .resources.api_data import AsyncAPIDataResourceWithStreamingResponse

        return AsyncAPIDataResourceWithStreamingResponse(self._client.api_data)

    @cached_property
    def resource(self) -> resource.AsyncResourceResourceWithStreamingResponse:
        from .resources.resource import AsyncResourceResourceWithStreamingResponse

        return AsyncResourceResourceWithStreamingResponse(self._client.resource)

    @cached_property
    def member_info(self) -> member_info.AsyncMemberInfoResourceWithStreamingResponse:
        from .resources.member_info import AsyncMemberInfoResourceWithStreamingResponse

        return AsyncMemberInfoResourceWithStreamingResponse(self._client.member_info)


Client = XRayWebhook

AsyncClient = AsyncXRayWebhook
