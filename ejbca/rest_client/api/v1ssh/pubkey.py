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
from ...models.ssh_public_key_rest_response import SshPublicKeyRestResponse
from ...types import Response


def _get_kwargs(
    ca_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/ssh/{ca_name}/pubkey".format(client.base_url, ca_name=ca_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[SshPublicKeyRestResponse]:
    if response.status_code == 200:
        response_200 = SshPublicKeyRestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SshPublicKeyRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    ca_name: str,
    *,
    client: Client,
) -> Response[SshPublicKeyRestResponse]:
    """Retrieves a CA's public key in SSH format.

     Retrieves a CA's public key in SSH format.

    Args:
        ca_name (str):

    Returns:
        Response[SshPublicKeyRestResponse]
    """

    kwargs = _get_kwargs(
        ca_name=ca_name,
        client=client,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    ca_name: str,
    *,
    client: Client,
) -> Optional[SshPublicKeyRestResponse]:
    """Retrieves a CA's public key in SSH format.

     Retrieves a CA's public key in SSH format.

    Args:
        ca_name (str):

    Returns:
        Response[SshPublicKeyRestResponse]
    """

    return sync_detailed(
        ca_name=ca_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    ca_name: str,
    *,
    client: Client,
) -> Response[SshPublicKeyRestResponse]:
    """Retrieves a CA's public key in SSH format.

     Retrieves a CA's public key in SSH format.

    Args:
        ca_name (str):

    Returns:
        Response[SshPublicKeyRestResponse]
    """

    kwargs = _get_kwargs(
        ca_name=ca_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    ca_name: str,
    *,
    client: Client,
) -> Optional[SshPublicKeyRestResponse]:
    """Retrieves a CA's public key in SSH format.

     Retrieves a CA's public key in SSH format.

    Args:
        ca_name (str):

    Returns:
        Response[SshPublicKeyRestResponse]
    """

    return (
        await asyncio_detailed(
            ca_name=ca_name,
            client=client,
        )
    ).parsed
