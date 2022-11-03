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

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnrollCertificateRestRequest")


@attr.s(auto_attribs=True)
class EnrollCertificateRestRequest:
    """
    Attributes:
        certificate_request (Union[Unset, str]): Certificate request Example: -----BEGIN CERTIFICATE REQUEST-----
            MIICh...V8shQ==
            -----END CERTIFICATE REQUEST-----.
        certificate_profile_name (Union[Unset, str]): Certificate profile name Example: ENDUSER.
        end_entity_profile_name (Union[Unset, str]): End Entity profile name Example: ExampleEEP.
        certificate_authority_name (Union[Unset, str]): Certificate Authority (CA) name Example: CN=ExampleCA.
        username (Union[Unset, str]): Username Example: JohnDoe.
        password (Union[Unset, str]): Password Example: foo123.
        account_binding_id (Union[Unset, str]): Account Binding ID Example: 1234567890.
        include_chain (Union[Unset, bool]):
        email (Union[Unset, str]): Email Example: john.doe@example.com.
    """

    certificate_request: Union[Unset, str] = UNSET
    certificate_profile_name: Union[Unset, str] = UNSET
    end_entity_profile_name: Union[Unset, str] = UNSET
    certificate_authority_name: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    account_binding_id: Union[Unset, str] = UNSET
    include_chain: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        certificate_request = self.certificate_request
        certificate_profile_name = self.certificate_profile_name
        end_entity_profile_name = self.end_entity_profile_name
        certificate_authority_name = self.certificate_authority_name
        username = self.username
        password = self.password
        account_binding_id = self.account_binding_id
        include_chain = self.include_chain
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificate_request is not UNSET:
            field_dict["certificate_request"] = certificate_request
        if certificate_profile_name is not UNSET:
            field_dict["certificate_profile_name"] = certificate_profile_name
        if end_entity_profile_name is not UNSET:
            field_dict["end_entity_profile_name"] = end_entity_profile_name
        if certificate_authority_name is not UNSET:
            field_dict["certificate_authority_name"] = certificate_authority_name
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if account_binding_id is not UNSET:
            field_dict["account_binding_id"] = account_binding_id
        if include_chain is not UNSET:
            field_dict["include_chain"] = include_chain
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        certificate_request = d.pop("certificate_request", UNSET)

        certificate_profile_name = d.pop("certificate_profile_name", UNSET)

        end_entity_profile_name = d.pop("end_entity_profile_name", UNSET)

        certificate_authority_name = d.pop("certificate_authority_name", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        account_binding_id = d.pop("account_binding_id", UNSET)

        include_chain = d.pop("include_chain", UNSET)

        email = d.pop("email", UNSET)

        enroll_certificate_rest_request = cls(
            certificate_request=certificate_request,
            certificate_profile_name=certificate_profile_name,
            end_entity_profile_name=end_entity_profile_name,
            certificate_authority_name=certificate_authority_name,
            username=username,
            password=password,
            account_binding_id=account_binding_id,
            include_chain=include_chain,
            email=email,
        )

        enroll_certificate_rest_request.additional_properties = d
        return enroll_certificate_rest_request

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
