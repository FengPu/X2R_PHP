#-*- coding: utf-8 -*-
import requests
import json


url = 'http://localhost/x2r_php/em/mapper.php'
rc = open('../../data/alf.rdf', 'rb').read()

m = {}

#single match testing
em1 = {}
em1['status'] = ''
em1['term'] = ''
em1['lineNumbers'] = ''
em1['originalURI'] = 'http://openisdm.com/MAD/property/longitude'
em1['replacedURI'] = 'http://replace.success1'


#multiple match testing
em2 = {}
em2['status'] = ''
em2['term'] = ''
em2['lineNumbers'] = ''
em2['originalURI'] = 'http://openisdm.com/MAD/facility/FAC073863'
em2['replacedURI'] ='http://replace.success2'


m['metadata'] = []
m['mapping'] = [em1, em2]

mapping = json.dumps(m)

#print '\n', 'the mapping input: \n\n', mapping, '\n\n' 

payload = {'format': 'rdfxml', 'mapping': mapping, 'rdfContent': rc}

r = requests.post(url, data=payload)
result = r.text

print 'the result: \n\n'
print result
