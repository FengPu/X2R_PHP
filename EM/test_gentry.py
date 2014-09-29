#-*- coding: utf-8 -*-
import requests
import json

'''
json_data=open('../../data/test.mapping')
data = json.load(json_data)
for mapping_entry in data['mapping']:
	print 'replacedURI', mapping_entry['replacedURI']
	print 'originalURI', mapping_entry['originalURI']
'''

rc = open('../../data/sample.rdf', 'rb').read()

mapping = open('../../data/test.mapping', 'rb').read()

payload = {'format': 'rdfxml', 'mapping': mapping, 'rdfContent': rc}

url = 'http://localhost/x2r_php/em/mapper.php'
r = requests.post(url, data=payload)
result = r.text
print 'the result: \n\n'
print result