# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.expiring_certificates_rest_response import ExpiringCertificatesRestResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    days: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    max_number_of_results: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/certificate/expire".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["days"] = days

    params["offset"] = offset

    params["maxNumberOfResults"] = max_number_of_results

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ExpiringCertificatesRestResponse]:
    if response.status_code == 200:
        response_200 = ExpiringCertificatesRestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ExpiringCertificatesRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    days: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    max_number_of_results: Union[Unset, None, int] = UNSET,
) -> Response[ExpiringCertificatesRestResponse]:
    """Get a list of certificates that are about to expire

     List of certificates expiring within specified number of days

    Args:
        days (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        max_number_of_results (Union[Unset, None, int]):

    Returns:
        Response[ExpiringCertificatesRestResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        days=days,
        offset=offset,
        max_number_of_results=max_number_of_results,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    days: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    max_number_of_results: Union[Unset, None, int] = UNSET,
) -> Optional[ExpiringCertificatesRestResponse]:
    """Get a list of certificates that are about to expire

     List of certificates expiring within specified number of days

    Args:
        days (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        max_number_of_results (Union[Unset, None, int]):

    Returns:
        Response[ExpiringCertificatesRestResponse]
    """

    return sync_detailed(
        client=client,
        days=days,
        offset=offset,
        max_number_of_results=max_number_of_results,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    days: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    max_number_of_results: Union[Unset, None, int] = UNSET,
) -> Response[ExpiringCertificatesRestResponse]:
    """Get a list of certificates that are about to expire

     List of certificates expiring within specified number of days

    Args:
        days (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        max_number_of_results (Union[Unset, None, int]):

    Returns:
        Response[ExpiringCertificatesRestResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        days=days,
        offset=offset,
        max_number_of_results=max_number_of_results,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    days: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    max_number_of_results: Union[Unset, None, int] = UNSET,
) -> Optional[ExpiringCertificatesRestResponse]:
    """Get a list of certificates that are about to expire

     List of certificates expiring within specified number of days

    Args:
        days (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        max_number_of_results (Union[Unset, None, int]):

    Returns:
        Response[ExpiringCertificatesRestResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            offset=offset,
            max_number_of_results=max_number_of_results,
        )
    ).parsed
