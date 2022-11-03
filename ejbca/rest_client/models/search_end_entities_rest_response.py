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

from ..models.end_entity_rest_response import EndEntityRestResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEndEntitiesRestResponse")


@attr.s(auto_attribs=True)
class SearchEndEntitiesRestResponse:
    """
    Attributes:
        end_entities (Union[Unset, List[EndEntityRestResponse]]):
        more_results (Union[Unset, bool]):
    """

    end_entities: Union[Unset, List[EndEntityRestResponse]] = UNSET
    more_results: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.end_entities, Unset):
            end_entities = []
            for end_entities_item_data in self.end_entities:
                end_entities_item = end_entities_item_data.to_dict()

                end_entities.append(end_entities_item)

        more_results = self.more_results

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_entities is not UNSET:
            field_dict["end_entities"] = end_entities
        if more_results is not UNSET:
            field_dict["more_results"] = more_results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_entities = []
        _end_entities = d.pop("end_entities", UNSET)
        for end_entities_item_data in _end_entities or []:
            end_entities_item = EndEntityRestResponse.from_dict(end_entities_item_data)

            end_entities.append(end_entities_item)

        more_results = d.pop("more_results", UNSET)

        search_end_entities_rest_response = cls(
            end_entities=end_entities,
            more_results=more_results,
        )

        search_end_entities_rest_response.additional_properties = d
        return search_end_entities_rest_response

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
