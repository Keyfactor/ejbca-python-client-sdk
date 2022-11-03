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

from ..models.add_end_entity_rest_request_token import AddEndEntityRestRequestToken
from ..models.extended_information_rest_request_component import ExtendedInformationRestRequestComponent
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddEndEntityRestRequest")


@attr.s(auto_attribs=True)
class AddEndEntityRestRequest:
    """
    Attributes:
        username (Union[Unset, str]): Username Example: JohnDoe.
        password (Union[Unset, str]): Password Example: foo123.
        subject_dn (Union[Unset, str]): Subject Distinguished Name Example: CN=John Doe,SURNAME=Doe,GIVENNAME=John,C=SE.
        subject_alt_name (Union[Unset, str]): Subject Alternative Name (SAN) Example: rfc822Name=john.doe@example.com.
        email (Union[Unset, str]): Email Example: john.doe@example.com.
        extension_data (Union[Unset, List[ExtendedInformationRestRequestComponent]]):
        ca_name (Union[Unset, str]): Certificate Authority (CA) name Example: CN=ExampleCA.
        certificate_profile_name (Union[Unset, str]): Certificate profile name Example: ENDUSER.
        end_entity_profile_name (Union[Unset, str]): End Entity profile name Example: ExampleEEP.
        token (Union[Unset, AddEndEntityRestRequestToken]): Token type property Example: P12.
        account_binding_id (Union[Unset, str]): Account Binding ID Example: 1234567890.
    """

    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    subject_dn: Union[Unset, str] = UNSET
    subject_alt_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    extension_data: Union[Unset, List[ExtendedInformationRestRequestComponent]] = UNSET
    ca_name: Union[Unset, str] = UNSET
    certificate_profile_name: Union[Unset, str] = UNSET
    end_entity_profile_name: Union[Unset, str] = UNSET
    token: Union[Unset, AddEndEntityRestRequestToken] = UNSET
    account_binding_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        subject_dn = self.subject_dn
        subject_alt_name = self.subject_alt_name
        email = self.email
        extension_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extension_data, Unset):
            extension_data = []
            for extension_data_item_data in self.extension_data:
                extension_data_item = extension_data_item_data.to_dict()

                extension_data.append(extension_data_item)

        ca_name = self.ca_name
        certificate_profile_name = self.certificate_profile_name
        end_entity_profile_name = self.end_entity_profile_name
        token: Union[Unset, str] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token.value

        account_binding_id = self.account_binding_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if subject_dn is not UNSET:
            field_dict["subject_dn"] = subject_dn
        if subject_alt_name is not UNSET:
            field_dict["subject_alt_name"] = subject_alt_name
        if email is not UNSET:
            field_dict["email"] = email
        if extension_data is not UNSET:
            field_dict["extension_data"] = extension_data
        if ca_name is not UNSET:
            field_dict["ca_name"] = ca_name
        if certificate_profile_name is not UNSET:
            field_dict["certificate_profile_name"] = certificate_profile_name
        if end_entity_profile_name is not UNSET:
            field_dict["end_entity_profile_name"] = end_entity_profile_name
        if token is not UNSET:
            field_dict["token"] = token
        if account_binding_id is not UNSET:
            field_dict["account_binding_id"] = account_binding_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        subject_dn = d.pop("subject_dn", UNSET)

        subject_alt_name = d.pop("subject_alt_name", UNSET)

        email = d.pop("email", UNSET)

        extension_data = []
        _extension_data = d.pop("extension_data", UNSET)
        for extension_data_item_data in _extension_data or []:
            extension_data_item = ExtendedInformationRestRequestComponent.from_dict(extension_data_item_data)

            extension_data.append(extension_data_item)

        ca_name = d.pop("ca_name", UNSET)

        certificate_profile_name = d.pop("certificate_profile_name", UNSET)

        end_entity_profile_name = d.pop("end_entity_profile_name", UNSET)

        _token = d.pop("token", UNSET)
        token: Union[Unset, AddEndEntityRestRequestToken]
        if isinstance(_token, Unset):
            token = UNSET
        else:
            token = AddEndEntityRestRequestToken(_token)

        account_binding_id = d.pop("account_binding_id", UNSET)

        add_end_entity_rest_request = cls(
            username=username,
            password=password,
            subject_dn=subject_dn,
            subject_alt_name=subject_alt_name,
            email=email,
            extension_data=extension_data,
            ca_name=ca_name,
            certificate_profile_name=certificate_profile_name,
            end_entity_profile_name=end_entity_profile_name,
            token=token,
            account_binding_id=account_binding_id,
        )

        add_end_entity_rest_request.additional_properties = d
        return add_end_entity_rest_request

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
