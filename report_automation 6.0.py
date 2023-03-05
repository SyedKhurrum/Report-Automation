from simple_salesforce import Salesforce


folder_id = "00l6f0000019nsPAAQ"

# Login to Salesforce API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Query report metadata
headers = {"Content-Type": "application/json", "Accept": "application/json"}
folder_metadata = sf.restful("folders/" + folder_id, headers=headers, method="GET")
folder_name = folder_metadata["name"]


print("Report developer name:", folder_name)

