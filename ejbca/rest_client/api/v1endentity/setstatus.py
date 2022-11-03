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
from ...models.set_end_entity_status_rest_request import SetEndEntityStatusRestRequest
from ...types import Response


def _get_kwargs(
    endentity_name: str,
    *,
    client: Client,
    json_body: SetEndEntityStatusRestRequest,
) -> Dict[str, Any]:
    url = "{}/v1/endentity/{endentity_name}/setstatus".format(client.base_url, endentity_name=endentity_name)

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
    endentity_name: str,
    *,
    client: Client,
    json_body: SetEndEntityStatusRestRequest,
) -> Response[Any]:
    """Edits end entity setting new status

     Edit status, password and token type of related end entity

    Args:
        endentity_name (str):
        json_body (SetEndEntityStatusRestRequest): Use one of allowed values as property(see enum
            values below).
            Available TOKEN - USERGENERATED, P12, BCFKS, JKS, PEM;
            Available STATUS - NEW, FAILED, INITIALIZED, INPROCESS, GENERATED, REVOKED, HISTORICAL,
            KEYRECOVERY, WAITINGFORADDAPPROVAL;

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endentity_name=endentity_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        cert=client.cert,
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response).parsed


async def asyncio_detailed(
    endentity_name: str,
    *,
    client: Client,
    json_body: SetEndEntityStatusRestRequest,
) -> Response[Any]:
    """Edits end entity setting new status

     Edit status, password and token type of related end entity

    Args:
        endentity_name (str):
        json_body (SetEndEntityStatusRestRequest): Use one of allowed values as property(see enum
            values below).
            Available TOKEN - USERGENERATED, P12, BCFKS, JKS, PEM;
            Available STATUS - NEW, FAILED, INITIALIZED, INPROCESS, GENERATED, REVOKED, HISTORICAL,
            KEYRECOVERY, WAITINGFORADDAPPROVAL;

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endentity_name=endentity_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response).parsed
