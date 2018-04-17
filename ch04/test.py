from elasticsearch5 import Elasticsearch
ELASTIC_URL='http://localhost:9200/agile_data_science'

es = Elasticsearch(ELASTIC_URL)

#res = es.search(index="agile_data_science", body={"query": {"match": { "Origin": "JFK" }}})
res = es.search( body={"query": { "bool" : { "must":[{ "match": { 'Origin': 'JFK' } }] } }} )
#res = es.search(index="agile_data_science", body={"query": {"bool": {"must": [{"match": {"FlightDate": "2015-01-01"}}, {"match": {"Origin": "JFK"}}]}}} )


print("Got %d Hits:" % res['hits']['total'])
print(res)