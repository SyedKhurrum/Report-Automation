import csv
import logging
from simple_salesforce import Salesforce

# Set up logging
logging.basicConfig(filename='salesforce_debug.log', level=logging.DEBUG)

# Connect to Salesforce with debug logs enabled
sf = Salesforce(username = 'khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token = 'O2vpuER1zpuC2gRuiT8oiat1', domain = 'test')
# Define the name of the CSV file
csv_filename = 'reports.csv'

# Open the CSV file and find the ID column
with open(csv_filename, 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)
    id_column_index = header_row.index('id')
    report_ids = [row[id_column_index] for row in reader]

# Get the ID for the ToBeDeleted folder
folder_name = 'ToBeDeleted'
query = f"SELECT Id FROM Folder WHERE Name = '{folder_name}' AND Type = 'Report'"
result = sf.query(query)
folder_id = str(result['records'][0]['Id'])

# Get a list of all reports in the organization
query = "SELECT Id, OwnerId FROM Report"
result = sf.query(query)
reports = result['records']

# Move the reports to the ToBeDeleted folder
for report in reports:
    if report['Id'] in report_ids:
        print(f'Moving report {report["Id"]} to folder {folder_id}')  # Debugging statement
        sf.Reports.update(report['Id'], {'OwnerId': str(sf.user_id), 'FolderId': folder_id})
        print(f"Report {report['Id']} moved to folder {folder_name}")
