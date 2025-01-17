import glob
from rdflib import Graph

files = glob.glob("./**/*.ttl", recursive=True)

for x in files:
    print(f"Checking {x}")
    g = Graph()
    g.parse(x)

print(f"All {len(files)} ttl-files are well-formed")