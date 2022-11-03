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
from ...types import Response


def _get_kwargs(
    endentity_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/endentity/{endentity_name}".format(client.base_url, endentity_name=endentity_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
) -> Response[Any]:
    """Deletes end entity

     Deletes specified end entity and keeps certificate information untouched, if end entity does not
    exist success is still returned

    Args:
        endentity_name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endentity_name=endentity_name,
        client=client,
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
) -> Response[Any]:
    """Deletes end entity

     Deletes specified end entity and keeps certificate information untouched, if end entity does not
    exist success is still returned

    Args:
        endentity_name (str):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        endentity_name=endentity_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response).parsed
