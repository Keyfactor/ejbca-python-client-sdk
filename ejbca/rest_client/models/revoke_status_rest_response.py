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

T = TypeVar("T", bound="RevokeStatusRestResponse")


@attr.s(auto_attribs=True)
class RevokeStatusRestResponse:
    """
    Attributes:
        issuer_dn (Union[Unset, str]): Issuer Distinguished Name Example: CN=ExampleCA.
        serial_number (Union[Unset, str]): Hex Serial Number Example: 1234567890ABCDEF.
        revocation_reason (Union[Unset, str]): RFC5280 revokation reason Example: KEY_COMPROMISE.
        revocation_date (Union[Unset, datetime.datetime]): Revokation date Example: 1970-01-01 00:00:00+00:00.
        message (Union[Unset, str]): Message Example: Successfully revoked.
        revoked (Union[Unset, bool]):
    """

    issuer_dn: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    revocation_reason: Union[Unset, str] = UNSET
    revocation_date: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    revoked: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer_dn = self.issuer_dn
        serial_number = self.serial_number
        revocation_reason = self.revocation_reason
        revocation_date: Union[Unset, str] = UNSET
        if not isinstance(self.revocation_date, Unset):
            revocation_date = self.revocation_date.isoformat()

        message = self.message
        revoked = self.revoked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer_dn is not UNSET:
            field_dict["issuer_dn"] = issuer_dn
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if revocation_reason is not UNSET:
            field_dict["revocation_reason"] = revocation_reason
        if revocation_date is not UNSET:
            field_dict["revocation_date"] = revocation_date
        if message is not UNSET:
            field_dict["message"] = message
        if revoked is not UNSET:
            field_dict["revoked"] = revoked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuer_dn = d.pop("issuer_dn", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        revocation_reason = d.pop("revocation_reason", UNSET)

        _revocation_date = d.pop("revocation_date", UNSET)
        revocation_date: Union[Unset, datetime.datetime]
        if isinstance(_revocation_date, Unset):
            revocation_date = UNSET
        else:
            revocation_date = isoparse(_revocation_date)

        message = d.pop("message", UNSET)

        revoked = d.pop("revoked", UNSET)

        revoke_status_rest_response = cls(
            issuer_dn=issuer_dn,
            serial_number=serial_number,
            revocation_reason=revocation_reason,
            revocation_date=revocation_date,
            message=message,
            revoked=revoked,
        )

        revoke_status_rest_response.additional_properties = d
        return revoke_status_rest_response

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
