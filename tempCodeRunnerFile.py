import csv
from simple_salesforce import Salesforce


# Create the Salesforce instance
sf = Salesforce(username = 'khurrum.syed@brighthousefinancial.com.fullcopy1', password='torontoraptors1234kS!', security_token = 'O2vpuER1zpuC2gRuiT8oiat1', domain = 'test')

# Define the name of the CSV file and the ID column header
csv_filename = 'reports.csv'
id_column_header = 'id'

# Define the name of the target folder
folder_name = 'ToBeDeleted'

# Open the CSV file and find the ID column
with open(csv_filename, 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)
    id_column_index = header_row.index(id_column_header)
    report_ids = [row[id_column_index] for row in reader]

# Get the ID for the target folder
query = f"SELECT Id FROM Folder WHERE Name = '{folder_name}' AND Type = 'Report'"
result = sf.query(query)
folder_id = result['records'][0]['Id']

# Get a list of all reports in the organization
query = "SELECT Id, OwnerId FROM Report"
result = sf.query(query)
reports = result['records']

# Move the reports to the target folder
for report in reports:
    if report['Id'] in report_ids:
        print(f'Moving report {report["Id"]} to folder {folder_id}')  # Debugging statement
        sf.Report.update(report['Id'], {'OwnerId': str(sf.user_id), 'FolderId': str(folder_id)})
        report_url = f'{sf.base_url[:-1]}/analytics/report/{report["Id"]}'
        print(f"Report {report['Id']} moved to folder {folder_name}. URL: {report_url}")
