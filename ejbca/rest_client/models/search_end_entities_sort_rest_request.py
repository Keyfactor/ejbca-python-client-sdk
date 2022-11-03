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

from ..models.search_end_entities_sort_rest_request_operation import SearchEndEntitiesSortRestRequestOperation
from ..models.search_end_entities_sort_rest_request_property import SearchEndEntitiesSortRestRequestProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEndEntitiesSortRestRequest")


@attr.s(auto_attribs=True)
class SearchEndEntitiesSortRestRequest:
    """Use one of allowed values as property and operation.
    Available propertiesUSERNAME
    SUBJECT_DN
    SUBJECT_ALT_NAME
    END_ENTITY_PROFILE(by databse identifier, not user-given name)
    CERTIFICATE_PROFILE(by identifier)
    CA(by identifier)
    STATUS
    UPDATE_TIME
    CREATED_DATE

    Available operationsASC
    DESC

        Attributes:
            property_ (Union[Unset, SearchEndEntitiesSortRestRequestProperty]): Sorted by
            operation (Union[Unset, SearchEndEntitiesSortRestRequestOperation]): Sort ascending or descending. 'ASC' for
                ascending, 'DESC' for descending.
    """

    property_: Union[Unset, SearchEndEntitiesSortRestRequestProperty] = UNSET
    operation: Union[Unset, SearchEndEntitiesSortRestRequestOperation] = UNSET
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
        property_: Union[Unset, SearchEndEntitiesSortRestRequestProperty]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = SearchEndEntitiesSortRestRequestProperty(_property_)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, SearchEndEntitiesSortRestRequestOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = SearchEndEntitiesSortRestRequestOperation(_operation)

        search_end_entities_sort_rest_request = cls(
            property_=property_,
            operation=operation,
        )

        search_end_entities_sort_rest_request.additional_properties = d
        return search_end_entities_sort_rest_request

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
