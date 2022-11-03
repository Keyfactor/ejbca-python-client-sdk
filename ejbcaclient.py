# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
import json
from datetime import datetime
import ejbca.rest_client as ejbca
import ejbca.rest_client.api.v2certificate.search_certificates_1 as ejbca_search_certificates_1
import ejbca.rest_client.api.v2certificate.get_certificate_profile_info as ejbca_get_certificate_profile_info
import ejbca.rest_client.api.v2certificate.status_3 as ejbca_status_3
import ejbca.rest_client.api.v1ca.get_latest_crl as ejbca_get_latest_crl
import ejbca.rest_client.api.v1ca.get_certificate_as_pem as ejbca_get_certificate_as_pem
import ejbca.rest_client.api.v1ca.list_cas as ejbca_list_cas
import ejbca.rest_client.api.v1ca.create_crl as ejbca_create_crl
import ejbca.rest_client.api.v1ca.status_1 as ejbca_status_1
import ejbca.rest_client.api.v1ca.import_crl as ejbca_import_crl
import ejbca.rest_client.api.v1ssh.pubkey as ejbca_pubkey
import ejbca.rest_client.api.v1ssh.status_8 as ejbca_status_8
import ejbca.rest_client.api.v2endentity.status_7 as ejbca_status_7
import ejbca.rest_client.api.v2endentity.profile as ejbca_profile
import ejbca.rest_client.api.v2endentity.sorted_search as ejbca_sorted_search
import ejbca.rest_client.api.v2endentity.get_authorized_end_entity_profiles as ejbca_get_authorized_end_entity_profiles
import ejbca.rest_client.api.v1cryptotoken.activate_1 as ejbca_activate_1
import ejbca.rest_client.api.v1cryptotoken.generate_keys as ejbca_generate_keys
import ejbca.rest_client.api.v1cryptotoken.deactivate_1 as ejbca_deactivate_1
import ejbca.rest_client.api.v1cryptotoken.status_5 as ejbca_status_5
import ejbca.rest_client.api.v1cryptotoken.remove_keys as ejbca_remove_keys
import ejbca.rest_client.api.v1ca_management.status as ejbca_status
import ejbca.rest_client.api.v1ca_management.deactivate as ejbca_deactivate
import ejbca.rest_client.api.v1ca_management.activate as ejbca_activate
import ejbca.rest_client.api.v1endentity.search as ejbca_search
import ejbca.rest_client.api.v1endentity.delete as ejbca_delete
import ejbca.rest_client.api.v1endentity.status_6 as ejbca_status_6
import ejbca.rest_client.api.v1endentity.revoke as ejbca_revoke
import ejbca.rest_client.api.v1endentity.add as ejbca_add
import ejbca.rest_client.api.v1endentity.setstatus as ejbca_setstatus
import ejbca.rest_client.api.v1certificate.get_certificates_about_to_expire as ejbca_get_certificates_about_to_expire
import ejbca.rest_client.api.v1certificate.status_2 as ejbca_status_2
import ejbca.rest_client.api.v1certificate.enroll_pkcs_10_certificate as ejbca_enroll_pkcs_10_certificate
import ejbca.rest_client.api.v1certificate.search_certificates as ejbca_search_certificates
import ejbca.rest_client.api.v1certificate.revoke_certificate as ejbca_revoke_certificate
import ejbca.rest_client.api.v1certificate.revocation_status as ejbca_revocation_status
import ejbca.rest_client.api.v1certificate.enroll_keystore as ejbca_enroll_keystore
import ejbca.rest_client.api.v1certificate.certificate_request as ejbca_certificate_request
import ejbca.rest_client.api.v1certificate.finalize_enrollment as ejbca_finalize_enrollment
import ejbca.rest_client.models.extended_information_rest_request_component as ejbca_extended_information_rest_request_component
import ejbca.rest_client.models.pagination_rest_response_component as ejbca_pagination_rest_response_component
import ejbca.rest_client.models.configdump_results as ejbca_configdump_results
import ejbca.rest_client.models.search_certificates_rest_response_v2 as ejbca_search_certificates_rest_response_v2
import ejbca.rest_client.models.end_entity_revocation_rest_request as ejbca_end_entity_revocation_rest_request
import ejbca.rest_client.models.set_end_entity_status_rest_request_token as ejbca_set_end_entity_status_rest_request_token
import ejbca.rest_client.models.end_entity_profile_response as ejbca_end_entity_profile_response
import ejbca.rest_client.models.end_entity_rest_response_token as ejbca_end_entity_rest_response_token
import ejbca.rest_client.models.revoke_status_rest_response as ejbca_revoke_status_rest_response
import ejbca.rest_client.models.ssh_public_key_rest_response as ejbca_ssh_public_key_rest_response
import ejbca.rest_client.models.search_certificates_rest_request as ejbca_search_certificates_rest_request
import ejbca.rest_client.models.certificate_profile_info_rest_response_v2 as ejbca_certificate_profile_info_rest_response_v2
import ejbca.rest_client.models.authorized_ee_ps_rest_response as ejbca_authorized_ee_ps_rest_response
import ejbca.rest_client.models.add_end_entity_rest_request as ejbca_add_end_entity_rest_request
import ejbca.rest_client.models.ca_info_rest_response as ejbca_ca_info_rest_response
import ejbca.rest_client.models.finalize_rest_request as ejbca_finalize_rest_request
import ejbca.rest_client.models.search_end_entities_rest_request as ejbca_search_end_entities_rest_request
import ejbca.rest_client.models.search_certificate_sort_rest_request_operation as ejbca_search_certificate_sort_rest_request_operation
import ejbca.rest_client.models.create_crl_rest_response_latest_partition_delta_crl_versions as ejbca_create_crl_rest_response_latest_partition_delta_crl_versions
import ejbca.rest_client.models.import_crl_multipart_data as ejbca_import_crl_multipart_data
import ejbca.rest_client.models.certificate_rest_response_v2 as ejbca_certificate_rest_response_v2
import ejbca.rest_client.models.enroll_certificate_rest_request as ejbca_enroll_certificate_rest_request
import ejbca.rest_client.models.key_store_rest_request as ejbca_key_store_rest_request
import ejbca.rest_client.models.add_end_entity_rest_request_token as ejbca_add_end_entity_rest_request_token
import ejbca.rest_client.models.expiring_certificates_rest_response as ejbca_expiring_certificates_rest_response
import ejbca.rest_client.models.search_end_entities_sort_rest_request as ejbca_search_end_entities_sort_rest_request
import ejbca.rest_client.models.end_entity_revocation_rest_request_reason_code as ejbca_end_entity_revocation_rest_request_reason_code
import ejbca.rest_client.models.search_end_entity_criteria_rest_request as ejbca_search_end_entity_criteria_rest_request
import ejbca.rest_client.models.search_end_entities_rest_response as ejbca_search_end_entities_rest_response
import ejbca.rest_client.models.search_end_entities_rest_request_v2 as ejbca_search_end_entities_rest_request_v2
import ejbca.rest_client.models.search_certificate_criteria_rest_request as ejbca_search_certificate_criteria_rest_request
import ejbca.rest_client.models.search_end_entities_sort_rest_request_operation as ejbca_search_end_entities_sort_rest_request_operation
import ejbca.rest_client.models.search_end_entities_sort_rest_request_property as ejbca_search_end_entities_sort_rest_request_property
import ejbca.rest_client.models.search_certificate_criteria_rest_request_operation as ejbca_search_certificate_criteria_rest_request_operation
import ejbca.rest_client.models.pagination as ejbca_pagination
import ejbca.rest_client.models.certificate_rest_response_v2_revocation_reason as ejbca_certificate_rest_response_v2_revocation_reason
import ejbca.rest_client.models.search_certificate_criteria_rest_request_property as ejbca_search_certificate_criteria_rest_request_property
import ejbca.rest_client.models.extended_information_rest_response_component as ejbca_extended_information_rest_response_component
import ejbca.rest_client.models.search_end_entity_criteria_rest_request_operation as ejbca_search_end_entity_criteria_rest_request_operation
import ejbca.rest_client.models.create_crl_rest_response_latest_partition_crl_versions as ejbca_create_crl_rest_response_latest_partition_crl_versions
import ejbca.rest_client.models.crl_rest_response as ejbca_crl_rest_response
import ejbca.rest_client.models.search_certificates_rest_request_v2 as ejbca_search_certificates_rest_request_v2
import ejbca.rest_client.models.search_certificate_sort_rest_request_property as ejbca_search_certificate_sort_rest_request_property
import ejbca.rest_client.models.set_end_entity_status_rest_request_status as ejbca_set_end_entity_status_rest_request_status
import ejbca.rest_client.models.crypto_token_key_generation_rest_request as ejbca_crypto_token_key_generation_rest_request
import ejbca.rest_client.models.set_end_entity_status_rest_request as ejbca_set_end_entity_status_rest_request
import ejbca.rest_client.models.search_end_entity_criteria_rest_request_property as ejbca_search_end_entity_criteria_rest_request_property
import ejbca.rest_client.models.create_crl_rest_response as ejbca_create_crl_rest_response
import ejbca.rest_client.models.search_certificate_sort_rest_request as ejbca_search_certificate_sort_rest_request
import ejbca.rest_client.models.rest_resource_status_rest_response as ejbca_rest_resource_status_rest_response
import ejbca.rest_client.models.crypto_token_activation_rest_request as ejbca_crypto_token_activation_rest_request
import ejbca.rest_client.models.certificate_request_rest_request as ejbca_certificate_request_rest_request
import ejbca.rest_client.models.end_entity_rest_response as ejbca_end_entity_rest_response
import ejbca.rest_client.models.finalize_rest_request_response_format as ejbca_finalize_rest_request_response_format
import ejbca.rest_client.models.search_certificates_rest_response as ejbca_search_certificates_rest_response
import ejbca.rest_client.models.ca_infos_rest_response as ejbca_ca_infos_rest_response
import ejbca.rest_client.models.pagination_summary as ejbca_pagination_summary
import ejbca.rest_client.models.certificate_rest_response as ejbca_certificate_rest_response
import ejbca.rest_client.models.end_entity_profile_rest_response as ejbca_end_entity_profile_rest_response
import ejbca.rest_client.models.certificates_rest_response as ejbca_certificates_rest_response
import ejbca.rest_client.models.end_entity_rest_response_status as ejbca_end_entity_rest_response_status

