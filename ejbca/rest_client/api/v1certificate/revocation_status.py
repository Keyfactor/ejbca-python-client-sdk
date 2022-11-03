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
from ...models.revoke_status_rest_response import RevokeStatusRestResponse
from ...types import Response


def _get_kwargs(
    issuer_dn: str,
    certificate_serial_number: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/certificate/{issuer_dn}/{certificate_serial_number}/revocationstatus".format(
        client.base_url, issuer_dn=issuer_dn, certificate_serial_number=certificate_serial_number
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[RevokeStatusRestResponse]:
    if response.status_code == 200:
        response_200 = RevokeStatusRestResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[RevokeStatusRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    issuer_dn: str,
    certificate_serial_number: str,
    *,
    client: Client,
) -> Response[RevokeStatusRestResponse]:
    """Checks revocation status of the specified certificate

     Checks revocation status of the specified certificate

    Args:
        issuer_dn (str):
        certificate_serial_number (str):

    Returns:
        Response[RevokeStatusRestResponse]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        certificate_serial_number=certificate_serial_number,
        client=client,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    issuer_dn: str,
    certificate_serial_number: str,
    *,
    client: Client,
) -> Optional[RevokeStatusRestResponse]:
    """Checks revocation status of the specified certificate

     Checks revocation status of the specified certificate

    Args:
        issuer_dn (str):
        certificate_serial_number (str):

    Returns:
        Response[RevokeStatusRestResponse]
    """

    return sync_detailed(
        issuer_dn=issuer_dn,
        certificate_serial_number=certificate_serial_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    issuer_dn: str,
    certificate_serial_number: str,
    *,
    client: Client,
) -> Response[RevokeStatusRestResponse]:
    """Checks revocation status of the specified certificate

     Checks revocation status of the specified certificate

    Args:
        issuer_dn (str):
        certificate_serial_number (str):

    Returns:
        Response[RevokeStatusRestResponse]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        certificate_serial_number=certificate_serial_number,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    issuer_dn: str,
    certificate_serial_number: str,
    *,
    client: Client,
) -> Optional[RevokeStatusRestResponse]:
    """Checks revocation status of the specified certificate

     Checks revocation status of the specified certificate

    Args:
        issuer_dn (str):
        certificate_serial_number (str):

    Returns:
        Response[RevokeStatusRestResponse]
    """

    return (
        await asyncio_detailed(
            issuer_dn=issuer_dn,
            certificate_serial_number=certificate_serial_number,
            client=client,
        )
    ).parsed
