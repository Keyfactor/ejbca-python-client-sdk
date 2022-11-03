# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
import ejbcaclient
import cryptoOps
import random

def addEndEntity(username,password,subject,ca,profile):
  ejbcaclient.add({"username": username,"password": password,"subject_dn": subject,"ca_name": ca,"certificate_profile_name": "ENDUSER","end_entity_profile_name": profile,"token": "USERGENERATED","account_binding_id": "1234567890"})

def csrEnrollment(subject):
  csr,key = cryptoOps.createCSR(subject)
  username = f'python_client_{random.randrange(100000000,1000000000)}'
  password = f'python_client_{random.randrange(100000000,1000000000)}_{random.randrange(100000000,1000000000)}'
  addEndEntity(username,password,subject,ejbcaclient.config["ca"],ejbcaclient.config["profile"])
  cert = ejbcaclient.certificate_request({"certificate_request":csr,"username":username,"password":password})
  return cert["certificate"],key

