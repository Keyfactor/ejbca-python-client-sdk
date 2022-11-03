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

from ..models.search_end_entities_sort_rest_request import SearchEndEntitiesSortRestRequest
from ..models.search_end_entity_criteria_rest_request import SearchEndEntityCriteriaRestRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEndEntitiesRestRequestV2")


@attr.s(auto_attribs=True)
class SearchEndEntitiesRestRequestV2:
    """
    Attributes:
        max_number_of_results (Union[Unset, int]): Maximum number of results Example: 10.
        current_page (Union[Unset, int]): Current page number
        criteria (Union[Unset, List[SearchEndEntityCriteriaRestRequest]]): A List of search criteria.
        sort_operation (Union[Unset, SearchEndEntitiesSortRestRequest]): Use one of allowed values as property and
            operation.
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
    """

    max_number_of_results: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    criteria: Union[Unset, List[SearchEndEntityCriteriaRestRequest]] = UNSET
    sort_operation: Union[Unset, SearchEndEntitiesSortRestRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_number_of_results = self.max_number_of_results
        current_page = self.current_page
        criteria: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()

                criteria.append(criteria_item)

        sort_operation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort_operation, Unset):
            sort_operation = self.sort_operation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_number_of_results is not UNSET:
            field_dict["max_number_of_results"] = max_number_of_results
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if sort_operation is not UNSET:
            field_dict["sort_operation"] = sort_operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_number_of_results = d.pop("max_number_of_results", UNSET)

        current_page = d.pop("current_page", UNSET)

        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = SearchEndEntityCriteriaRestRequest.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        _sort_operation = d.pop("sort_operation", UNSET)
        sort_operation: Union[Unset, SearchEndEntitiesSortRestRequest]
        if isinstance(_sort_operation, Unset):
            sort_operation = UNSET
        else:
            sort_operation = SearchEndEntitiesSortRestRequest.from_dict(_sort_operation)

        search_end_entities_rest_request_v2 = cls(
            max_number_of_results=max_number_of_results,
            current_page=current_page,
            criteria=criteria,
            sort_operation=sort_operation,
        )

        search_end_entities_rest_request_v2.additional_properties = d
        return search_end_entities_rest_request_v2

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
