from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import configargparse

from utils import get_correct_form_word, get_wines, get_years_of_work


def create_parser():
    parser = configargparse.ArgParser(
        "Wines shop app",
        default_config_files=[".env"],
    )
    parser.add_argument(
        "--goods",
        type=str,
        help="Name of file with goods",
        default='wines.xlsx',
        env_var='goods',
    )
    return parser


def render_page(goods):
    env = Environment(
        loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
    )
    template = env.get_template("template.html")
    years_for_work = get_years_of_work()
    return template.render(
        years_of_work=years_for_work,
        year=get_correct_form_word(years_for_work),
        stored_wines=get_wines(goods),
    )


def main():
    args = create_parser().parse_args()
    rendered_page = render_page(args.goods)
    with open("index.html", "w", encoding="utf8") as file:
        file.write(rendered_page)

    with HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler) as server:
        print(f'Serving on 0.0.0.0:8000')
        server.serve_forever()


if __name__ == "__main__":
    main()
