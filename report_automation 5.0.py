import json
import logging
from simple_salesforce import Salesforce

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Connect to the Salesforce API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')
# Define the report ID and the destination folder ID
report_id = '00O6f0000084OmPEAU' # replace with the ID of the report you want to move
folder_id = '00l6f000002TZf4AAG' # replace with the ID of the folder you want to move the report to

# Retrieve the report metadata
logging.debug('Retrieving report metadata for report {}'.format(report_id))
report_metadata = sf.mdapi.Report.read(report_id)

# Modify the folder location in the report metadata
logging.debug('Updating folder location for report {} to folder {}'.format(report_id, folder_id))
report_metadata['folder'] = folder_id

# Update the report in Salesforce using the Metadata API
try:
    logging.debug('Updating report metadata in Salesforce')
    sf.metadata.update('Report', json.dumps(report_metadata))
except Exception as e:
    logging.error('Error updating report metadata: {}'.format(e))
    raise

# Print a message indicating success
print('Report "{}" moved to folder "{}"'.format(report_id, folder_id))
