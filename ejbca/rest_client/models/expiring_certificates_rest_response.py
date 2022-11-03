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

from ..models.certificates_rest_response import CertificatesRestResponse
from ..models.pagination_rest_response_component import PaginationRestResponseComponent
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExpiringCertificatesRestResponse")


@attr.s(auto_attribs=True)
class ExpiringCertificatesRestResponse:
    """
    Attributes:
        pagination_rest_response_component (Union[Unset, PaginationRestResponseComponent]):
        certificates_rest_response (Union[Unset, CertificatesRestResponse]):
    """

    pagination_rest_response_component: Union[Unset, PaginationRestResponseComponent] = UNSET
    certificates_rest_response: Union[Unset, CertificatesRestResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination_rest_response_component: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_rest_response_component, Unset):
            pagination_rest_response_component = self.pagination_rest_response_component.to_dict()

        certificates_rest_response: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificates_rest_response, Unset):
            certificates_rest_response = self.certificates_rest_response.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination_rest_response_component is not UNSET:
            field_dict["pagination_rest_response_component"] = pagination_rest_response_component
        if certificates_rest_response is not UNSET:
            field_dict["certificates_rest_response"] = certificates_rest_response

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pagination_rest_response_component = d.pop("pagination_rest_response_component", UNSET)
        pagination_rest_response_component: Union[Unset, PaginationRestResponseComponent]
        if isinstance(_pagination_rest_response_component, Unset):
            pagination_rest_response_component = UNSET
        else:
            pagination_rest_response_component = PaginationRestResponseComponent.from_dict(
                _pagination_rest_response_component
            )

        _certificates_rest_response = d.pop("certificates_rest_response", UNSET)
        certificates_rest_response: Union[Unset, CertificatesRestResponse]
        if isinstance(_certificates_rest_response, Unset):
            certificates_rest_response = UNSET
        else:
            certificates_rest_response = CertificatesRestResponse.from_dict(_certificates_rest_response)

        expiring_certificates_rest_response = cls(
            pagination_rest_response_component=pagination_rest_response_component,
            certificates_rest_response=certificates_rest_response,
        )

        expiring_certificates_rest_response.additional_properties = d
        return expiring_certificates_rest_response

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
