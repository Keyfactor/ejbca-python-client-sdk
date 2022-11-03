# Copyright 2022 Keyfactor                                                   
# Licensed under the Apache License, Version 2.0 (the "License"); you may    
# not use this file except in compliance with the License.  You may obtain a 
# copy of the License at http://www.apache.org/licenses/LICENSE-2.0.  Unless 
# required by applicable law or agreed to in writing, software distributed   
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES   
# OR CONDITIONS OF ANY KIND, either express or implied. See the License for  
# thespecific language governing permissions and limitations under the       
# License. 
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
import os

apiRoot = f'{os.getcwd()}/ejbca/rest_client/api'
dirs = [f for f in os.listdir(apiRoot) if not os.path.isfile(os.path.join(apiRoot,f))]
calls = {tag:[f for f in os.listdir(os.path.join(apiRoot,tag)) if f[-3:] == ".py" and '__' not in f] for tag in dirs}
files = [os.path.join(os.path.join(apiRoot,tag),f) for tag in calls for f in calls[tag]]

def getFile(filename):
  f = open(filename,"r")
  contents = f.read()
  f.close()
  return contents

def writeFile(filename, contents):
  f = open(filename,"w")
  f.write(contents)
  f.close()

def addSyncMethod(contents):
  if "def sync(" in contents:
    return contents
  contents = contents.replace("def sync_detailed", "class EmptyResponse:\n  def to_dict(self):\n    return None\ndef sync")
  contents = contents.replace("_build_response(response=response)","_build_response(response=response).parsed")
  contents = contents.replace("parsed=None","parsed=EmptyResponse()")
  return contents if "def sync(" in contents else contents.replace("def sync_detailed", "def sync").replace("_build_response(response=response)","_build_response(response=response).parsed")

def addCertAuth(contents):
  return contents.replace("httpx.request(\n        verify=client.verify_ssl","httpx.request(\n        cert=client.cert,\n        verify=client.verify_ssl")

def adjustContents(contents):
  contents = addSyncMethod(contents)
  contents = addCertAuth(contents)
  return contents

def updateCalls():
  [writeFile(f,adjustContents(getFile(f))) for f in files]

updateCalls()
