# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CaInfoRestResponse")


@attr.s(auto_attribs=True)
class CaInfoRestResponse:
    """
    Attributes:
        id (Union[Unset, int]): CA identifier Example: 12345678.
        name (Union[Unset, str]): Certificate Authority (CA) name Example: CN=ExampleCA.
        subject_dn (Union[Unset, str]): Subject Distinguished Name Example: CN=ExampleCA,O=Sample,C=SE.
        issuer_dn (Union[Unset, str]): Issuer Distinguished Name Example: CN=ExampleCA,O=Sample,C=SE.
        expiration_date (Union[Unset, datetime.datetime]): Expiration date Example: 2038-01-19 03:14:07+00:00.
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    subject_dn: Union[Unset, str] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        subject_dn = self.subject_dn
        issuer_dn = self.issuer_dn
        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if subject_dn is not UNSET:
            field_dict["subject_dn"] = subject_dn
        if issuer_dn is not UNSET:
            field_dict["issuer_dn"] = issuer_dn
        if expiration_date is not UNSET:
            field_dict["expiration_date"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        subject_dn = d.pop("subject_dn", UNSET)

        issuer_dn = d.pop("issuer_dn", UNSET)

        _expiration_date = d.pop("expiration_date", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        ca_info_rest_response = cls(
            id=id,
            name=name,
            subject_dn=subject_dn,
            issuer_dn=issuer_dn,
            expiration_date=expiration_date,
        )

        ca_info_rest_response.additional_properties = d
        return ca_info_rest_response

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
