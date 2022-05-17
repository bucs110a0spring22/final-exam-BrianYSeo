import requests
import re
class Definition:

  def __init__(self):
    self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

  def definition(self,quote):
    quote_word = re.findall(r'\w+', quote)
    quote_word = quote_word[3]
    print(f'Word selected from the quote is: "{quote_word}."')
    self.api_url = f"{self.api_url}{quote_word}"
    response = requests.get(self.api_url)
    defined = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    return defined