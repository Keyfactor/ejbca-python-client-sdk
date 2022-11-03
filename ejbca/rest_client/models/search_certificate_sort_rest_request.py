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

from ..models.search_certificate_sort_rest_request_operation import SearchCertificateSortRestRequestOperation
from ..models.search_certificate_sort_rest_request_property import SearchCertificateSortRestRequestProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCertificateSortRestRequest")


@attr.s(auto_attribs=True)
class SearchCertificateSortRestRequest:
    """Use one of allowed values as property and operation.
    Available propertiesUSERNAME
    ISSUER_DN
    SUBJECT_DN
    EXTERNAL_ACCOUNT_BINDING_ID
    END_ENTITY_PROFILE
    CERTIFICATE_PROFILE
    STATUS
    TAG
    TYPE
    UPDATE_TIME
    ISSUED_DATE
    EXPIRE_DATE
    REVOCATION_DATE

    Available operationsASC
    DESC

        Attributes:
            property_ (Union[Unset, SearchCertificateSortRestRequestProperty]): Sorted by
            operation (Union[Unset, SearchCertificateSortRestRequestOperation]): Sort ascending or descending. 'ASC' for
                ascending, 'DESC' for descending.
    """

    property_: Union[Unset, SearchCertificateSortRestRequestProperty] = UNSET
    operation: Union[Unset, SearchCertificateSortRestRequestOperation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_: Union[Unset, str] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, SearchCertificateSortRestRequestProperty]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = SearchCertificateSortRestRequestProperty(_property_)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, SearchCertificateSortRestRequestOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = SearchCertificateSortRestRequestOperation(_operation)

        search_certificate_sort_rest_request = cls(
            property_=property_,
            operation=operation,
        )

        search_certificate_sort_rest_request.additional_properties = d
        return search_certificate_sort_rest_request

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
