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

T = TypeVar("T", bound="CertificateProfileInfoRestResponseV2")


@attr.s(auto_attribs=True)
class CertificateProfileInfoRestResponseV2:
    """
    Attributes:
        available_key_algs (Union[Unset, List[str]]):
        available_bit_lenghts (Union[Unset, List[int]]):
        available_ecdsa_curves (Union[Unset, List[str]]):
        available_cas (Union[Unset, List[str]]):
    """

    available_key_algs: Union[Unset, List[str]] = UNSET
    available_bit_lenghts: Union[Unset, List[int]] = UNSET
    available_ecdsa_curves: Union[Unset, List[str]] = UNSET
    available_cas: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_key_algs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_key_algs, Unset):
            available_key_algs = self.available_key_algs

        available_bit_lenghts: Union[Unset, List[int]] = UNSET
        if not isinstance(self.available_bit_lenghts, Unset):
            available_bit_lenghts = self.available_bit_lenghts

        available_ecdsa_curves: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_ecdsa_curves, Unset):
            available_ecdsa_curves = self.available_ecdsa_curves

        available_cas: Union[Unset, List[str]] = UNSET
        if not isinstance(self.available_cas, Unset):
            available_cas = self.available_cas

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_key_algs is not UNSET:
            field_dict["available_key_algs"] = available_key_algs
        if available_bit_lenghts is not UNSET:
            field_dict["available_bit_lenghts"] = available_bit_lenghts
        if available_ecdsa_curves is not UNSET:
            field_dict["available_ecdsa_curves"] = available_ecdsa_curves
        if available_cas is not UNSET:
            field_dict["available_cas"] = available_cas

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        available_key_algs = cast(List[str], d.pop("available_key_algs", UNSET))

        available_bit_lenghts = cast(List[int], d.pop("available_bit_lenghts", UNSET))

        available_ecdsa_curves = cast(List[str], d.pop("available_ecdsa_curves", UNSET))

        available_cas = cast(List[str], d.pop("available_cas", UNSET))

        certificate_profile_info_rest_response_v2 = cls(
            available_key_algs=available_key_algs,
            available_bit_lenghts=available_bit_lenghts,
            available_ecdsa_curves=available_ecdsa_curves,
            available_cas=available_cas,
        )

        certificate_profile_info_rest_response_v2.additional_properties = d
        return certificate_profile_info_rest_response_v2

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
