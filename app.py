from pathlib import Path

from flask import Flask, render_template, request
from rdflib import Graph, Namespace, RDFS
from rdflib.namespace import RDF
app = Flask(__name__)

# Load RDF data from the project directory so the app works after cloning.
BASE_DIR = Path(__file__).resolve().parent
rdf_file_path = BASE_DIR / 'ontology.ttl'
graph = Graph()
graph.parse(rdf_file_path, format='turtle')

# Define the namespaces
onto = Namespace("http://www.kr_paris.com/ontologies/tourism#")
dbo = Namespace("http://dbpedia.org/ontology/")
foaf = Namespace("http://xmlns.com/foaf/0.1/")

@app.route('/')
def home():
    # Query to retrieve data
    query = """
        SELECT ?label ?description ?image ?countryCode ?currency ?timeZone
        WHERE {
            ?country rdf:type dbo:Country ;
                     rdfs:label ?label ;
                     dbo:description ?description ;
                     dbo:image ?image .
            ?countryInfo rdf:type dbo:CountryInfo ;
                          dbo:countryCode ?countryCode ;
                          dbo:currency ?currency ;
                          dbo:timeZone ?timeZone .
        }
    """
    results = graph.query(query, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results
    for row in results:
        label, description, image, countryCode, currency, timeZone = row

    # Pass the data to the template
    return render_template('home.html', label=label, description=description, image=image,
                           countryCode=countryCode, currency=currency, timeZone=timeZone)

@app.route('/regions_main')
def regions_main():
    # Query to retrieve data
    query1 = """
    SELECT ?region ?label ?description ?image ?cultureDescription
    WHERE {
        ?region rdf:type dbo:Region ;
                rdfs:label ?label ;
                dbo:description ?description ;
                dbo:cultureDescription ?cultureDescription;
                foaf:depiction ?image .
        FILTER (?region IN (<http://example.org/places/northern-germany>,
                            <http://example.org/places/southern-germany>,
                            <http://example.org/places/eastern-germany>,
                            <http://example.org/places/western-germany>))
    }
    """
    results = graph.query(query1, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    regions_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image), 'cultureDescription': str(row.cultureDescription),
                     'region_uri': str(row.region)} for row in results]

    # Pass the data to the template
    return render_template('regions_main.html', regions_data=regions_data)


@app.route('/region/<region_name>')
def show_region(region_name):
    # Replace spaces with underscores in the region name
    region_name_safe = region_name.replace(' ', '_')
    
    return render_template(f'{region_name_safe}.html')
   
@app.route('/region/northern_germany')
def northern():
    # Query to retrieve data
    query_north = """
    SELECT ?state ?label ?description ?image
    WHERE {
        ?state rdf:type dbo:State ;
                rdfs:label ?label ;
                dbo:description ?description ;
                foaf:depiction ?image .
        FILTER (?state IN (<http://example.org/places/hamburg> ,
                            <http://example.org/places/bremen>,
                           <http://example.org/places/lower-saxony> ,
                            <http://example.org/places/mecklenburg-vorpommern> ,
                            <http://example.org/places/schleswig-holstein>))
    }
    """
    results = graph.query(query_north, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    regions_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image)} for row in results]

    # Pass the data to the template
    return render_template('northern_germany.html', regions_data=regions_data)

@app.route('/region/eastern_germany')
def eastern():
    # Query to retrieve data
    query_east = """
    SELECT ?state ?label ?description ?image
    WHERE {
        ?state rdf:type dbo:State ;
                rdfs:label ?label ;
                dbo:description ?description ;
                foaf:depiction ?image .
        FILTER (?state IN (<http://example.org/places/brandenburg> ,
                            <http://example.org/places/saxony> ,
                            <http://example.org/places/saxonyAnhalt> ,
                            <http://example.org/places/berlin> ,
                            <http://example.org/places/thuringia>))
    }
    """
    results = graph.query(query_east, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    regions_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image)} for row in results]

   

    # Pass the data to the template
    return render_template('eastern_germany.html', regions_data=regions_data)

