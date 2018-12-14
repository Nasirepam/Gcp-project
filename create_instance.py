from terrascript import Terrascript, provider
from python_terraform import *
from terrascript.google.r import google_compute_instance
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/home/nasiruddin_happy/ns002p/service_account.json')
ts = Terrascript()

ts += provider('google', credentials='/home/nasiruddin_happy/ns002p/service_account.json', project='learn-internal', region='us-central1')
inst = ts.add(
        google_compute_instance(
	    'test-vm', 	
            name='test-nasir1-tft', 
            boot_disk=[{'initialize_params':[{'image':'debian-cloud/debian-9'}]}], 
            network_interface=[{'network':'default', 'access_config':{} }], 
            machine_type='n1-standard-1', 
            zone='us-east1-b'))

print(ts.dump())

file = open("/home/nasiruddin_happy/ns002p/template/terraform/sample.tf.json", "w")
file.write(ts.dump())
file.close()

tf = Terraform(working_dir='/home/nasiruddin_happy/ns002p/template/terraform')
tf.init()
approve = {"auto-approve": True}
print(tf.plan())
print(tf.apply(**approve))

