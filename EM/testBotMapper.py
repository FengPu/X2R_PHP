#-*- coding: utf-8 -*-
import requests
import json


url = 'http://localhost/x2r_php/em/mapper.php'
rc = open('../../data/alf2.rdf', 'rb').read()

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
em2['replacedURI'] ='http://replace.success2#gentry'

#multiple match testing
em3 = {}
em3['status'] = ''
em3['term'] = ''
em3['lineNumbers'] = ''
em3['originalURI'] = 'http://openisdm.com/MAD/facility/FAC048003_alf#gentry'
em3['replacedURI'] ='http://replace.success3'


m['metadata'] = []
m['mapping'] = [em1, em2, em3]

mapping = json.dumps(m)

#print '\n', 'the mapping input: \n\n', mapping, '\n\n' 

payload = {'format': 'rdfxml', 'mapping': mapping, 'rdfContent': rc}

r = requests.post(url, data=payload)
result = r.text

print 'the result: \n\n'
print result
