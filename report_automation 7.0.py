import csv
from simple_salesforce import Salesforce

# Login to Salesforce API
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Set up CSV files
input_file = 'input.csv'
output_file = 'output.csv'
fieldnames = ['ID', 'Developer Name', 'Folder Name']

with open(input_file, 'r', encoding='utf-8-sig') as csvfile_in, open(output_file, 'w', newline='', encoding='utf-8') as csvfile_out:
    reader = csv.DictReader(csvfile_in)
    
    # Modify column header to remove BOM character
    reader.fieldnames[0] = reader.fieldnames[0].lstrip('\ufeff')
    
    # Debug statement to print column names
    print('Input CSV file columns:', reader.fieldnames)
    
    writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        report_id = row['id']
        # Query report metadata
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        report_metadata = sf.restful("analytics/reports/" + report_id + "/describe", headers=headers, method="GET")
        developer_name = report_metadata["reportMetadata"]["developerName"]
        folder_id = report_metadata["reportMetadata"]["folderId"]
        folder_metadata = sf.restful("folders/" + folder_id, headers=headers, method="GET")
        folder_name = folder_metadata["name"]
        
        # Write output to CSV file
        writer.writerow({'ID': report_id, 'Developer Name': developer_name, 'Folder Name': folder_name})
        
print('Done writing to output file.')
