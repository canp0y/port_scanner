# Simple Port Scanner

The basic function of this tool is to do a quick TCP domain/hostname scan. This tool 
supports single/multiple port scanning, range IP scanning and file (txt) scanning.

### Score Earned
87/100

### basic function
1. Allow command-line switches to specify a host and port.
2. Present a simple response to the user.

### Additional function
1. Allow more than one host to be scanned
  * Reading a text file of host IP’s or reading a range from the command line - Doing Both
  * Allowing different ways to specify hosts (subnet mask and range)
2. Allow multiple ports to be specified
3. Traceroute
4. User experience results - A pdf file will be generated


### Input Format
Format Accepted: 
1. 192.168.0.1/24
2. ['192.168.0.1','192.168.0.2'] 
3. 192.168.0.1-255
4. 127.0.0.1

### Example Usage
`usage: scan.py [-h] [-a HOSTNAME] [-p PORT [PORT ...]] [-filename FILENAME]`

optional arguments:

  -h, --help            **show this help message and exit**\
  -a HOSTNAME, --hostname HOSTNAME **Scan hostname, followed by a domain name or a IP address** \
  -p PORT [PORT ...], --port PORT [PORT ...] **Scan specific port, or many ports**\
  -filename FILENAME    **Read text file**
  
  ### Example OutPut
  Command Line: `python3 scan.py -a 127.0.0.1-2`\
  OutPut:
  `hostname:127.0.0.1`\
`ports:[{"type": "tcp", "port": "21", "state": "closed", "service": "ftp"}, {"type": "tcp", "port": "22", "state":
"open", "service": "ssh"}, {"type": "tcp", "port": "23", "state": "closed", "service": "telnet"}, {"type": "tcp",
"port": "25", "state": "open", "service": "smtp"}, {"type": "tcp", "port": "80", "state": "closed", "service":
"http"}, {"type": "tcp", "port": "110", "state": "closed", "service": "pop3"}, {"type": "tcp", "port": "139",
"state": "closed", "service": "netbios-ssn"}, {"type": "tcp", "port": "443", "state": "closed", "service": "https"},
{"type": "tcp", "port": "445", "state": "closed", "service": "microsoft-ds"}, {"type": "tcp", "port": "3389",
"state": "closed", "service": "ms-wbt-server"}]

`hostname:127.0.0.2`\
`ports:[{"type": "tcp", "port": "21", "state": "closed", "service": "ftp"}, {"type": "tcp", "port": "22", "state":
"open", "service": "ssh"}, {"type": "tcp", "port": "23", "state": "closed", "service": "telnet"}, {"type": "tcp",
"port": "25", "state": "closed", "service": "smtp"}, {"type": "tcp", "port": "80", "state": "closed", "service":
"http"}, {"type": "tcp", "port": "110", "state": "closed", "service": "pop3"}, {"type": "tcp", "port": "139",
"state": "closed", "service": "netbios-ssn"}, {"type": "tcp", "port": "443", "state": "closed", "service": "https"},
{"type": "tcp", "port": "445", "state": "closed", "service": "microsoft-ds"}, {"type": "tcp", "port": "3389",
"state": "closed", "service": "ms-wbt-server"}]`
  
  Command Line: `python3 scan.py -a 127.0.0.1-2 -p 80`\
  Output:
  `hostname:127.0.0.1`\
`ports:[{"type": "tcp", "port": 80, "state": "closed", "service": "http"}]
hostname:127.0.0.2
ports:[{"type": "tcp", "port": 80, "state": "closed", "service": "http"}]`

 Command Line: `python3 scan.py -filename ip_address.txt`\
  OutPut:
  `hostname: 142.250.69.196`\
`ports:[{"type": "tcp", "port": "21", "state": "filtered", "service": "ftp"}, {"type": "tcp", "port": "22", "state":
"filtered", "service": "ssh"}, {"type": "tcp", "port": "23", "state": "filtered", "service": "telnet"}, {"type": "tcp",
"port": "25", "state": "filtered", "service": "smtp"}, {"type": "tcp", "port": "80", "state": "open", "service":
"http"}, {"type": "tcp", "port": "110", "state": "filtered", "service": "pop3"}, {"type": "tcp", "port": "139",
"state": "filtered", "service": "netbios-ssn"}, {"type": "tcp", "port": "443", "state": "open", "service": "https"},
{"type": "tcp", "port": "445", "state": "filtered", "service": "microsoft-ds"}, {"type": "tcp", "port": "3389",
"state": "filtered", "service": "ms-wbt-server"}]`

