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

from ..models.set_end_entity_status_rest_request_status import SetEndEntityStatusRestRequestStatus
from ..models.set_end_entity_status_rest_request_token import SetEndEntityStatusRestRequestToken
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetEndEntityStatusRestRequest")


@attr.s(auto_attribs=True)
class SetEndEntityStatusRestRequest:
    """Use one of allowed values as property(see enum values below).
    Available TOKEN - USERGENERATED, P12, BCFKS, JKS, PEM;
    Available STATUS - NEW, FAILED, INITIALIZED, INPROCESS, GENERATED, REVOKED, HISTORICAL, KEYRECOVERY,
    WAITINGFORADDAPPROVAL;

        Attributes:
            password (Union[Unset, str]): Password Example: foo123.
            token (Union[Unset, SetEndEntityStatusRestRequestToken]): Token type property Example: USERGENERATED.
            status (Union[Unset, SetEndEntityStatusRestRequestStatus]): End entity status property Example: NEW.
    """

    password: Union[Unset, str] = UNSET
    token: Union[Unset, SetEndEntityStatusRestRequestToken] = UNSET
    status: Union[Unset, SetEndEntityStatusRestRequestStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        token: Union[Unset, str] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if token is not UNSET:
            field_dict["token"] = token
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, SetEndEntityStatusRestRequestToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = SetEndEntityStatusRestRequestToken(_token)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SetEndEntityStatusRestRequestStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SetEndEntityStatusRestRequestStatus(_status)

        set_end_entity_status_rest_request = cls(
            password=password,
            token=token,
            status=status,
        )

        set_end_entity_status_rest_request.additional_properties = d
        return set_end_entity_status_rest_request

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
