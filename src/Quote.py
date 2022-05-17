import requests
class Quote:

  def __init__(self):
    self.api_url = "https://animechan.vercel.app/api/random"

  def quote(self):
    response = requests.get(self.api_url)
    return str(response.json()["quote"])