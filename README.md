# ipsniffer-corgi
A python script to automate criminalip.io queries for finding origin IPs of web servers.
 
​
## Introduction:
Many companies and organizations often leave their internal IP addresses exposed when accessing their websites, which makes them vulnerable to DDoS attacks. ipsniffer-corgi can help identify the original IP addresses of exposed web servers and mitigate security vulnerabilities. This tool automates criminalip.io to find vulnerable internal IPs.
​
​
​
# Prerequisites
​
* criminalip.io API Key
​
   Get it [here](https://www.criminalip.io/)
​
​
​
# Installation
​
Clone repository:
​
```
$ git clone https://github.com/KamilDogo/ipsniffer-corgi.git
```
​
```
$ cd web-server-ip
```
​
```
$ python3 -m venv .venv
$ source .venv/bin/activate
```
​
```
$ pip3 install -r requirements.txt
```
​
​
## Run:
​
	$ python3 ipx.py --K  [your-criminalip-api-key] --S apache    
​
​
## Usage  
```  
$ python ipx.py --K  [your-criminalip-api-key] --S apache  
```     
​
## Optional Arguments 
​
-K/--key	API key	-K [your-criminalip-api-key]
-S/--query	query	-S apache
​
# Feedback
Feedback welcome!