def normalize(arg):
  return None if arg is None else arg.to_dict()

def getJson(filename):
  f = open(filename,"r")
  contents = f.read()
  f.close()
  data = json.loads(contents)
  return data

config = getJson("environment.json")
scheme = config["scheme"]
host = config["host"]
URLBase = config["URLbase"]
token = config["token"]
cert = (config["certPath"], config["keyPath"])
ejbcaclient = ejbca.client.AuthenticatedClient(base_url=f"{scheme}://{host}/{URLBase}",prefix="Basic",token=token,verify_ssl=False)
ejbcaclient.cert = cert

def search_certificates_1_(sync=True, **kwargs):
  if sync:
    return ejbca_search_certificates_1.sync(client=ejbcaclient,**kwargs)

def get_certificate_profile_info_(sync=True, **kwargs):
  if sync:
    return ejbca_get_certificate_profile_info.sync(client=ejbcaclient,**kwargs)

def status_3_(sync=True, **kwargs):
  if sync:
    return ejbca_status_3.sync(client=ejbcaclient,**kwargs)

def get_latest_crl_(sync=True, **kwargs):
  if sync:
    return ejbca_get_latest_crl.sync(client=ejbcaclient,**kwargs)

def get_certificate_as_pem_(sync=True, **kwargs):
  if sync:
    return ejbca_get_certificate_as_pem.sync(client=ejbcaclient,**kwargs)

