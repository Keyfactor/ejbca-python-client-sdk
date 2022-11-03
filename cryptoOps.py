# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
import cryptography.hazmat.backends as backends

oids = {"C":NameOID.COUNTRY_NAME, "CN":NameOID.COMMON_NAME, "E":NameOID.EMAIL_ADDRESS, "L":NameOID.LOCALITY_NAME, "O":NameOID.ORGANIZATION_NAME, "OU":NameOID.ORGANIZATIONAL_UNIT_NAME, "S":NameOID.STATE_OR_PROVINCE_NAME}
backend = backends.default_backend()

def genRSAKeypair(keySize):
  return rsa.generate_private_key(public_exponent=65537,key_size=keySize,backend=backend)

def getRSAPrivateKey(keypair):
  bstr = keypair.private_bytes(serialization.Encoding.PEM, encryption_algorithm = serialization.NoEncryption(), format=serialization.PrivateFormat.PKCS8)
  return str(bstr.decode("UTF-8")).replace("\\n","\n")

def buildSubject(DN):
  return x509.Name([x509.NameAttribute(oids[rdn[0]],rdn[1]) for rdn in map(lambda x: x.split('='),DN.split(','))])

def buildDNSSans(domains):
  return x509.SubjectAlternativeName([x509.DNSName(d) for d in domains])

def getPublicBytes(CSR):
  return str(CSR.public_bytes(serialization.Encoding.PEM).decode("UTF-8")).replace("\\n","\n")

def getThumbprint(pem):
  return x509.load_pem_x509_certificate(pem.encode("UTF-8"),backend=backend).fingerprint(hashes.SHA1()).hex()

def createCSR(DN,domainSANs=[],keySize=2048):
  csrBuilder = x509.CertificateSigningRequestBuilder().subject_name(buildSubject(DN)).add_extension(buildDNSSans(domainSANs),critical=False)
  key = genRSAKeypair(keySize)
  csr = csrBuilder.sign(key, hashes.SHA256(),backend=backend)
  return (getPublicBytes(csr),getRSAPrivateKey(key))

