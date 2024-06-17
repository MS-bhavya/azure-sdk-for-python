# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, Type, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._routes_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_endpoint_request,
    build_update_request,
)
from .._vendor import CdnManagementClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class RoutesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.cdn.aio.CdnManagementClient`'s
        :attr:`routes` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_endpoint(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.Route"]:
        """Lists all of the existing origins within a profile.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :return: An iterator like instance of either Route or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.RouteListResult] = kwargs.pop("cls", None)

        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_endpoint_request(
                    resource_group_name=resource_group_name,
                    profile_name=profile_name,
                    endpoint_name=endpoint_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("RouteListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, route_name: str, **kwargs: Any
    ) -> _models.Route:
        """Gets an existing route with the specified route name under the specified subscription, resource
        group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :return: Route or the result of cls(response)
        :rtype: ~azure.mgmt.cdn.models.Route
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.Route] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            route_name=route_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Route", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_initial(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route: Union[_models.Route, IO[bytes]],
        **kwargs: Any
    ) -> _models.Route:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Route] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(route, (IOBase, bytes)):
            _content = route
        else:
            _json = self._serialize.body(route, "Route")

        _request = build_create_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            route_name=route_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("Route", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("Route", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

            deserialized = self._deserialize("Route", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route: _models.Route,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Creates a new route with the specified route name under the specified subscription, resource
        group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route: Route properties. Required.
        :type route: ~azure.mgmt.cdn.models.Route
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Creates a new route with the specified route name under the specified subscription, resource
        group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route: Route properties. Required.
        :type route: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route: Union[_models.Route, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Creates a new route with the specified route name under the specified subscription, resource
        group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route: Route properties. Is either a Route type or a IO[bytes] type. Required.
        :type route: ~azure.mgmt.cdn.models.Route or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Route] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_initial(
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                route_name=route_name,
                route=route,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Route", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Route].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Route](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _update_initial(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route_update_properties: Union[_models.RouteUpdateParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.Route:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Route] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(route_update_properties, (IOBase, bytes)):
            _content = route_update_properties
        else:
            _json = self._serialize.body(route_update_properties, "RouteUpdateParameters")

        _request = build_update_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            route_name=route_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("Route", pipeline_response)

        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

            deserialized = self._deserialize("Route", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route_update_properties: _models.RouteUpdateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Updates an existing route with the specified route name under the specified subscription,
        resource group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route_update_properties: Route update properties. Required.
        :type route_update_properties: ~azure.mgmt.cdn.models.RouteUpdateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route_update_properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Updates an existing route with the specified route name under the specified subscription,
        resource group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route_update_properties: Route update properties. Required.
        :type route_update_properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        profile_name: str,
        endpoint_name: str,
        route_name: str,
        route_update_properties: Union[_models.RouteUpdateParameters, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.Route]:
        """Updates an existing route with the specified route name under the specified subscription,
        resource group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :param route_update_properties: Route update properties. Is either a RouteUpdateParameters type
         or a IO[bytes] type. Required.
        :type route_update_properties: ~azure.mgmt.cdn.models.RouteUpdateParameters or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either Route or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[~azure.mgmt.cdn.models.Route]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Route] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._update_initial(
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                route_name=route_name,
                route_update_properties=route_update_properties,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("Route", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.Route].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.Route](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, profile_name: str, endpoint_name: str, route_name: str, **kwargs: Any
    ) -> None:
        error_map: MutableMapping[int, Type[HttpResponseError]] = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            profile_name=profile_name,
            endpoint_name=endpoint_name,
            route_name=route_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.AfdErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["location"] = self._deserialize("str", response.headers.get("location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, profile_name: str, endpoint_name: str, route_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes an existing route with the specified route name under the specified subscription,
        resource group, profile, and AzureFrontDoor endpoint.

        :param resource_group_name: Name of the Resource group within the Azure subscription. Required.
        :type resource_group_name: str
        :param profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile
         which is unique within the resource group. Required.
        :type profile_name: str
        :param endpoint_name: Name of the endpoint under the profile which is unique globally.
         Required.
        :type endpoint_name: str
        :param route_name: Name of the routing rule. Required.
        :type route_name: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                profile_name=profile_name,
                endpoint_name=endpoint_name,
                route_name=route_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod,
                AsyncARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs),
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore
