import json
from pathlib import Path
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Fight Club", "year": 1999}
]


data = json.dumps(movies)
print(data)
Path("movies.json").write_text(data, encoding='utf-8')

file_data = Path("movies.json")
file_data.write_text(data, encoding="utf-8")

read_data = file_data.read_text(encoding="utf-8")

parsed_data = json.loads(read_data)
print(parsed_data)
