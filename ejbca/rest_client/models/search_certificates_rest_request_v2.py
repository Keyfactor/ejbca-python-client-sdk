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

from ..models.pagination import Pagination
from ..models.search_certificate_criteria_rest_request import SearchCertificateCriteriaRestRequest
from ..models.search_certificate_sort_rest_request import SearchCertificateSortRestRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchCertificatesRestRequestV2")


@attr.s(auto_attribs=True)
class SearchCertificatesRestRequestV2:
    """
    Attributes:
        pagination (Union[Unset, Pagination]):
        sort (Union[Unset, SearchCertificateSortRestRequest]): Use one of allowed values as property and operation.
            Available propertiesUSERNAME
            ISSUER_DN
            SUBJECT_DN
            EXTERNAL_ACCOUNT_BINDING_ID
            END_ENTITY_PROFILE
            CERTIFICATE_PROFILE
            STATUS
            TAG
            TYPE
            UPDATE_TIME
            ISSUED_DATE
            EXPIRE_DATE
            REVOCATION_DATE

            Available operationsASC
            DESC
        criteria (Union[Unset, List[SearchCertificateCriteriaRestRequest]]): A List of search criteria.
    """

    pagination: Union[Unset, Pagination] = UNSET
    sort: Union[Unset, SearchCertificateSortRestRequest] = UNSET
    criteria: Union[Unset, List[SearchCertificateCriteriaRestRequest]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pagination: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        sort: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sort, Unset):
            sort = self.sort.to_dict()

        criteria: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = []
            for criteria_item_data in self.criteria:
                criteria_item = criteria_item_data.to_dict()

                criteria.append(criteria_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if sort is not UNSET:
            field_dict["sort"] = sort
        if criteria is not UNSET:
            field_dict["criteria"] = criteria

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        _sort = d.pop("sort", UNSET)
        sort: Union[Unset, SearchCertificateSortRestRequest]
        if isinstance(_sort, Unset):
            sort = UNSET
        else:
            sort = SearchCertificateSortRestRequest.from_dict(_sort)

        criteria = []
        _criteria = d.pop("criteria", UNSET)
        for criteria_item_data in _criteria or []:
            criteria_item = SearchCertificateCriteriaRestRequest.from_dict(criteria_item_data)

            criteria.append(criteria_item)

        search_certificates_rest_request_v2 = cls(
            pagination=pagination,
            sort=sort,
            criteria=criteria,
        )

        search_certificates_rest_request_v2.additional_properties = d
        return search_certificates_rest_request_v2

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
