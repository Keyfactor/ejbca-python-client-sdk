# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SshPublicKeyRestResponse")


@attr.s(auto_attribs=True)
class SshPublicKeyRestResponse:
    """
    Attributes:
        ca_name (Union[Unset, str]): Certificate Authority (CA) name Example: CN=ExampleCA.
        response (Union[Unset, str]): CA’s public key Example: ssh-rsa AAAAB...QxLwx SshCA.
    """

    ca_name: Union[Unset, str] = UNSET
    response: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca_name = self.ca_name
        response = self.response

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_name is not UNSET:
            field_dict["ca_name"] = ca_name
        if response is not UNSET:
            field_dict["response"] = response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ca_name = d.pop("ca_name", UNSET)

        response = d.pop("response", UNSET)

        ssh_public_key_rest_response = cls(
            ca_name=ca_name,
            response=response,
        )

        ssh_public_key_rest_response.additional_properties = d
        return ssh_public_key_rest_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
