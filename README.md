# Germany Tourism Knowledge Graph Website

A Flask web application for exploring tourism information about Germany using an RDF/OWL knowledge graph and SPARQL queries.

## Features

- Germany overview page
- Northern, Southern, Eastern, and Western Germany regions
- State-level tourism information
- Tourist destinations
- Attractions search by attraction type
- RDF/Turtle knowledge graph queried with SPARQL

## Project structure

```text
.
├── app.py
├── ontology.ttl
├── requirements.txt
├── templates/
│   ├── attraction.html
│   ├── destinations.html
│   ├── eastern_germany.html
│   ├── home.html
│   ├── northern_germany.html
│   ├── regions_main.html
│   ├── search.html
│   ├── southern_germany.html
│   └── western_germany.html
└── query test.ipynb
```

## Requirements

- Python 3.9 or newer
- Flask
- RDFLib

## Run locally

1. Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd <YOUR-REPOSITORY-NAME>
```

2. Create and activate a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the Flask application:

```bash
python app.py
```

5. Open the local address shown by Flask in your browser (normally `http://127.0.0.1:5000/`).

## Knowledge graph

The application loads `ontology.ttl` from the same directory as `app.py`, so the project does not depend on a computer-specific file path.

## SPARQL testing

`query test.ipynb` contains notebook-based query experiments. It is optional for running the website.
