# -*- coding: utf-8 -*-
import argparse
import nmap3 
import json
from fpdf import FPDF 

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--hostname", help="Scan hostname, followed by a domain name or a IP address")
parser.add_argument("-p", "--port", help = "Scan specific port, or many ports", type = int, nargs='+')
parser.add_argument("-filename", help = "Read text file", required = False)
#parser.add_argument("-t", "--tcpscan")

args = parser.parse_args()
hostnames = args.hostname
ports = args.port
filename = args.filename

def get_port_info(ip, res):
    report_list = []
    for i in res[ip]['ports']:
                    report = {}
                    
                    state = i['state']
                    service = i['service']['name']
                    report['type'] = i['protocol']
                    report['port'] = i['portid']
                    report['state'] = state
                    report['service'] = service
                    
                    report_list.append(report)
    return report_list

def output2pdf(content, output_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times', '', 12)
    pdf.multi_cell(0, 5, txt = content)
    pdf.ln()
    pdf.output(output_name) 
    
try:
    nm = nmap3.Nmap()
    
    
#If users specify th port number, the code will filter the port
    
    
    if ports != None:
        result = nm.scan_top_ports(hostnames)
        ip_array = []
        text = ""
        for i in result:
            ip_array.append(i)
            if i == 'stats':
                break
        for k in ip_array:
            report_list = []
            for i in result[k]['ports']:
                
                for j in ports:
                    
                    if j == int(i['portid']):
                        
                        report = {}
                        
                        state = i['state']
                        service = i['service']['name']
                        report['type'] = i['protocol']
                        report['port'] = j
                        report['state'] = state
                        report['service'] = service
                        
                        report_list.append(report)
            txt = "\nhostname:"+ k + '\nports:'+ json.dumps(report_list)
            text += txt
            output2pdf(text, "pdf.pdf")
    		
    elif filename != None:
        report_list = []
        text = ""
        with open(filename) as f:
            ip = f.readline()
        result = nm.scan_top_ports(ip)
        ip_array = []
        for i in result:
            ip_array.append(i)
            if i == 'stats':
                break
        for i in ip_array:
            report_list = get_port_info(i, result)
            txt = "\nhostname: \n" + i + '\nports:'+ json.dumps(report_list)
            text += txt 
            output2pdf(text, "pdf.pdf")
	
		
    else:
        result = nm.scan_top_ports(hostnames)
        ip_array = []
        text = ""
        for i in result:
            ip_array.append(i)
            if i == 'stats':
                break
        
        for i in ip_array:
            report_list = []
            report_list = get_port_info(i, result)
            txt = "\nhostname:"+ i+ '\nports:'+ json.dumps(report_list)
            text += txt
            output2pdf(text, "pdf.pdf")
		    
except Exception as e:
    pass
    
