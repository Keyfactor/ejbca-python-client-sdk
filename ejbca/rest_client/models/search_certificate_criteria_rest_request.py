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

from ..models.search_certificate_criteria_rest_request_operation import SearchCertificateCriteriaRestRequestOperation
from ..models.search_certificate_criteria_rest_request_property import SearchCertificateCriteriaRestRequestProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCertificateCriteriaRestRequest")


@attr.s(auto_attribs=True)
class SearchCertificateCriteriaRestRequest:
    """Use one of allowed values as property(see enum values below).
    QUERY - multiplicity [0, 1] - is used to search by SubjectDn, SubjectAn, Username or SerialNr;
    Available STATUS - multiplicity [0, 12] - values are: CERT_ACTIVE, CERT_REVOKED, REVOCATION_REASON_UNSPECIFIED,
    REVOCATION_REASON_KEYCOMPROMISE, REVOCATION_REASON_CACOMPROMISE, REVOCATION_REASON_AFFILIATIONCHANGED,
    REVOCATION_REASON_SUPERSEDED, REVOCATION_REASON_CESSATIONOFOPERATION, REVOCATION_REASON_CERTIFICATEHOLD,
    REVOCATION_REASON_REMOVEFROMCRL, REVOCATION_REASON_PRIVILEGESWITHDRAWN, REVOCATION_REASON_AACOMPROMISE;

    END_ENTITY_PROFILE, CERTIFICATE_PROFILE, CA - multiplicity [0, *) - exact match of the name for referencing End
    Entity Profile, Certificate Profile or CA;
    ISSUED_DATE 'BEFORE' - multiplicity [0, 1] - ISO 8601 Date string;
    ISSUED_DATE 'AFTER' - multiplicity [0, 1] - ISO 8601 Date string;
    EXPIRE_DATE 'BEFORE' - multiplicity [0, 1] - ISO 8601 Date string;
    EXPIRE_DATE 'AFTER' - multiplicity [0, 1] - ISO 8601 Date string;
    REVOCATION_DATE 'BEFORE' - multiplicity [0, 1] - ISO 8601 Date string;
    REVOCATION_DATE 'AFTER' - multiplicity [0, 1] - ISO 8601 Date string.
    UPDATE_TIME 'BEFORE' - multiplicity [0, 1] - ISO 8601 Date string;
    UPDATE_TIME 'AFTER' - multiplicity [0, 1] - ISO 8601 Date string;

        Attributes:
            property_ (Union[Unset, SearchCertificateCriteriaRestRequestProperty]): A search property Example:
                CERTIFICATE_PROFILE.
            value (Union[Unset, str]): A search value. This could be sting value, ISO 8601 Date string, an appropriate
                string name of End Entity Profile or Certificate Profile or CA Example: ENDUSER.
            operation (Union[Unset, SearchCertificateCriteriaRestRequestOperation]): An operation for property on inserted
                value. 'EQUAL' for string, 'LIKE' for string value ('QUERY'), 'BEFORE' or 'AFTER' for date values Example:
                EQUAL.
    """

    property_: Union[Unset, SearchCertificateCriteriaRestRequestProperty] = UNSET
    value: Union[Unset, str] = UNSET
    operation: Union[Unset, SearchCertificateCriteriaRestRequestOperation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_: Union[Unset, str] = UNSET
        if not isinstance(self.property_, Unset):
            property_ = self.property_.value

        value = self.value
        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_ is not UNSET:
            field_dict["property"] = property_
        if value is not UNSET:
            field_dict["value"] = value
        if operation is not UNSET:
            field_dict["operation"] = operation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _property_ = d.pop("property", UNSET)
        property_: Union[Unset, SearchCertificateCriteriaRestRequestProperty]
        if isinstance(_property_, Unset):
            property_ = UNSET
        else:
            property_ = SearchCertificateCriteriaRestRequestProperty(_property_)

        value = d.pop("value", UNSET)

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, SearchCertificateCriteriaRestRequestOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = SearchCertificateCriteriaRestRequestOperation(_operation)

        search_certificate_criteria_rest_request = cls(
            property_=property_,
            value=value,
            operation=operation,
        )

        search_certificate_criteria_rest_request.additional_properties = d
        return search_certificate_criteria_rest_request

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
