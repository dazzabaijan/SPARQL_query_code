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

# adding "Label" at the end of a variable will show the variable in its label, instead of a Qcode link.
# to show entries that don't have a birthplace, replace "?item wdt:P19 ?birthplace ." with 
# "OPTIONAL { ?item wdt:P19 ?birthplace .}"
example_query4 = """# Brazilians who are either poets or novelist, but not both and show their birth places
SELECT ?item ?itemLabel ?birthplaceLabel
WHERE 
{
  ?item wdt:P31 wd:Q5. # humans
  ?item wdt:P27 wd:Q155. # citizens of Brazil
  { ?item wdt:P106 wd:Q49757.} # occupation - poet
  UNION 
  { ?item wdt:P106 wd:Q6625963. } # occupation - novelist
  ?item wdt:P19 ?birthplace. # and put the birthplace into a variable
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

example_query5 = """# American politicians whose father was also a politician

# instance of human
# citizenship - US
# occupation - politician
# father - ?father

SELECT ?item ?itemLabel ?fatherLabel
WHERE 
{
  ?item wdt:P31 wd:Q5. # instance of human
  ?item wdt:P27 wd:Q30. # US citizen
  ?item wdt:P106 wd:Q82955. # politician
  ?item wdt:P22 ?father. # who have *a* father
  ?father wdt:P106 wd:Q82955. # who *himself* was a politician
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

example_query5 = """# American politicians whose father was also a politician
# with child born after 1950
# instance of human
# citizenship - US
# occupation - politician
# father - ?father

SELECT ?child ?childLabel ?fatherLabel
WHERE 
{
  ?child wdt:P31 wd:Q5. # instance of human
  ?child wdt:P27 wd:Q30. # US citizen
  ?child wdt:P106 wd:Q82955. # politician
  ?child wdt:P22 ?father. # who have *a* father
  ?father wdt:P106 wd:Q82955. # who *himself* was a politician
  
  ?child wdt:P569 ?dob . # child should have *a* date of birth
  FILTER (YEAR(?dob) > 1950)
  
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""