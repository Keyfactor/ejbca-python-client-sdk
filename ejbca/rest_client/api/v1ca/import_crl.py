# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict

import httpx

from ...client import Client
from ...models.import_crl_multipart_data import ImportCrlMultipartData
from ...types import Response


def _get_kwargs(
    issuer_dn: str,
    *,
    client: Client,
    multipart_data: ImportCrlMultipartData,
) -> Dict[str, Any]:
    url = "{}/v1/ca/{issuer_dn}/importcrl".format(client.base_url, issuer_dn=issuer_dn)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=EmptyResponse(),
    )


class EmptyResponse:
  def to_dict(self):
    return None
def sync(
    issuer_dn: str,
    *,
    client: Client,
    multipart_data: ImportCrlMultipartData,
) -> Response[Any]:
    """Import a certificate revocation list (CRL) for a CA

    Args:
        issuer_dn (str):
        multipart_data (ImportCrlMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio_detailed(
    issuer_dn: str,
    *,
    client: Client,
    multipart_data: ImportCrlMultipartData,
) -> Response[Any]:
    """Import a certificate revocation list (CRL) for a CA

    Args:
        issuer_dn (str):
        multipart_data (ImportCrlMultipartData):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        issuer_dn=issuer_dn,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response).parsed
