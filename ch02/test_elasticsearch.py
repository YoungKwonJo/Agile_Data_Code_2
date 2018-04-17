from pyelasticsearch import ElasticSearch
es = ElasticSearch('http://localhost:9200/')
print(es.search('name:Russell', index='agile_data_science'))
