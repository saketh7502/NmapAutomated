# NmapAutomated
# Overview

This Python script is designed to facilitate network scanning using Nmap, process the obtained data in XML format, and generate a CSV file containing relevant information about open ports. The script is written in Python, demonstrating proficiency in programming principles, including modularity, effective file handling, subprocess execution, and XML parsing.

## Features

- **Network Scanning:** Utilizes Nmap to scan a list of IP addresses and generates individual XML files for each scan result.
- **XML File Combination:** Combines multiple XML files into a single XML file for consolidated data.
- **CSV Generation:** Converts the combined XML file into a CSV file, containing information about open ports.

## How to Use
 1.clone the repository
   Install dependencies

 2.Configure Input: Add the IP addresses you want to scan in the ip_addresses.txt file

 3.Run the script: python final.py

 4.Results:
 The individual XML files will be stored in the scan_results directory.
 The combined XML file will be saved as combined_scan_results.xml.
 The CSV file with open port information will be saved as open_ports.csv
