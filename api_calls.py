import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept":"application/json"}
    response = requests.get(url = url,
                            headers = headers
                            )

    if response.status_code == 200:
        print(f"\nJoke: {response.json().get("joke")}")
    else:
        print(f"Error: {response.status_code}: Could not fetch joke")

def get_country_info():
    country = input("Enter country name:").strip()
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url = url)
    if response.status_code == 200:
        data = response.json()[0]
        print(f"\nCountry: {data['name']['common']}")
        print(f"Capital: {data.get('capital', ['N/A'])[0]}")
        print(f"Region: {data['region']}")
        print(f"Population: {data['population']}")
    else:
        print(f"Could not find country {country}")

def get_cat_fact():
    url = "https://catfact.ninja/fact"
    response = requests.get(url = url)
    if response.status_code == 200:
        print(f"Cat fact: {response.json()['fact']}")
    else:
        print("Cat fact not found")

def get_trivia_question():
    url = "https://opentdb.com/api.php?amount=5"
    try:
        response = requests.get(url = url)
        data = response.json()
        question = data['results'][0]
        print(f"\nTrivia question: {question['question']}")
        print(f"Answer: {question['correct_answer']}")
    except requests.exceptions.RequestException:
        print("Could not find trivia question")

get_trivia_question()