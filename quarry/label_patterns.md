# Patterns for rdfs:label

## Lang-tags; to decide
* no lang tags
* always one lang (de or en)
* always two lang
* what to do with unknown

## compute (some) labels
Some labels might be generated via SPARQL?

## [crm:E21_Person](https://ontome.net/class/21/namespace/1)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/person__10228> a crm:E21_Person ;
    rdfs:label "Tintner, Hans"@de .
```
## pattern
> `"last name, first name"`
> `"name"`

## [crm:E53_Place](https://ontome.net/class/51/namespace/1)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/place__332> a crm:E53_Place ;
    rdfs:label "Linz"@de .
```
### pattern
> `"{the name of the place}"`

## [crm:E74_Group](https://ontome.net/class/68/namespace/1)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/org__117961> a ns1:E74_Group ;
    rdfs:label "Le Chat Noir"@de .
```
### pattern
> `"{the name of the group}"`

## [crm:E67_Birth](https://ontome.net/class/61/namespace/1) (via SPARQL?)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/person__10069/birth> a crm:E67_Birth ;
    rdfs:label "Geburt von Stranik, Erwin"@de ;
    crm:P4_has_time-span <https://pmb.acdh.oeaw.ac.at/person__10069/birth/time-span> ;
    crm:P7_took_place_at <https://pmb.acdh.oeaw.ac.at/place__50> ;
    crm:P98_brought_into_life <https://pmb.acdh.oeaw.ac.at/person__10069> .
```
### pattern
> `"Geburt von {rfds:label P98_brought_into_life}"`

## [crm:E69_Death](https://ontome.net/class/63/namespace/1) (via SPARQL?)
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/person__100689/death> a crm:E69_Death ;
    rdfs:label "Tod von Novotny, Johann"@de ;
    crm:P100_was_death_of <https://pmb.acdh.oeaw.ac.at/person__100689> ;
    crm:P4_has_time-span <https://pmb.acdh.oeaw.ac.at/person__100689/death/time-span> .
```
### pattern
> `"Tod von {rdf:rfds:label crm:P100_was_death_of}"`

## [crm:E85_Joining](https://ontome.net/class/78/namespace/188) (via SPARQL?)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .

<https://pmb.acdh.oeaw.ac.at/person__10069/joining/29320/0> a crm:E85_Joining ;
    rdfs:label "Stranik, Erwin joins Neues Wiener Journal"@en ;
    crm:P143_joined <https://pmb.acdh.oeaw.ac.at/person__10069> ;
    crm:P144_joined_with <https://pmb.acdh.oeaw.ac.at/org__29320> ;
    crm:P4_has_time-span <https://pmb.acdh.oeaw.ac.at/person__10069/joining/29320/0/time-span/1921-01-01> .
```
### pattern
> `"{rdfs:label crm:P143_joined } tritt bei { rdfs:label crm:P143_joined }"`

## [sari:SRPC3_in_social_relation](https://docs.swissartresearch.net/schema/#SRPC3_in_social_relation) (via SPARQL?)
### example
```ttl
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix sari: <http://w3id.org/sari#> .

<https://pmb.acdh.oeaw.ac.at/person__13698/Is-engaged-to/person__19758> a sari:SRPC3_in_social_relation ;
    rdfs:label "Kris, Adolf — ist verlobt mit — Bally, Jenny"@de ;
    sari:SRP3_relation_type pfpt:Is-engaged-to ;
    crm:P01_has_domain <https://pmb.acdh.oeaw.ac.at/person__13698> ;
    crm:P02_has_range <https://pmb.acdh.oeaw.ac.at/person__19758> .
```
### pattern
> `"{rdfs:label crm:P01_has_domain } — {rdfs:label SRP3_relation_type} — {crm:P02_has_range}"`

