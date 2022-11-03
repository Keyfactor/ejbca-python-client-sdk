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

from ..models.search_end_entity_criteria_rest_request_operation import SearchEndEntityCriteriaRestRequestOperation
from ..models.search_end_entity_criteria_rest_request_property import SearchEndEntityCriteriaRestRequestProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEndEntityCriteriaRestRequest")


@attr.s(auto_attribs=True)
class SearchEndEntityCriteriaRestRequest:
    """Use one of allowed values as property(see enum values below).
    QUERY - multiplicity [0, 1] - is used to search by SubjectDn, SubjectAn, Username;
    Available STATUS - multiplicity [0, 9] - values are: NEW, FAILED, INITIALIZED, INPROCESS, GENERATED, REVOKED,
    HISTORICAL, KEYRECOVERY, WAITINGFORADDAPPROVAL;

    END_ENTITY_PROFILE, CERTIFICATE_PROFILE, CA - multiplicity [0, *) - exact match of the name for referencing End
    Entity Profile, Certificate Profile or CA;

        Attributes:
            property_ (Union[Unset, SearchEndEntityCriteriaRestRequestProperty]): A search property
            value (Union[Unset, str]): A search value. This could be string value, an appropriate string name of End Entity
                Profile or Certificate Profile or CA Example: exampleUsername.
            operation (Union[Unset, SearchEndEntityCriteriaRestRequestOperation]): An operation for property on inserted
                value. 'EQUALS' for string, 'LIKE' for string value ('QUERY')
    """

    property_: Union[Unset, SearchEndEntityCriteriaRestRequestProperty] = UNSET
    value: Union[Unset, str] = UNSET
    operation: Union[Unset, SearchEndEntityCriteriaRestRequestOperation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_: Union[Unset, str] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        value = self.value
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if value is not UNSET:
            field_dict["value"] = value
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, SearchEndEntityCriteriaRestRequestProperty]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = SearchEndEntityCriteriaRestRequestProperty(_property_)

        value = d.pop("value", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, SearchEndEntityCriteriaRestRequestOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = SearchEndEntityCriteriaRestRequestOperation(_operation)

        search_end_entity_criteria_rest_request = cls(
            property_=property_,
            value=value,
            operation=operation,
        )

        search_end_entity_criteria_rest_request.additional_properties = d
        return search_end_entity_criteria_rest_request

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