def list_cas_(sync=True, **kwargs):
  if sync:
    return ejbca_list_cas.sync(client=ejbcaclient,**kwargs)

def create_crl_(sync=True, **kwargs):
  if sync:
    return ejbca_create_crl.sync(client=ejbcaclient,**kwargs)

def status_1_(sync=True, **kwargs):
  if sync:
    return ejbca_status_1.sync(client=ejbcaclient,**kwargs)

def import_crl_(sync=True, **kwargs):
  if sync:
    return ejbca_import_crl.sync(client=ejbcaclient,**kwargs)

def pubkey_(sync=True, **kwargs):
  if sync:
    return ejbca_pubkey.sync(client=ejbcaclient,**kwargs)

def status_8_(sync=True, **kwargs):
  if sync:
    return ejbca_status_8.sync(client=ejbcaclient,**kwargs)

def status_7_(sync=True, **kwargs):
  if sync:
    return ejbca_status_7.sync(client=ejbcaclient,**kwargs)

def profile_(sync=True, **kwargs):
  if sync:
    return ejbca_profile.sync(client=ejbcaclient,**kwargs)

def sorted_search_(sync=True, **kwargs):
  if sync:
    return ejbca_sorted_search.sync(client=ejbcaclient,**kwargs)

def get_authorized_end_entity_profiles_(sync=True, **kwargs):
  if sync:
    return ejbca_get_authorized_end_entity_profiles.sync(client=ejbcaclient,**kwargs)

def activate_1_(sync=True, **kwargs):
  if sync:
    return ejbca_activate_1.sync(client=ejbcaclient,**kwargs)

def generate_keys_(sync=True, **kwargs):
  if sync:
    return ejbca_generate_keys.sync(client=ejbcaclient,**kwargs)

def deactivate_1_(sync=True, **kwargs):
  if sync:
    return ejbca_deactivate_1.sync(client=ejbcaclient,**kwargs)

def status_5_(sync=True, **kwargs):
  if sync:
    return ejbca_status_5.sync(client=ejbcaclient,**kwargs)

def remove_keys_(sync=True, **kwargs):
  if sync:
    return ejbca_remove_keys.sync(client=ejbcaclient,**kwargs)

def status_(sync=True, **kwargs):
  if sync:
    return ejbca_status.sync(client=ejbcaclient,**kwargs)

