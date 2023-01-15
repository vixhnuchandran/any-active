#!/usr/bin/env python3
# twitter https://twitter.com/callmelokzy
#linkedin https://www.linkedin.com/in/callmelokzy/


import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", help="Path of the file containing the list of subdomains/urls")
parser.add_argument("-u", "--url", help="URL to check")
parser.add_argument("-dir", "--directory", help="directory path to save the output files")
args = parser.parse_args()

print(''''\033[1;32m'
    ╔═══╗         ╔═══╗     ╔╗               
    ║╔═╗║         ║╔═╗║    ╔╝╚╗              
    ║║ ║║╔═╗ ╔╗ ╔╗║║ ║║╔══╗╚╗╔╝╔╗╔╗╔╗╔══╗    
    ║╚═╝║║╔╗╗║║ ║║║╚═╝║║╔═╝ ║║ ╠╣║╚╝║║╔╗║    
    ║╔═╗║║║║║║╚═╝║║╔═╗║║╚═╗ ║╚╗║║╚╗╔╝║║═╣    
    ╚╝ ╚╝╚╝╚╝╚═╗╔╝╚╝ ╚╝╚══╝ ╚═╝╚╝ ╚╝ ╚══╝    
\033[1;34m       v0.1\033[1;32m  ╔═╝║     \033[1;34mBy Lokzy\033[1;32m                       
             ╚══╝     
''')




if args.directory:
    if not os.path.exists(args.directory):
        os.makedirs(args.directory)

if args.url:

    try:
        response = requests.get(args.url, timeout=5)
        status_code = response.status_code
        print(f"Status code: {status_code}")
        print(f"Server: {response.headers.get('Server')}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Content-Length: {response.headers.get('Content-Length')}")

        if 400 <= status_code < 500:
            if args.directory:
                with open(args.directory+"/clienerror_4xx.txt", "a") as file:
                    file.write(args.url + "\n")
                print(f"{args.url} is saved in {args.directory}/clienerror_4xx.txt file.")
            else:
                with open("clienerror_4xx.txt", "a") as file:
                    file.write(args.url + "\n")
                print(f"{args.url} is saved in clienerror_4xx.txt file in current directory.")

    except Exception:
        pass

elif args.list:
    with open(args.list, "r") as file:
        subdomains = file.read().splitlines()

    succesful_2xx = []
    redirection_3xx = []
    clienerror_4xx = []
    servererror_5xx = []

    for subdomain in subdomains:
        try:
            response = requests.get("http://" + subdomain, timeout=5)
            status_code = response.status_code
            if 200 <= status_code < 300:
                succesful_2xx.append(f'{status_code} : {subdomain}')
            elif 300 <= status_code < 400:
                redirection_3xx.append(f'{status_code} : {subdomain}')
            elif 400 <= status_code < 500:
                clienerror_4xx.append(f'{status_code} : {subdomain}')
            elif 500 <= status_code < 600:
                servererror_5xx.append(f'{status_code} : {subdomain}')

        except:
            pass

    if args.directory:
        with open(args.directory + "/succesful_2xx.txt", "w") as file:
            for subdomain in succesful_2xx:
                file.write(subdomain + "\n")
    else:
        with open("succesful_2xx.txt", "w") as file:
            for subdomain in succesful_2xx:
                file.write(subdomain + "\n")
    print(f"{len(succesful_2xx)}  found with 2xx status codes.")

    if args.directory:
        with open(args.directory + "/redirection_3xx.txt", "w") as file:
            for subdomain in redirection_3xx:
                file.write(subdomain + "\n")
    else:
        with open("redirection_3xx.txt", "w") as file:
            for subdomain in redirection_3xx:
                file.write(subdomain + "\n")
    print(f"{len(redirection_3xx)} found with 3xx status codes.")

    if args.directory:
        with open(args.directory + "/clienerror_4xx.txt", "w") as file:
            for subdomain in clienerror_4xx:
                file.write(subdomain + "\n")
    else:
        with open("clienerror_4xx.txt", "w") as file:
            for subdomain in clienerror_4xx:
                file.write(subdomain + "\n")
    print(f"{len(clienerror_4xx)} found with 4xx status codes.")

    if args.directory:
        with open(args.directory + "/servererror_5xx.txt", "w") as file:
            for subdomain in servererror_5xx:
                file.write(subdomain + "\n")
    else:
        with open("servererror_5xx.txt", "w") as file:
            for subdomain in servererror_5xx:
                file.write(subdomain + "\n")

    print(f"{len(succesful_2xx)}  found with 2xx status codes.")
    print(f"{len(redirection_3xx)} found with 3xx status codes.")
    print(f"{len(clienerror_4xx)} found with 4xx status codes.")
    print(f"{len(servererror_5xx)} found with 5xx status codes.")

    if args.directory:
        print(f"Results are saved under \"{args.directory}\" directory.")

