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

from ..models.certificate_rest_response_v2_revocation_reason import CertificateRestResponseV2RevocationReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateRestResponseV2")


@attr.s(auto_attribs=True)
class CertificateRestResponseV2:
    """
    Attributes:
        fingerprint (Union[Unset, str]): Certificate fingerprint Example: 123abc456def789ghi123klm456nop789qrs123t.
        c_a_fingerprint (Union[Unset, str]): Certificate Authority fingerprint Example:
            abc123def456ghi789klm123nop456qrs789tvx1.
        certificate_profile_id (Union[Unset, int]): Certificate Profile Identifier Example: 1.
        end_entity_profile_id (Union[Unset, int]): End Entity Profile Identifier Example: 1.
        expire_date (Union[Unset, int]): Date after which certificate should be considered expired Example:
            2147483647000.
        issuer_dn (Union[Unset, str]): Issuer Distinguished Name Example: CN=ExampleCA.
        not_before (Union[Unset, int]): Date at which certificate became valid Example: 1659952800011.
        revocation_date (Union[Unset, int]): Revocation date Example: -1.
        revocation_reason (Union[Unset, CertificateRestResponseV2RevocationReason]): Revocation reson Example: -1.
        serial_number (Union[Unset, str]): Hex Serial Number Example: 1234567890ABCDEF.
        status (Union[Unset, int]): Certificate status Example: 20.
        subject_alt_name (Union[Unset, str]): Subject Alternative Name (SAN) Example: rfc822Name=john.doe@example.com.
        subject_dn (Union[Unset, str]): Subject Distinguished Name Example: CN=John Doe,SURNAME=Doe,GIVENNAME=John,C=SE.
        subject_key_id (Union[Unset, str]): Subject Key Identifier Example: z123abc456def789ghi123klm456nop789qrs123.
        tag (Union[Unset, str]):
        type (Union[Unset, int]):
        udpate_time (Union[Unset, int]): Update time Example: 1659967133000.
        username (Union[Unset, str]): Username Example: JohnDoe.
        base_64_cert (Union[Unset, str]): Base64 encoded certificate Example: TUlJR...t2A==.
        certificate_request (Union[Unset, str]): Certificate request Example: -----BEGIN CERTIFICATE REQUEST-----
            MIICh...V8shQ==
            -----END CERTIFICATE REQUEST-----.
        crl_partition_index (Union[Unset, int]): CRL partition index Example: 1.
    """

    fingerprint: Union[Unset, str] = UNSET
    c_a_fingerprint: Union[Unset, str] = UNSET
    certificate_profile_id: Union[Unset, int] = UNSET
    end_entity_profile_id: Union[Unset, int] = UNSET
    expire_date: Union[Unset, int] = UNSET
    issuer_dn: Union[Unset, str] = UNSET
    not_before: Union[Unset, int] = UNSET
    revocation_date: Union[Unset, int] = UNSET
    revocation_reason: Union[Unset, CertificateRestResponseV2RevocationReason] = UNSET
    serial_number: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    subject_alt_name: Union[Unset, str] = UNSET
    subject_dn: Union[Unset, str] = UNSET
    subject_key_id: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    type: Union[Unset, int] = UNSET
    udpate_time: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    base_64_cert: Union[Unset, str] = UNSET
    certificate_request: Union[Unset, str] = UNSET
    crl_partition_index: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fingerprint = self.fingerprint
        c_a_fingerprint = self.c_a_fingerprint
        certificate_profile_id = self.certificate_profile_id
        end_entity_profile_id = self.end_entity_profile_id
        expire_date = self.expire_date
        issuer_dn = self.issuer_dn
        not_before = self.not_before
        revocation_date = self.revocation_date
        revocation_reason: Union[Unset, int] = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason.value

        serial_number = self.serial_number
        status = self.status
        subject_alt_name = self.subject_alt_name
        subject_dn = self.subject_dn
        subject_key_id = self.subject_key_id
        tag = self.tag
        type = self.type
        udpate_time = self.udpate_time
        username = self.username
        base_64_cert = self.base_64_cert
        certificate_request = self.certificate_request
        crl_partition_index = self.crl_partition_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if c_a_fingerprint is not UNSET:
            field_dict["cAFingerprint"] = c_a_fingerprint
        if certificate_profile_id is not UNSET:
            field_dict["certificateProfileId"] = certificate_profile_id
        if end_entity_profile_id is not UNSET:
            field_dict["endEntityProfileId"] = end_entity_profile_id
        if expire_date is not UNSET:
            field_dict["expireDate"] = expire_date
        if issuer_dn is not UNSET:
            field_dict["issuerDN"] = issuer_dn
        if not_before is not UNSET:
            field_dict["notBefore"] = not_before
        if revocation_date is not UNSET:
            field_dict["revocationDate"] = revocation_date
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if status is not UNSET:
            field_dict["status"] = status
        if subject_alt_name is not UNSET:
            field_dict["subjectAltName"] = subject_alt_name
        if subject_dn is not UNSET:
            field_dict["subjectDN"] = subject_dn
        if subject_key_id is not UNSET:
            field_dict["subjectKeyId"] = subject_key_id
        if tag is not UNSET:
            field_dict["tag"] = tag
        if type is not UNSET:
            field_dict["type"] = type
        if udpate_time is not UNSET:
            field_dict["udpateTime"] = udpate_time
        if username is not UNSET:
            field_dict["username"] = username
        if base_64_cert is not UNSET:
            field_dict["base64Cert"] = base_64_cert
        if certificate_request is not UNSET:
            field_dict["certificateRequest"] = certificate_request
        if crl_partition_index is not UNSET:
            field_dict["crlPartitionIndex"] = crl_partition_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fingerprint = d.pop("fingerprint", UNSET)

        c_a_fingerprint = d.pop("cAFingerprint", UNSET)

        certificate_profile_id = d.pop("certificateProfileId", UNSET)

        end_entity_profile_id = d.pop("endEntityProfileId", UNSET)

        expire_date = d.pop("expireDate", UNSET)

        issuer_dn = d.pop("issuerDN", UNSET)

        not_before = d.pop("notBefore", UNSET)

        revocation_date = d.pop("revocationDate", UNSET)

        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: Union[Unset, CertificateRestResponseV2RevocationReason]
        if isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = CertificateRestResponseV2RevocationReason(_revocation_reason)

        serial_number = d.pop("serialNumber", UNSET)

        status = d.pop("status", UNSET)

        subject_alt_name = d.pop("subjectAltName", UNSET)

        subject_dn = d.pop("subjectDN", UNSET)

        subject_key_id = d.pop("subjectKeyId", UNSET)

        tag = d.pop("tag", UNSET)

        type = d.pop("type", UNSET)

        udpate_time = d.pop("udpateTime", UNSET)

        username = d.pop("username", UNSET)

        base_64_cert = d.pop("base64Cert", UNSET)

        certificate_request = d.pop("certificateRequest", UNSET)

        crl_partition_index = d.pop("crlPartitionIndex", UNSET)

        certificate_rest_response_v2 = cls(
            fingerprint=fingerprint,
            c_a_fingerprint=c_a_fingerprint,
            certificate_profile_id=certificate_profile_id,
            end_entity_profile_id=end_entity_profile_id,
            expire_date=expire_date,
            issuer_dn=issuer_dn,
            not_before=not_before,
            revocation_date=revocation_date,
            revocation_reason=revocation_reason,
            serial_number=serial_number,
            status=status,
            subject_alt_name=subject_alt_name,
            subject_dn=subject_dn,
            subject_key_id=subject_key_id,
            tag=tag,
            type=type,
            udpate_time=udpate_time,
            username=username,
            base_64_cert=base_64_cert,
            certificate_request=certificate_request,
            crl_partition_index=crl_partition_index,
        )

        certificate_rest_response_v2.additional_properties = d
        return certificate_rest_response_v2

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
