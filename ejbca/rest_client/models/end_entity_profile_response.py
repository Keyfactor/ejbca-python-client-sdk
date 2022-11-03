# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndEntityProfileResponse")


@attr.s(auto_attribs=True)
class EndEntityProfileResponse:
    """
    Attributes:
        end_entity_profile_name (Union[Unset, str]): End Entity profile name Example: ExampleEEP.
        subject_distinguished_name_fields (Union[Unset, List[str]]): List of Subject DN Attributes Example: [ “CN“ ].
        subject_alternative_name_fields (Union[Unset, List[str]]): List of Subject Alternative Name fields Example: [
            “RFC822NAME“ ].
        available_certificate_profiles (Union[Unset, List[str]]): List of available Certificate Profiles Example: [
            “ENDUSER“ ].
        available_cas (Union[Unset, List[str]]): List of available Certificate Authorities (CAs) Example: [ “ExampleCA“
            ].
    """

    end_entity_profile_name: Union[Unset, str] = UNSET
    subject_distinguished_name_fields: Union[Unset, List[str]] = UNSET
    subject_alternative_name_fields: Union[Unset, List[str]] = UNSET
    available_certificate_profiles: Union[Unset, List[str]] = UNSET
    available_cas: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_entity_profile_name = self.end_entity_profile_name
        subject_distinguished_name_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subject_distinguished_name_fields, Unset):
            subject_distinguished_name_fields = self.subject_distinguished_name_fields

        subject_alternative_name_fields: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subject_alternative_name_fields, Unset):
            subject_alternative_name_fields = self.subject_alternative_name_fields

        available_certificate_profiles: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_certificate_profiles, Unset):
            available_certificate_profiles = self.available_certificate_profiles

        available_cas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_cas, Unset):
            available_cas = self.available_cas

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_entity_profile_name is not UNSET:
            field_dict["end_entity_profile_name"] = end_entity_profile_name
        if subject_distinguished_name_fields is not UNSET:
            field_dict["subject_distinguished_name_fields"] = subject_distinguished_name_fields
        if subject_alternative_name_fields is not UNSET:
            field_dict["subject_alternative_name_fields"] = subject_alternative_name_fields
        if available_certificate_profiles is not UNSET:
            field_dict["available_certificate_profiles"] = available_certificate_profiles
        if available_cas is not UNSET:
            field_dict["available_cas"] = available_cas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        end_entity_profile_name = d.pop("end_entity_profile_name", UNSET)

        subject_distinguished_name_fields = cast(List[str], d.pop("subject_distinguished_name_fields", UNSET))

        subject_alternative_name_fields = cast(List[str], d.pop("subject_alternative_name_fields", UNSET))

        available_certificate_profiles = cast(List[str], d.pop("available_certificate_profiles", UNSET))

        available_cas = cast(List[str], d.pop("available_cas", UNSET))

        end_entity_profile_response = cls(
            end_entity_profile_name=end_entity_profile_name,
            subject_distinguished_name_fields=subject_distinguished_name_fields,
            subject_alternative_name_fields=subject_alternative_name_fields,
            available_certificate_profiles=available_certificate_profiles,
            available_cas=available_cas,
        )

        end_entity_profile_response.additional_properties = d
        return end_entity_profile_response

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
