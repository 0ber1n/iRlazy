import subprocess
import re

def extract_ports_from_file(content):
    # Use regular expression to find port numbers
    port_matches = re.findall(r'(\d+)/tcp\s+open\s+\w+', content)

    # Extract the port numbers and remove spaces
    port_numbers = [match.replace(" ", "") for match in port_matches]

    return port_numbers

# Prompt the user to enter an IP address
ip_input = input("Enter the IP address to scan: ")

# Prompt the user to enter the name of the victim
vic_name = input("What is the name of the victim? ");
file_name = "-oA " + vic_name;


# Run nmap command to scan for open ports and write output to a text file
with open("nmap_output.txt", "w") as output_file:
    process = subprocess.Popen(["nmap", "-n", "-Pn","-p-", "--min-rate=1000", "-T4", ip_input], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            output_file.write(output)
            output_file.flush()

# Read the content of the file
with open("nmap_output.txt", "r") as file:
    nmap_output = file.read()

# Extract port numbers from nmap output
ports = extract_ports_from_file(nmap_output)

# Check if ports were found
if not ports:
    print("Error: No ports found.")
    exit(1)

print("Ports:", ports)

# Run nmap with the discovered ports
subprocess.run(["nmap", "-n", "-Pn","-p", ",".join(ports), "-sC", "-sV", ip_input, file_name])
