import csv
from simple_salesforce import Salesforce
from tqdm import tqdm

# Salesforce API credentials
sf = Salesforce(username='khurrum.syed@brighthousefinancial.com.fullcopy1',
                password='torontoraptors1234kS!',
                security_token='O2vpuER1zpuC2gRuiT8oiat1',
                domain='test')

# Set up CSV files
input_file = 'input.csv'
output_file = 'package2.xml'
fieldnames = ['name', 'members']

with open(input_file, 'r', encoding='utf-8-sig') as csvfile_in, open(output_file, 'w', newline='', encoding='utf-8') as xmlfile_out:
    reader = csv.DictReader(csvfile_in)
    
    # Modify column header to remove BOM character
    reader.fieldnames[0] = reader.fieldnames[0].lstrip('\ufeff')
    
    # Debug statement to print column names
    print('Input CSV file columns:', reader.fieldnames)
    
    xmlfile_out.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xmlfile_out.write('<Package xmlns="http://soap.sforce.com/2006/04/metadata">\n')
    
    report_names = []
    
    for row in tqdm(reader):
        report_id = row['id']
        # Query report metadata
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        report_metadata = sf.restful("analytics/reports/" + report_id + "/describe", headers=headers, method="GET")

        if "reportMetadata" not in report_metadata:
            continue  # ignore and continue

        developer_name = report_metadata["reportMetadata"]["developerName"]
        folder_id = report_metadata["reportMetadata"]["folderId"]
        
        if folder_id == '00DDE0000043klL2AQ':
            folder_name = 'unfiled$public'
        elif folder_id is None:
            folder_name = 'NOTFOUND'
            developer_name = 'NOTFOUND'
        else:
            folder_metadata = sf.restful("folders/" + folder_id, headers=headers, method="GET")
            folder_name = folder_metadata["name"]
        
        # Add report name to the list
        report_names.append(folder_name + '/' + developer_name)
        
    # Write output to package.xml file
    xmlfile_out.write('    <types>\n')
    xmlfile_out.write('        <name>Report</name>\n')
    for name in report_names:
        xmlfile_out.write('        <members>' + name + '</members>\n')
    xmlfile_out.write('    </types>\n')
    xmlfile_out.write('    <version>43.0</version>\n')
    xmlfile_out.write('</Package>')
        
print('Done writing to package.xml file.')
