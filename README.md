[![Check Turtle Files](https://github.com/acdh-oeaw/pfp-schema/actions/workflows/check_ttls.yml/badge.svg)](https://github.com/acdh-oeaw/pfp-schema/actions/workflows/check_ttls.yml)

# pfp-schema
The PFP - [Prosopographic Research Platform](https://www.oeaw.ac.at/acdh/research/dh-research-infrastructure/activities/modelling-humanities-data/pfp-prosopographical-research-platform-austria) Austria serves as an umbrella project for personal research at the Austrian Academy of Sciences (ÖAW) using methods of the Digital Humanities. On this page we publish relevant materials with regard to the overarching dta model. 


## dev

* clone the repo
* (create virtual env e.g. `python -m venv venv`)
* `python scripts/build_static.py` to build the website and convert .ttl stored in anywhere in the `./html` into HTML sites using [pylode](https://github.com/rdflib/pyLODE)


## docker

```bash
docker build -t pfp-schema:latest .
docker run -d -p 5000:5000 --name pfp-schema pfp-schema:latest
```
