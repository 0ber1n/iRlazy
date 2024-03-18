# iRlazy
For starters, big thanks to the Nmap Project for giving us such an amazing enumeration tool.

This script allows the user to input an IP and will run an all port scan of the machine. It then takes the output of the port scan and runs a -sC (Script) and -sV (version) scan against the open ports if found in the first part. The second scan will output in all nmap file types, and will name it with the file name you entered in the beginning.

This is a starter project to learn python and automate some of my HTB testing, so I may expand in the future or make it better somehow.

```script
python3 iRlazy.py
```
