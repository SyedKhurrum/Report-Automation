import csv
from simple_salesforce import Salesforce

# Create the Salesforce instance
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Define the name of the CSV file and the ID column header
csv_filename = 'reports.csv'
id_column_header = 'id'

# Define the ID for the target folder
folder_id = '00l6f000002TZf4AAG'

# Open the CSV file and find the ID column
with open(csv_filename, 'r', encoding='utf-8-sig') as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)
    id_column_index = header_row.index(id_column_header)
    report_ids = [row[id_column_index] for row in reader]

# Move the reports to the target folder
for report_id in report_ids:
    print(f'Moving report {report_id} to folder {folder_id}')
    sf.Report.update(report_id, {'OwnerId': folder_id})
    print(f"Report {report_id} moved to folder {folder_id}")
