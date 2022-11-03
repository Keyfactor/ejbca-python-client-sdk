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
from ...models.certificate_rest_response import CertificateRestResponse
from ...models.finalize_rest_request import FinalizeRestRequest
from ...types import Response


def _get_kwargs(
    request_id: int,
    *,
    client: Client,
    json_body: FinalizeRestRequest,
) -> Dict[str, Any]:
    url = "{}/v1/certificate/{request_id}/finalize".format(client.base_url, request_id=request_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[CertificateRestResponse]:
    if response.status_code == 201:
        response_201 = CertificateRestResponse.from_dict(response.json())

        return response_201
    return None


def _build_response(*, response: httpx.Response) -> Response[CertificateRestResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    request_id: int,
    *,
    client: Client,
    json_body: FinalizeRestRequest,
) -> Response[CertificateRestResponse]:
    """Finalize enrollment

     Finalizes enrollment after administrator approval using request Id

    Args:
        request_id (int):
        json_body (FinalizeRestRequest):

    Returns:
        Response[CertificateRestResponse]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    request_id: int,
    *,
    client: Client,
    json_body: FinalizeRestRequest,
) -> Optional[CertificateRestResponse]:
    """Finalize enrollment

     Finalizes enrollment after administrator approval using request Id

    Args:
        request_id (int):
        json_body (FinalizeRestRequest):

    Returns:
        Response[CertificateRestResponse]
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    request_id: int,
    *,
    client: Client,
    json_body: FinalizeRestRequest,
) -> Response[CertificateRestResponse]:
    """Finalize enrollment

     Finalizes enrollment after administrator approval using request Id

    Args:
        request_id (int):
        json_body (FinalizeRestRequest):

    Returns:
        Response[CertificateRestResponse]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    request_id: int,
    *,
    client: Client,
    json_body: FinalizeRestRequest,
) -> Optional[CertificateRestResponse]:
    """Finalize enrollment

     Finalizes enrollment after administrator approval using request Id

    Args:
        request_id (int):
        json_body (FinalizeRestRequest):

    Returns:
        Response[CertificateRestResponse]
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
