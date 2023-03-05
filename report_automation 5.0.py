from simple_salesforce import Salesforce


report_id = "00O6f0000086O3kEAE"

# Login to Salesforce API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Query report metadata
headers = {"Content-Type": "application/json", "Accept": "application/json"}
report_metadata = sf.restful("analytics/reports/" + report_id + "/describe", headers=headers, method="GET")
developer_name = report_metadata["reportMetadata"]["developerName"]
folderid = report_metadata["reportMetadata"]["folderId"]
folder_metadata = sf.restful("folders/" + folderid, headers=headers, method="GET")
folder_name = folder_metadata["name"]


print("Report developer name:", developer_name)
print("Folder id:", folderid)
print("Folder developer name:", folder_name)
