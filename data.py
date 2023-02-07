import requests

parameters = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}
def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    # print(response.status_code)
    data = response.json()
    new_question_data = data["results"]
    # print(new_question_data)
    return new_question_data


question_data = get_questions()