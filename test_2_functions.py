"""Separate file for test_2 functions"""


import requests, csv


URL = 'https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU'


def get_court_data(url: str) -> dict:

    """Returns court api in json format"""

    try:
        req = requests.get(url)
        return req.json()
    except ConnectionError:
        ConnectionError('Could not fulfil get request')


def get_dx_number(court_data: dict) -> str:

    """Returns court dx_number"""

    if court_data["dx_number"] == 'null':
        return "No dx_number availible."
    else:
        return court_data["dx_number"]


def get_nearest_court(court_data:list[dict]) -> dict:

    """Returns nearest court"""

    return sorted(court_data, key=lambda x: x["distance"])[0]


def filter_court_by_type(court_data: list[dict], court_type: str) -> list[dict]:

    """Filter court data by the court_type"""

    return [court for court in court_data if court_type.title() in court["types"]]


def get_url(postcode: str) -> str:

    """Returns new url with updated postcode"""

    url = f"https://courttribunalfinder.service.gov.uk/search/results.json?postcode={postcode}"

    return url


def loop_through_csv_file():

    with open('./people.csv', mode='r') as f:

        data = csv.reader(f)

        for line in data:
            
            person_name = line[0]
            person_postcode = line[1]
            person_court_type= line[2]
            
            if person_name == 'person_name':
                continue
            else:
                url = get_url(person_postcode)
                try:
                    court_data = get_court_data(url)
                except ConnectionError as Err:
                    print(Err)
                courts_by_type = filter_court_by_type(court_data, person_court_type)
                nearest_court = get_nearest_court(courts_by_type)
                data_to_return = { "person_name": person_name,
                                  "type_of_court": person_court_type,
                                  "home_postcode": person_postcode,
                                  "court_name": nearest_court["name"],
                                  "dx_number": get_dx_number(nearest_court),
                                  "distance": str(nearest_court["distance"]) + 'km'
                                  }
                print(data_to_return)


if __name__ == "__main__":
    loop_through_csv_file()
