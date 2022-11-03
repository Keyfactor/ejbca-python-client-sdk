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

from ..models.ca_info_rest_response import CaInfoRestResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="CaInfosRestResponse")


@attr.s(auto_attribs=True)
class CaInfosRestResponse:
    """
    Attributes:
        certificate_authorities (Union[Unset, List[CaInfoRestResponse]]):
    """

    certificate_authorities: Union[Unset, List[CaInfoRestResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_authorities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificate_authorities, Unset):
            certificate_authorities = []
            for certificate_authorities_item_data in self.certificate_authorities:
                certificate_authorities_item = certificate_authorities_item_data.to_dict()

                certificate_authorities.append(certificate_authorities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_authorities is not UNSET:
            field_dict["certificate_authorities"] = certificate_authorities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_authorities = []
        _certificate_authorities = d.pop("certificate_authorities", UNSET)
        for certificate_authorities_item_data in _certificate_authorities or []:
            certificate_authorities_item = CaInfoRestResponse.from_dict(certificate_authorities_item_data)

            certificate_authorities.append(certificate_authorities_item)

        ca_infos_rest_response = cls(
            certificate_authorities=certificate_authorities,
        )

        ca_infos_rest_response.additional_properties = d
        return ca_infos_rest_response

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
