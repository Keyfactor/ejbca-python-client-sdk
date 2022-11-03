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

from ..models.end_entity_profile_rest_response import EndEntityProfileRestResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthorizedEEPsRestResponse")


@attr.s(auto_attribs=True)
class AuthorizedEEPsRestResponse:
    """
    Attributes:
        end_entitie_profiles (Union[Unset, List[EndEntityProfileRestResponse]]):
    """

    end_entitie_profiles: Union[Unset, List[EndEntityProfileRestResponse]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_entitie_profiles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.end_entitie_profiles, Unset):
            end_entitie_profiles = []
            for end_entitie_profiles_item_data in self.end_entitie_profiles:
                end_entitie_profiles_item = end_entitie_profiles_item_data.to_dict()

                end_entitie_profiles.append(end_entitie_profiles_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_entitie_profiles is not UNSET:
            field_dict["end_entitie_profiles"] = end_entitie_profiles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_entitie_profiles = []
        _end_entitie_profiles = d.pop("end_entitie_profiles", UNSET)
        for end_entitie_profiles_item_data in _end_entitie_profiles or []:
            end_entitie_profiles_item = EndEntityProfileRestResponse.from_dict(end_entitie_profiles_item_data)

            end_entitie_profiles.append(end_entitie_profiles_item)

        authorized_ee_ps_rest_response = cls(
            end_entitie_profiles=end_entitie_profiles,
        )

        authorized_ee_ps_rest_response.additional_properties = d
        return authorized_ee_ps_rest_response

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
