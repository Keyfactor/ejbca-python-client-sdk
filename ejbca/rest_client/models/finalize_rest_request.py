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

from ..models.finalize_rest_request_response_format import FinalizeRestRequestResponseFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="FinalizeRestRequest")


@attr.s(auto_attribs=True)
class FinalizeRestRequest:
    """
    Attributes:
        response_format (Union[Unset, FinalizeRestRequestResponseFormat]): Response format Example: P12.
        password (Union[Unset, str]): Password Example: foo123.
        key_alg (Union[Unset, str]): Key algorithm Example: RSA.
        key_spec (Union[Unset, str]): Key specification Example: 4096.
    """

    response_format: Union[Unset, FinalizeRestRequestResponseFormat] = UNSET
    password: Union[Unset, str] = UNSET
    key_alg: Union[Unset, str] = UNSET
    key_spec: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        response_format: Union[Unset, str] = UNSET
        if not isinstance(self.response_format, Unset):
            response_format = self.response_format.value

        password = self.password
        key_alg = self.key_alg
        key_spec = self.key_spec

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if password is not UNSET:
            field_dict["password"] = password
        if key_alg is not UNSET:
            field_dict["key_alg"] = key_alg
        if key_spec is not UNSET:
            field_dict["key_spec"] = key_spec

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _response_format = d.pop("response_format", UNSET)
        response_format: Union[Unset, FinalizeRestRequestResponseFormat]
        if isinstance(_response_format, Unset):
            response_format = UNSET
        else:
            response_format = FinalizeRestRequestResponseFormat(_response_format)

        password = d.pop("password", UNSET)

        key_alg = d.pop("key_alg", UNSET)

        key_spec = d.pop("key_spec", UNSET)

        finalize_rest_request = cls(
            response_format=response_format,
            password=password,
            key_alg=key_alg,
            key_spec=key_spec,
        )

        finalize_rest_request.additional_properties = d
        return finalize_rest_request

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
