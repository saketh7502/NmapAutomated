import subprocess
import xml.etree.ElementTree as ET
import os
import csv

def run_nmap_scan(ip, output_dir):
    output_file = os.path.join(output_dir, f'nmap_scan_{ip}.xml')
    nmap_command = f'nmap -Pn -p 5432,22 -oX {output_file} {ip}'
    subprocess.run(nmap_command, shell=True)

def combine_nmap_xml_files(input_dir, output_file):
    root = ET.Element('nmaprun')

    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            file_path = os.path.join(input_dir, filename)
            tree = ET.parse(file_path)
            root.extend(tree.getroot())

    combined_tree = ET.ElementTree(root)
    combined_tree.write(output_file, encoding='utf-8', xml_declaration=True)

def convert_xml_to_csv(xml_file, csv_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    with open(csv_file, 'w', newline='') as csv_output:
        csv_writer = csv.writer(csv_output)
        csv_writer.writerow(['IP Address', 'Port', 'Port Status'])

        for host in root.findall('.//host'):
            address = host.find('.//address').get('addr')
            for port in host.findall('.//port'):
                port_num = port.get('portid')
                port_status = port.find('.//state').get('state')
                csv_writer.writerow([address, port_num, port_status])

input_file = 'ip_addresses.txt'
output_dir = 'scan_results'
combined_xml_file = 'combined_scan_results.xml'
output_csv_file = 'port_status.csv'

os.makedirs(output_dir, exist_ok=True)

with open(input_file, 'r') as file:
    ip_addresses = file.read().splitlines()

for ip in ip_addresses:
    run_nmap_scan(ip, output_dir)

print("Nmap scans completed, and XML files are saved in the 'scan_results' directory.")

combine_nmap_xml_files(output_dir, combined_xml_file)
print(f"Combined XML file '{combined_xml_file}' created.")

convert_xml_to_csv(combined_xml_file, output_csv_file)
print(f"Combined XML file '{combined_xml_file}' has been converted to CSV: '{output_csv_file}'.")
