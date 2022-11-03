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

from ..models.certificate_rest_response_v2 import CertificateRestResponseV2
from ..models.pagination_summary import PaginationSummary
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCertificatesRestResponseV2")


@attr.s(auto_attribs=True)
class SearchCertificatesRestResponseV2:
    """
    Attributes:
        certificates (Union[Unset, List[CertificateRestResponseV2]]):
        pagination_summary (Union[Unset, PaginationSummary]):
    """

    certificates: Union[Unset, List[CertificateRestResponseV2]] = UNSET
    pagination_summary: Union[Unset, PaginationSummary] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificates: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()

                certificates.append(certificates_item)

        pagination_summary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination_summary, Unset):
            pagination_summary = self.pagination_summary.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if pagination_summary is not UNSET:
            field_dict["pagination_summary"] = pagination_summary

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = CertificateRestResponseV2.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        _pagination_summary = d.pop("pagination_summary", UNSET)
        pagination_summary: Union[Unset, PaginationSummary]
        if isinstance(_pagination_summary, Unset):
            pagination_summary = UNSET
        else:
            pagination_summary = PaginationSummary.from_dict(_pagination_summary)

        search_certificates_rest_response_v2 = cls(
            certificates=certificates,
            pagination_summary=pagination_summary,
        )

        search_certificates_rest_response_v2.additional_properties = d
        return search_certificates_rest_response_v2

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
