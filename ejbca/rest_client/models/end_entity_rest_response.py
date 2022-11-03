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

from ..models.end_entity_rest_response_status import EndEntityRestResponseStatus
from ..models.end_entity_rest_response_token import EndEntityRestResponseToken
from ..models.extended_information_rest_response_component import ExtendedInformationRestResponseComponent
from ..types import UNSET, Unset

T = TypeVar("T", bound="EndEntityRestResponse")


@attr.s(auto_attribs=True)
class EndEntityRestResponse:
    """
    Attributes:
        username (Union[Unset, str]): Username Example: JohnDoe.
        dn (Union[Unset, str]): Subject Distinguished Name Example: CN=John Doe,SURNAME=Doe,GIVENNAME=John,C=SE.
        subject_alt_name (Union[Unset, str]): Subject Alternative Name (SAN) Example: rfc822Name=john.doe@example.com.
        email (Union[Unset, str]): Email Example: john.doe@example.com.
        status (Union[Unset, EndEntityRestResponseStatus]): End Entity status Example: NEW.
        token (Union[Unset, EndEntityRestResponseToken]): Token type Example: P12.
        extension_data (Union[Unset, List[ExtendedInformationRestResponseComponent]]): Extended Information
    """

    username: Union[Unset, str] = UNSET
    dn: Union[Unset, str] = UNSET
    subject_alt_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    status: Union[Unset, EndEntityRestResponseStatus] = UNSET
    token: Union[Unset, EndEntityRestResponseToken] = UNSET
    extension_data: Union[Unset, List[ExtendedInformationRestResponseComponent]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        dn = self.dn
        subject_alt_name = self.subject_alt_name
        email = self.email
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        token: Union[Unset, str] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.value

        extension_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extension_data, Unset):
            extension_data = []
            for extension_data_item_data in self.extension_data:
                extension_data_item = extension_data_item_data.to_dict()

                extension_data.append(extension_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if dn is not UNSET:
            field_dict["dn"] = dn
        if subject_alt_name is not UNSET:
            field_dict["subject_alt_name"] = subject_alt_name
        if email is not UNSET:
            field_dict["email"] = email
        if status is not UNSET:
            field_dict["status"] = status
        if token is not UNSET:
            field_dict["token"] = token
        if extension_data is not UNSET:
            field_dict["extension_data"] = extension_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        dn = d.pop("dn", UNSET)

        subject_alt_name = d.pop("subject_alt_name", UNSET)

        email = d.pop("email", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, EndEntityRestResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = EndEntityRestResponseStatus(_status)

        _token = d.pop("token", UNSET)
        token: Union[Unset, EndEntityRestResponseToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = EndEntityRestResponseToken(_token)

        extension_data = []
        _extension_data = d.pop("extension_data", UNSET)
        for extension_data_item_data in _extension_data or []:
            extension_data_item = ExtendedInformationRestResponseComponent.from_dict(extension_data_item_data)

            extension_data.append(extension_data_item)

        end_entity_rest_response = cls(
            username=username,
            dn=dn,
            subject_alt_name=subject_alt_name,
            email=email,
            status=status,
            token=token,
            extension_data=extension_data,
        )

        end_entity_rest_response.additional_properties = d
        return end_entity_rest_response

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
