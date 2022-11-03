# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.rest_resource_status_rest_response import RestResourceStatusRestResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/ca_management/status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RestResourceStatusRestResponse]:
    if response.status_code == 200:
        response_200 = RestResourceStatusRestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RestResourceStatusRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[RestResourceStatusRestResponse]:
    """Get the status of this REST Resource

     Returns status, API version and EJBCA version.

    Returns:
        Response[RestResourceStatusRestResponse]
    """

    kwargs = _get_kwargs(
        client=client,
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
) -> Optional[RestResourceStatusRestResponse]:
    """Get the status of this REST Resource

     Returns status, API version and EJBCA version.

    Returns:
        Response[RestResourceStatusRestResponse]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[RestResourceStatusRestResponse]:
    """Get the status of this REST Resource

     Returns status, API version and EJBCA version.

    Returns:
        Response[RestResourceStatusRestResponse]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[RestResourceStatusRestResponse]:
    """Get the status of this REST Resource

     Returns status, API version and EJBCA version.

    Returns:
        Response[RestResourceStatusRestResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
