from graph_class import Graph

class ParseError(Exception):
    """Raised when the input map file has invalid structure."""

def parse_map_file(path: str) -> Graph:
    g = Graph()

    try:
        with open(path, "r", encoding="utf-8") as f:        #Opens file
            lines = f.readlines()
    except OSError as e:
        raise ParseError(f"Cannot open file '{path}': {e}") from e    #Checks file

    mode = None  # None | "CITIES" | "ROADS"
    seen_cities = set()

    for idx, raw in enumerate(lines, start=1):  #Loop for file
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if line.upper() == "CITIES":        
            if mode is not None:
                raise ParseError(f"Line {idx}: 'CITIES' section appears more than once or in wrong place.") #Cities comes before Roads
            mode = "CITIES"
            continue

        if line.upper() == "ROADS":
            if mode != "CITIES":
                raise ParseError(f"Line {idx}: 'ROADS' section must come after 'CITIES'.") #Roads comes after Cities
            mode = "ROADS"
            continue

        if mode == "CITIES":    #Inputs Cities
            parts = line.split()
            if len(parts) != 1:
                #raise ParseError(f"Line {idx}: Invalid city name '{line}'.")    #Invailid Name
                print("")
            else:
                city = parts[0]
            if city in seen_cities:
                #raise ParseError(f"Line {idx}: Duplicate city '{city}'.")   #Duplicate Road
                print("")            
            else:
                g.add_node(city)
                seen_cities.add(city)
            

        elif mode == "ROADS":   #Inputs Roads
            parts = line.split()
            if len(parts) != 3:
                raise ParseError(f"Line {idx}: Invalid road line '{line}'.")  #Doesn't have enough information for a road
            src, dest, w_str = parts
            try:
                weight = int(w_str)
            except ValueError:
                raise ParseError(f"Line {idx}: Weight '{w_str}' is not an integer.")    #Not integer
            if src not in g.adj or dest not in g.adj:
                raise ParseError(f"Line {idx}: Road references unknown city '{src}' or '{dest}'.") #City doesn't exist
            if dest in g.adj[src]:
                #raise ParseError(f"Line {idx}: Duplicate edge {src}->{dest}.")  #Duplicate Road
                print("")
            else:
                g.add_edge(src, dest, weight)

        else:
            raise ParseError(f"Line {idx}: Content before 'CITIES' section.")

    if mode is None:
        raise ParseError("File must contain 'CITIES' and 'ROADS' sections.")

    return g