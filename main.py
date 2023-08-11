from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils import get_correct_form_word, get_wines, get_years_of_work

env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)

file = Path('wines.xlsx')

template = env.get_template("template.html")
years_for_work = get_years_of_work()

rendered_page = template.render(
    years_of_work=years_for_work,
    year=get_correct_form_word(years_for_work),
    stored_wines=get_wines(file),
)

with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
