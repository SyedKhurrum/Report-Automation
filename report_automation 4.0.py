from simple_salesforce import Salesforce, SalesforceMetadata

# Connect to the Salesforce API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

metadata = SalesforceMetadata(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Define the report ID and the destination folder ID
report_id = '00O6f0000084OmPEAU' # replace with the ID of the report you want to move
folder_id = '00l6f000002TZf4AAG' # replace with the ID of the folder you want to move the report to

# Retrieve the report metadata
metadata = sf.Report.get(report_id).metadata()

# Modify the folder location in the report metadata
metadata['folder'] = folder_id

# Update the report in Salesforce
sf.Report.update(report_id, {'Metadata': metadata})

# Print a message indicating success
print('Report "{}" moved to folder "{}"'.format(report_id, folder_id))
