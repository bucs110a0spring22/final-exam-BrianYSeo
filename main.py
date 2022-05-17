from src.Quote import Quote
from src.Definition import Definition

def main():
  q = Quote()
  quote = q.quote()
  print(f'The quote of the day is: "{quote}"')
  d = Definition()
  definition = d.definition(quote)
  print(f'The definition of that word is: "{definition}"')

main()