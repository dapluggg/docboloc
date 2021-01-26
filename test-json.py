import json
import pprint


with open('clauses-db.json') as f:
    data = json.load(f)

pprint.pprint(data['foreword']['text'])