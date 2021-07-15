example_query = """# Cats
SELECT ?item ?itemLabel 
WHERE 
{
 # a triple of item, property and value
  ?item wdt:P31 wd:Q146. # want any items with propery P31 and value Q146 (house cats)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}"""

example_query2 = """# American journalists
SELECT ?item ?itemLabel 
WHERE 
{
  # Item Property Value
  ?item wdt:P31 wd:Q5. # all the items that have instance-of with value human
  ?item wdt:P27 wd:Q30.  # and who are citizens of the US
  ?item wdt:P106 wd:Q1930187. # and who are journalists
  ?item wdt:P19 wd:Q1297 # who have place of birth in Chicago
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}"""

example_query3 = """# Show only 20 American journalists not born in Chicago
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q5. # all the items that have instance-of with value human
  ?item wdt:P27 wd:Q30.  # and who are citizens of the US
  ?item wdt:P106 wd:Q1930187. # and who are journalists
  MINUS {
    ?item wdt:P19 wd:Q1297 # who have place of birth in Chicago
  }
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 20
"""

example_query4 = """# Brazilians who are either poets or novelist, but not both
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q5. # humans
  ?item wdt:P27 wd:Q155.  # citizens of Brazil
  { ?item wdt:P106 wd:Q49757.} # occupation - poet
  UNION 
  { ?item wdt:P106 wd:Q6625963. } # occupation - novelist
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
LIMIT 20
"""