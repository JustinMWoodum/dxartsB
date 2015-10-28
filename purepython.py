from meaningcloudkey import MEANINGCLOUD_KEY

print MEANINGCLOUD_KEY

'''

import requests
import json

# We define the variables need to call the API
api = 'http://api.meaningcloud.com/sentiment-2.0'
txt = '<<<your text>>>'
model = 'general_es' # general_es / general_es / general_fr

# We make the request and parse the response
parameters = {'key': key,'model': model, 'txt': txt, 'src': 'sdk-python-2.0'}
r = requests.post(api, params=parameters)
response = r.content
response_json = json.loads(response)

# Show the response
print "Response"
print "================="
print response
print "\n"

# Prints the global sentiment values
print "Sentiment: "
print "==========="

try:
  if response_json['score_tag'] != '':
    print 'Global sentiment: ' + response_json['score_tag'] +' (' + response_json['agreement'] + ')'
    print 'Subjectivity: ' + response_json['subjectivity']
    print 'Irony: ' + response_json['irony']
    print 'Confidence: ' + response_json['confidence']
  else:
    print "Not found"
except KeyError:
  print "Not found"

try:
  if len(response_json['sentimented_entity_list']) > 0:
    print "\nEntities"
    print "==========="
    entities = response_json['sentimented_entity_list']
    for index in range(len(entities)):
      output = ''
      output += ' - ' + entities[index]['form']
      try:
        output += ' (' + entities[index]['type'] + ')'
      except KeyError:
        pass
      print output
except KeyError:
  pass

try:
  if len(response_json['sentimented_concept_list']) > 0:
    print "\nConcepts"
    print "==========="
    concepts = response_json['sentimented_concept_list']
    for index in range(len(concepts)):
      output = ''
      output += ' - ' + concepts[index]['form']
      try:
        output += ' (' + concepts[index]['type'] + ')'
      except KeyError:
        pass
      print output
except KeyError:
  pass

print "\n"

'''