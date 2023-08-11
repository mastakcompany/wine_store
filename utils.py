import collections
import datetime
import pandas as pd

YEAR_OF_ESTABLISHMENT = 1920


def get_years_of_work():
    current_year = datetime.datetime.now().year
    return current_year - YEAR_OF_ESTABLISHMENT


def get_correct_form_word(year):
    last_digit = year % 10
    last_two_digit = year % 100

    if 10 <= last_two_digit <= 19:
        return "лет"
    elif last_digit == 1:
        return "год"
    elif last_digit in (2, 3, 4):
        return "года"
    else:
        return "лет"


def get_wines(file):
    stored_wines = collections.defaultdict(list)
    excel_data = pd.read_excel(file, na_values=["N/A", "NA"], keep_default_na=False)
    for index, row in excel_data.iterrows():
        category = row["Категория"]
        details = {
            "Картинка": row["Картинка"],
            "Категория": category,
            "Название": row["Название"],
            "Сорт": row["Сорт"],
            "Цена": row["Цена"],
            "Акция": row["Акция"],
        }
        stored_wines[category].append(details)
    return stored_wines
