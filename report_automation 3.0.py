from simple_salesforce import Salesforce
from simple_salesforce.exceptions import SalesforceMalformedRequest

# Authenticate and connect to the Metadata API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Retrieve the metadata for the reports
report_folder_id = 'your_folder_id' # replace with the ID of the folder you want to move the reports from
new_folder_id = '00l6f000002TZf4AAG' # replace with the ID of the folder you want to move the reports to
reports = sf.query("SELECT Id, DeveloperName, FolderName FROM Report WHERE FolderId = '{}'".format(report_folder_id))

# Update the folder location for each report and save the changes
for report in reports['records']:
    metadata = sf.Report.get(report['DeveloperName']).metadata()
    metadata['folder'] = new_folder_id
    try:
        sf.Report.update(report['DeveloperName'], {'Metadata': metadata})
        print('Report "{}" moved to folder "{}"'.format(report['DeveloperName'], new_folder_id))
    except SalesforceMalformedRequest as e:
        print('Error moving report "{}": {}'.format(report['DeveloperName'], e.content[0]['message']))
