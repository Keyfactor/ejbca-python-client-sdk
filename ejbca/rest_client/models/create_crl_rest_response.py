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

from ..models.create_crl_rest_response_latest_partition_crl_versions import (
    CreateCrlRestResponseLatestPartitionCrlVersions,
)
from ..models.create_crl_rest_response_latest_partition_delta_crl_versions import (
    CreateCrlRestResponseLatestPartitionDeltaCrlVersions,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateCrlRestResponse")


@attr.s(auto_attribs=True)
class CreateCrlRestResponse:
    """
    Attributes:
        issuer_dn (Union[Unset, str]): Issuer Distinguished Name Example: CN=ExampleCA.
        latest_crl_version (Union[Unset, int]): Latest base CRL version Example: 10.
        latest_delta_crl_version (Union[Unset, int]): Latest delta CRL version Example: 5.
        latest_partition_crl_versions (Union[Unset, CreateCrlRestResponseLatestPartitionCrlVersions]):
        latest_partition_delta_crl_versions (Union[Unset, CreateCrlRestResponseLatestPartitionDeltaCrlVersions]):
        all_success (Union[Unset, bool]):
    """

    issuer_dn: Union[Unset, str] = UNSET
    latest_crl_version: Union[Unset, int] = UNSET
    latest_delta_crl_version: Union[Unset, int] = UNSET
    latest_partition_crl_versions: Union[Unset, CreateCrlRestResponseLatestPartitionCrlVersions] = UNSET
    latest_partition_delta_crl_versions: Union[Unset, CreateCrlRestResponseLatestPartitionDeltaCrlVersions] = UNSET
    all_success: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer_dn = self.issuer_dn
        latest_crl_version = self.latest_crl_version
        latest_delta_crl_version = self.latest_delta_crl_version
        latest_partition_crl_versions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_partition_crl_versions, Unset):
            latest_partition_crl_versions = self.latest_partition_crl_versions.to_dict()

        latest_partition_delta_crl_versions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.latest_partition_delta_crl_versions, Unset):
            latest_partition_delta_crl_versions = self.latest_partition_delta_crl_versions.to_dict()

        all_success = self.all_success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer_dn is not UNSET:
            field_dict["issuer_dn"] = issuer_dn
        if latest_crl_version is not UNSET:
            field_dict["latest_crl_version"] = latest_crl_version
        if latest_delta_crl_version is not UNSET:
            field_dict["latest_delta_crl_version"] = latest_delta_crl_version
        if latest_partition_crl_versions is not UNSET:
            field_dict["latest_partition_crl_versions"] = latest_partition_crl_versions
        if latest_partition_delta_crl_versions is not UNSET:
            field_dict["latest_partition_delta_crl_versions"] = latest_partition_delta_crl_versions
        if all_success is not UNSET:
            field_dict["all_success"] = all_success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuer_dn = d.pop("issuer_dn", UNSET)

        latest_crl_version = d.pop("latest_crl_version", UNSET)

        latest_delta_crl_version = d.pop("latest_delta_crl_version", UNSET)

        _latest_partition_crl_versions = d.pop("latest_partition_crl_versions", UNSET)
        latest_partition_crl_versions: Union[Unset, CreateCrlRestResponseLatestPartitionCrlVersions]
        if isinstance(_latest_partition_crl_versions, Unset):
            latest_partition_crl_versions = UNSET
        else:
            latest_partition_crl_versions = CreateCrlRestResponseLatestPartitionCrlVersions.from_dict(
                _latest_partition_crl_versions
            )

        _latest_partition_delta_crl_versions = d.pop("latest_partition_delta_crl_versions", UNSET)
        latest_partition_delta_crl_versions: Union[Unset, CreateCrlRestResponseLatestPartitionDeltaCrlVersions]
        if isinstance(_latest_partition_delta_crl_versions, Unset):
            latest_partition_delta_crl_versions = UNSET
        else:
            latest_partition_delta_crl_versions = CreateCrlRestResponseLatestPartitionDeltaCrlVersions.from_dict(
                _latest_partition_delta_crl_versions
            )

        all_success = d.pop("all_success", UNSET)

        create_crl_rest_response = cls(
            issuer_dn=issuer_dn,
            latest_crl_version=latest_crl_version,
            latest_delta_crl_version=latest_delta_crl_version,
            latest_partition_crl_versions=latest_partition_crl_versions,
            latest_partition_delta_crl_versions=latest_partition_delta_crl_versions,
            all_success=all_success,
        )

        create_crl_rest_response.additional_properties = d
        return create_crl_rest_response

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
