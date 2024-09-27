import csv
import pandas as pd
import os
from lxml import etree

file = ''

tree = etree.parse(file)

label = tree.xpath(".//madsrdf:authoritativeLabel/text()", namespaces={'madsrdf': 'http://www.loc.gov/mads/rdf/v1#'})

last_changed = tree.xpath(".//ri:recordChangeDate/text()", namespaces={'ri': 'http://id.loc.gov/ontologies/RecordInfo#'})

data = {'Label': label, 'Last Changed': last_changed}

df = pd.DataFrame.from_dict(data, orient='index').transpose()

with pd.ExcelWriter("term_list.xlsx") as writer:
     df.to_excel(writer, index=False)

print(df)