@app.route('/region/southern_germany')
def southern():
    # Query to retrieve data
    query_south = """
    SELECT ?state ?label ?description ?image
    WHERE {
        ?state rdf:type dbo:State ;
                rdfs:label ?label ;
                dbo:description ?description ;
                foaf:depiction ?image .
        FILTER (?state IN (<http://example.org/places/bavaria> ,
                            <http://example.org/places/hesse>,
                           <http://example.org/places/rhineland-palatinate> ,
                            <http://example.org/places/baden-wurttemberg>))
    }
    """
    results = graph.query(query_south, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    regions_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image)} for row in results]

    # Pass the data to the template
    return render_template('southern_germany.html', regions_data=regions_data)

@app.route('/region/western_germany')
def western():
    # Query to retrieve data
    # Query to retrieve data
    query_west = """
    SELECT ?state ?label ?description ?image
    WHERE {
        ?state rdf:type dbo:State ;
                rdfs:label ?label ;
                dbo:description ?description ;
                foaf:depiction ?image .
        FILTER (?state IN (<http://example.org/places/saarland> ,
                            <http://example.org/places/northrhinewestphalia>))
                            
    }
    """
    results = graph.query(query_west, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    regions_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image)} for row in results]

    # Pass the data to the template
    return render_template('western_germany.html', regions_data=regions_data)


@app.route('/destinations')
def destinations():
    # Query to retrieve data
    # Query to retrieve data
    query_destinations = """
    SELECT ?destination ?label ?description ?image
    WHERE {
        ?state rdf:type dbo:Destination ;
                rdfs:label ?label ;
                dbo:description ?description ;
                foaf:depiction ?image .
        FILTER (?state IN (<http://example.org/destination/bavarianalps> ,
                            <http://example.org/destination/berchtesgaden> ,
                            <http://example.org/destination/blackForest> ,
                            <http://example.org/destination/cologne> ,
                            <http://example.org/destination/culturaroutes> ,
                            <http://example.org/destination/dresen> ,
                            <http://example.org/destination/frankfurt> ,
                            <http://example.org/destination/heidelberg> ,
                            <http://example.org/destination/neuschwansteincastle> ,
                            <http://example.org/destination/nuremberg> ,
                            <http://example.org/destination/rhinevalley> ,
                            <http://example.org/destination/neuschwansteincastle> ,
                            <http://example.org/destination/nuremberg> ,
                            <http://example.org/destination/rhinevalley> ,
                            <http://example.org/destination/munich> ,                    
                            <http://example.org/destination/rothenburg>))
                            
    }
    """
    results = graph.query(query_destinations, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "foaf": foaf})

    # Extracting data from the query results and storing in a list of dictionaries
    dest_data = [{'label': str(row.label), 'description': str(row.description),
                     'image': str(row.image)} for row in results]

    # Pass the data to the template
    return render_template('destinations.html', dest_data=dest_data)

@app.route('/attraction')
def index():
    return render_template("attraction.html")

@app.route("/search", methods=["POST"])
def search():
    attraction_type = request.form.get("attraction_type")
    
    # Query RDF data to get places based on the selected attraction type
    query = f"""
    SELECT ?place ?label ?description
    WHERE {{
        ?place rdf:type dbo:Attraction ;
               rdfs:label ?label ;
               dbo:description ?description ;
               dbo:hasAttractionType onto:{attraction_type} .
    }}
    """
    results = graph.query(query, initNs={"dbo": dbo, "rdf": RDF, "rdfs": RDFS, "onto": onto})
    # Convert query results to a list of dictionaries
    attractions = [{"label": label, "description": description} for place, label, description in results]
    return render_template("search.html", attractions=attractions)


if __name__ == '__main__':
    app.run(debug=True)