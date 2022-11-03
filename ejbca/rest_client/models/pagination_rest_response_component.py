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

T = TypeVar("T", bound="PaginationRestResponseComponent")


@attr.s(auto_attribs=True)
class PaginationRestResponseComponent:
    """
    Attributes:
        more_results (Union[Unset, bool]):
        next_offset (Union[Unset, int]):
        number_of_results (Union[Unset, int]):
    """

    more_results: Union[Unset, bool] = UNSET
    next_offset: Union[Unset, int] = UNSET
    number_of_results: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        more_results = self.more_results
        next_offset = self.next_offset
        number_of_results = self.number_of_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if more_results is not UNSET:
            field_dict["more_results"] = more_results
        if next_offset is not UNSET:
            field_dict["next_offset"] = next_offset
        if number_of_results is not UNSET:
            field_dict["number_of_results"] = number_of_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        more_results = d.pop("more_results", UNSET)

        next_offset = d.pop("next_offset", UNSET)

        number_of_results = d.pop("number_of_results", UNSET)

        pagination_rest_response_component = cls(
            more_results=more_results,
            next_offset=next_offset,
            number_of_results=number_of_results,
        )

        pagination_rest_response_component.additional_properties = d
        return pagination_rest_response_component

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
