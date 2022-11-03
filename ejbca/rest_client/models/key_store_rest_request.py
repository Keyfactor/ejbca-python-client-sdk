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

T = TypeVar("T", bound="KeyStoreRestRequest")


@attr.s(auto_attribs=True)
class KeyStoreRestRequest:
    """
    Attributes:
        username (Union[Unset, str]): Username Example: JohnDoe.
        password (Union[Unset, str]): Password Example: foo123.
        key_alg (Union[Unset, str]): Key algorithm used for enrollment Example: RSA.
        key_spec (Union[Unset, str]): Key specification to use Example: 4096.
    """

    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    key_alg: Union[Unset, str] = UNSET
    key_spec: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        key_alg = self.key_alg
        key_spec = self.key_spec

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
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
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        key_alg = d.pop("key_alg", UNSET)

        key_spec = d.pop("key_spec", UNSET)

        key_store_rest_request = cls(
            username=username,
            password=password,
            key_alg=key_alg,
            key_spec=key_spec,
        )

        key_store_rest_request.additional_properties = d
        return key_store_rest_request

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
