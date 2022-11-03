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

from ..models.end_entity_revocation_rest_request_reason_code import EndEntityRevocationRestRequestReasonCode
from ..types import UNSET, Unset

T = TypeVar("T", bound="EndEntityRevocationRestRequest")


@attr.s(auto_attribs=True)
class EndEntityRevocationRestRequest:
    """End Entity revocation request. Available reason codes:
    0 - Unspecified,
    1 - Key Compromise,
    2 - CA Compromise,
    3 - Affiliation Changed,
    4 - Superseded,
    5 - Cessation of Operation,
    6 - Certificate Hold,
    8 - Remove from CRL,
    9 - Privileges Withdrawn,
    10 - AA Compromise

       Attributes:
           reason_code (Union[Unset, EndEntityRevocationRestRequestReasonCode]): Reason code Example: 2.
           delete (Union[Unset, bool]): Delete Example: True.
    """

    reason_code: Union[Unset, EndEntityRevocationRestRequestReasonCode] = UNSET
    delete: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reason_code: Union[Unset, int] = UNSET
        if not isinstance(self.reason_code, Unset):
            reason_code = self.reason_code.value

        delete = self.delete

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason_code is not UNSET:
            field_dict["reason_code"] = reason_code
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _reason_code = d.pop("reason_code", UNSET)
        reason_code: Union[Unset, EndEntityRevocationRestRequestReasonCode]
        if isinstance(_reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = EndEntityRevocationRestRequestReasonCode(_reason_code)

        delete = d.pop("delete", UNSET)

        end_entity_revocation_rest_request = cls(
            reason_code=reason_code,
            delete=delete,
        )

        end_entity_revocation_rest_request.additional_properties = d
        return end_entity_revocation_rest_request

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
