import os
from rdflib import Graph, URIRef, RDFS, Literal


def make_types():
    out_file = os.path.join("html", "types", "types.ttl")
    g = Graph()
    id_types = [
        "https://pfp-custom-types/idno/URI/GEONAMES",
        "https://pfp-custom-types/idno/URI/WIKIDATA",
        "https://pfp-custom-types/idno/URL/wikidata",
        "https://pfp-custom-types/idno/URI/PMB",
        "https://pfp-custom-types/idno/URI/GND",
        "https://pfp-custom-types/idno/URL/gnd",
        "https://pfp-custom-types/idno/xml-id",
        "https://pfp-custom-types/idno/URL/auden-musulin-papers",
        "https://pfp-custom-types/idno/URL/thun-korrespondenz",
        "https://pfp-custom-types/idno/URL/pmb",
        "https://pfp-custom-types/idno/URL/schnitzler-kino",
        "https://pfp-custom-types/idno/URL/legalkraus",
        "https://pfp-custom-types/idno/URL/schnitzler-mikrofilme",
        "https://pfp-custom-types/idno/URL/bahr-textverzeichnis",
        "https://pfp-custom-types/idno/URL/oeml",
        "https://pfp-custom-types/idno/URL/geonames",
        "https://pfp-custom-types/idno/URL/freud",
        "https://pfp-custom-types/idno/URL/schnitzler-interviews",
        "https://pfp-custom-types/idno/URL/dritte-walpurgisnacht",
        "https://pfp-custom-types/idno/URL/url",
        "https://pfp-custom-types/idno/URL",
        "https://pfp-custom-types/idno/URL/schnitzler-briefe",
        "https://pfp-custom-types/idno/URL/hanslick-online",
        "https://pfp-custom-types/idno/URL/schnitzler-tagebuch",
        "https://pfp-custom-types/idno/URL/wiengeschichtewiki",
        "https://pfp-custom-types/idno/URL/kaiserin-eleonora",
        "https://pfp-custom-types/idno/URL/brahms-online",
        "https://pfp-custom-types/idno/URL/schnitzler-lektueren",
        "https://pfp-custom-types/idno/URL/bahr-tsn",
        "https://pfp-custom-types/idno/URL/fackel",
        "https://pfp-custom-types/idno/URL/schubert-digital",
        "https://pfp-custom-types/idno/URL/wikipedia",
        "https://pfp-custom-types/idno/URL/oebl",
        "https://pfp-custom-types/idno/URL/schnitzler-bahr",
    ]
    appellation_types = [
        "https://pfp-custom-types/person/persname",
        "https://pfp-custom-types/org/orgname",
        "https://pfp-custom-types/place/placename",
    ]
    for x in appellation_types:
        g.add((URIRef(x), RDFS.label, Literal("appellation type", lang="en")))
    for x in id_types:
        g.add((URIRef(x), RDFS.label, Literal("identifier type", lang="en")))
    g.serialize(out_file)
    print(f"Written to {out_file}")
