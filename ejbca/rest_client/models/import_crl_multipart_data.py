# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="ImportCrlMultipartData")


@attr.s(auto_attribs=True)
class ImportCrlMultipartData:
    """
    Attributes:
        crl_file (Union[Unset, File]): CRL file in DER format
        crl_partition_index (Union[Unset, int]): CRL partition index
    """

    crl_file: Union[Unset, File] = UNSET
    crl_partition_index: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        crl_file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.crl_file, Unset):
            crl_file = self.crl_file.to_tuple()

        crl_partition_index = self.crl_partition_index

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if crl_file is not UNSET:
            field_dict["crlFile"] = crl_file
        if crl_partition_index is not UNSET:
            field_dict["crlPartitionIndex"] = crl_partition_index

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        crl_file: Union[Unset, FileJsonType] = UNSET
        if not isinstance(self.crl_file, Unset):
            crl_file = self.crl_file.to_tuple()

        crl_partition_index = (
            self.crl_partition_index
            if isinstance(self.crl_partition_index, Unset)
            else (None, str(self.crl_partition_index).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update({})
        if crl_file is not UNSET:
            field_dict["crlFile"] = crl_file
        if crl_partition_index is not UNSET:
            field_dict["crlPartitionIndex"] = crl_partition_index

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _crl_file = d.pop("crlFile", UNSET)
        crl_file: Union[Unset, File]
        if isinstance(_crl_file, Unset):
            crl_file = UNSET
        else:
            crl_file = File(payload=BytesIO(_crl_file))

        crl_partition_index = d.pop("crlPartitionIndex", UNSET)

        import_crl_multipart_data = cls(
            crl_file=crl_file,
            crl_partition_index=crl_partition_index,
        )

        import_crl_multipart_data.additional_properties = d
        return import_crl_multipart_data

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
