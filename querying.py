# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/

import sys
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"

# ? before a key denotes a variable
# variables within SELECT line gives columns of results
# here it'll show two columns of item and itemLabel
# codes within {} of WHERE set specific conditions of a query 
# we go through wikidata and returns matches of what we specify in the triple
query = """# Cats
SELECT ?item ?itemLabel 
WHERE 
{
 # a triple of item, property and value
  ?item wdt:P31 wd:Q146. # want any items with propery P31 and value Q146 (house cats)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}"""

def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


results = get_results(endpoint_url, query)

for result in results["results"]["bindings"]:
    print(result)