def deactivate_(sync=True, **kwargs):
  if sync:
    return ejbca_deactivate.sync(client=ejbcaclient,**kwargs)

def activate_(sync=True, **kwargs):
  if sync:
    return ejbca_activate.sync(client=ejbcaclient,**kwargs)

def search_(sync=True, **kwargs):
  if sync:
    return ejbca_search.sync(client=ejbcaclient,**kwargs)

def delete_(sync=True, **kwargs):
  if sync:
    return ejbca_delete.sync(client=ejbcaclient,**kwargs)

def status_6_(sync=True, **kwargs):
  if sync:
    return ejbca_status_6.sync(client=ejbcaclient,**kwargs)

def revoke_(sync=True, **kwargs):
  if sync:
    return ejbca_revoke.sync(client=ejbcaclient,**kwargs)

def add_(sync=True, **kwargs):
  if sync:
    return ejbca_add.sync(client=ejbcaclient,**kwargs)

def setstatus_(sync=True, **kwargs):
  if sync:
    return ejbca_setstatus.sync(client=ejbcaclient,**kwargs)

def get_certificates_about_to_expire_(sync=True, **kwargs):
  if sync:
    return ejbca_get_certificates_about_to_expire.sync(client=ejbcaclient,**kwargs)

def status_2_(sync=True, **kwargs):
  if sync:
    return ejbca_status_2.sync(client=ejbcaclient,**kwargs)

def enroll_pkcs_10_certificate_(sync=True, **kwargs):
  if sync:
    return ejbca_enroll_pkcs_10_certificate.sync(client=ejbcaclient,**kwargs)

def search_certificates_(sync=True, **kwargs):
  if sync:
    return ejbca_search_certificates.sync(client=ejbcaclient,**kwargs)

def revoke_certificate_(sync=True, **kwargs):
  if sync:
    return ejbca_revoke_certificate.sync(client=ejbcaclient,**kwargs)

def revocation_status_(sync=True, **kwargs):
  if sync:
    return ejbca_revocation_status.sync(client=ejbcaclient,**kwargs)

def enroll_keystore_(sync=True, **kwargs):
  if sync:
    return ejbca_enroll_keystore.sync(client=ejbcaclient,**kwargs)

def certificate_request_(sync=True, **kwargs):
  if sync:
    return ejbca_certificate_request.sync(client=ejbcaclient,**kwargs)

def finalize_enrollment_(sync=True, **kwargs):
  if sync:
    return ejbca_finalize_enrollment.sync(client=ejbcaclient,**kwargs)

def search_certificates_1(args):
  return normalize(search_certificates_1_(json_body=ejbca_search_certificates_rest_request_v2.SearchCertificatesRestRequestV2.from_dict(args)))

def sorted_search(args):
  return normalize(sorted_search_(json_body=ejbca_search_end_entities_rest_request_v2.SearchEndEntitiesRestRequestV2.from_dict(args)))

def activate_1(args):
  return normalize(activate_1_(json_body=ejbca_crypto_token_activation_rest_request.CryptoTokenActivationRestRequest.from_dict(args)))

def generate_keys(args):
  return normalize(generate_keys_(json_body=ejbca_crypto_token_key_generation_rest_request.CryptoTokenKeyGenerationRestRequest.from_dict(args)))

def search(args):
  return normalize(search_(json_body=ejbca_search_end_entities_rest_request.SearchEndEntitiesRestRequest.from_dict(args)))

def revoke(args):
  return normalize(revoke_(json_body=ejbca_end_entity_revocation_rest_request.EndEntityRevocationRestRequest.from_dict(args)))

def add(args):
  return normalize(add_(json_body=ejbca_add_end_entity_rest_request.AddEndEntityRestRequest.from_dict(args)))

def setstatus(args):
  return normalize(setstatus_(json_body=ejbca_set_end_entity_status_rest_request.SetEndEntityStatusRestRequest.from_dict(args)))

def enroll_pkcs_10_certificate(args):
  return normalize(enroll_pkcs_10_certificate_(json_body=ejbca_enroll_certificate_rest_request.EnrollCertificateRestRequest.from_dict(args)))

def search_certificates(args):
  return normalize(search_certificates_(json_body=ejbca_search_certificates_rest_request.SearchCertificatesRestRequest.from_dict(args)))

def enroll_keystore(args):
  return normalize(enroll_keystore_(json_body=ejbca_key_store_rest_request.KeyStoreRestRequest.from_dict(args)))

def certificate_request(args):
  return normalize(certificate_request_(json_body=ejbca_certificate_request_rest_request.CertificateRequestRestRequest.from_dict(args)))

def finalize_enrollment(args):
  return normalize(finalize_enrollment_(json_body=ejbca_finalize_rest_request.FinalizeRestRequest.from_dict(args)))
