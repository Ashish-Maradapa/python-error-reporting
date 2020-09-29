# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from collections import OrderedDict
import functools
import re
from typing import Dict, Sequence, Tuple, Type, Union
import pkg_resources

import google.api_core.client_options as ClientOptions  # type: ignore
from google.api_core import exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.errorreporting_v1beta1.services.error_stats_service import pagers
from google.cloud.errorreporting_v1beta1.types import common
from google.cloud.errorreporting_v1beta1.types import error_stats_service

from .transports.base import ErrorStatsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ErrorStatsServiceGrpcAsyncIOTransport
from .client import ErrorStatsServiceClient


class ErrorStatsServiceAsyncClient:
    """An API for retrieving and managing error statistics as well
    as data for individual events.
    """

    _client: ErrorStatsServiceClient

    DEFAULT_ENDPOINT = ErrorStatsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ErrorStatsServiceClient.DEFAULT_MTLS_ENDPOINT

    from_service_account_file = ErrorStatsServiceClient.from_service_account_file
    from_service_account_json = from_service_account_file

    get_transport_class = functools.partial(
        type(ErrorStatsServiceClient).get_transport_class, type(ErrorStatsServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: credentials.Credentials = None,
        transport: Union[str, ErrorStatsServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiate the error stats service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ErrorStatsServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint, this is the default value for
                the environment variable) and "auto" (auto switch to the default
                mTLS endpoint if client SSL credentials is present). However,
                the ``api_endpoint`` property takes precedence if provided.
                (2) The ``client_cert_source`` property is used to provide client
                SSL credentials for mutual TLS transport. If not provided, the
                default SSL credentials will be used if present.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """

        self._client = ErrorStatsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_group_stats(
        self,
        request: error_stats_service.ListGroupStatsRequest = None,
        *,
        project_name: str = None,
        time_range: error_stats_service.QueryTimeRange = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListGroupStatsAsyncPager:
        r"""Lists the specified groups.

        Args:
            request (:class:`~.error_stats_service.ListGroupStatsRequest`):
                The request object. Specifies a set of `ErrorGroupStats`
                to return.
            project_name (:class:`str`):
                Required. The resource name of the
                Google Cloud Platform project. Written
                as <code>projects/</code> plus the <a
                href="https://support.google.com/cloud/answer/6158840">Google
                Cloud Platform project ID</a>.

                Example: <code>projects/my-
                project-123</code>.
                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            time_range (:class:`~.error_stats_service.QueryTimeRange`):
                Optional. List data for the given time range. If not
                set, a default time range is used. The field
                time_range_begin in the response will specify the
                beginning of this time range. Only ErrorGroupStats with
                a non-zero count in the given time range are returned,
                unless the request contains an explicit group_id list.
                If a group_id list is given, also ErrorGroupStats with
                zero occurrences are returned.
                This corresponds to the ``time_range`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListGroupStatsAsyncPager:
                Contains a set of requested error
                group stats.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([project_name, time_range]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = error_stats_service.ListGroupStatsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if project_name is not None:
            request.project_name = project_name
        if time_range is not None:
            request.time_range = time_range

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_group_stats,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListGroupStatsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_events(
        self,
        request: error_stats_service.ListEventsRequest = None,
        *,
        project_name: str = None,
        group_id: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEventsAsyncPager:
        r"""Lists the specified events.

        Args:
            request (:class:`~.error_stats_service.ListEventsRequest`):
                The request object. Specifies a set of error events to
                return.
            project_name (:class:`str`):
                Required. The resource name of the Google Cloud Platform
                project. Written as ``projects/`` plus the `Google Cloud
                Platform project
                ID <https://support.google.com/cloud/answer/6158840>`__.
                Example: ``projects/my-project-123``.
                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            group_id (:class:`str`):
                Required. The group for which events
                shall be returned.
                This corresponds to the ``group_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.pagers.ListEventsAsyncPager:
                Contains a set of requested error
                events.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([project_name, group_id]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = error_stats_service.ListEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if project_name is not None:
            request.project_name = project_name
        if group_id is not None:
            request.group_id = group_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_events,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEventsAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_events(
        self,
        request: error_stats_service.DeleteEventsRequest = None,
        *,
        project_name: str = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> error_stats_service.DeleteEventsResponse:
        r"""Deletes all error events of a given project.

        Args:
            request (:class:`~.error_stats_service.DeleteEventsRequest`):
                The request object. Deletes all events in the project.
            project_name (:class:`str`):
                Required. The resource name of the Google Cloud Platform
                project. Written as ``projects/`` plus the `Google Cloud
                Platform project
                ID <https://support.google.com/cloud/answer/6158840>`__.
                Example: ``projects/my-project-123``.
                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.

            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            ~.error_stats_service.DeleteEventsResponse:
                Response message for deleting error
                events.

        """
        # Create or coerce a protobuf request object.
        # Sanity check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        if request is not None and any([project_name]):
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = error_stats_service.DeleteEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.

        if project_name is not None:
            request.project_name = project_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_events,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-errorreporting",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("ErrorStatsServiceAsyncClient",)