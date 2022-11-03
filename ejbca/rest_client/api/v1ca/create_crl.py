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
from ...models.create_crl_rest_response import CreateCrlRestResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    issuer_dn: str,
    *,
    client: Client,
    deltacrl: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/v1/ca/{issuer_dn}/createcrl".format(client.base_url, issuer_dn=issuer_dn)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["deltacrl"] = deltacrl

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CreateCrlRestResponse]:
    if response.status_code == 200:
        response_200 = CreateCrlRestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CreateCrlRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    issuer_dn: str,
    *,
    client: Client,
    deltacrl: Union[Unset, None, bool] = False,
) -> Response[CreateCrlRestResponse]:
    """Create CRL(main, partition and delta) issued by this CA

    Args:
        issuer_dn (str):
        deltacrl (Union[Unset, None, bool]):

    Returns:
        Response[CreateCrlRestResponse]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        client=client,
        deltacrl=deltacrl,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    issuer_dn: str,
    *,
    client: Client,
    deltacrl: Union[Unset, None, bool] = False,
) -> Optional[CreateCrlRestResponse]:
    """Create CRL(main, partition and delta) issued by this CA

    Args:
        issuer_dn (str):
        deltacrl (Union[Unset, None, bool]):

    Returns:
        Response[CreateCrlRestResponse]
    """

    return sync_detailed(
        issuer_dn=issuer_dn,
        client=client,
        deltacrl=deltacrl,
    ).parsed


async def asyncio_detailed(
    issuer_dn: str,
    *,
    client: Client,
    deltacrl: Union[Unset, None, bool] = False,
) -> Response[CreateCrlRestResponse]:
    """Create CRL(main, partition and delta) issued by this CA

    Args:
        issuer_dn (str):
        deltacrl (Union[Unset, None, bool]):

    Returns:
        Response[CreateCrlRestResponse]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        client=client,
        deltacrl=deltacrl,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    issuer_dn: str,
    *,
    client: Client,
    deltacrl: Union[Unset, None, bool] = False,
) -> Optional[CreateCrlRestResponse]:
    """Create CRL(main, partition and delta) issued by this CA

    Args:
        issuer_dn (str):
        deltacrl (Union[Unset, None, bool]):

    Returns:
        Response[CreateCrlRestResponse]
    """

    return (
        await asyncio_detailed(
            issuer_dn=issuer_dn,
            client=client,
            deltacrl=deltacrl,
        )
    ).parsed
