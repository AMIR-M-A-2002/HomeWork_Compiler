from antlr4 import InputStream, ParseTreeWalker
from PasswordLexer import PasswordLexer
from PasswordListener import PasswordListener
from PasswordParser import PasswordParser

def set_and_check_password():
  """
  Sets a password and then checks if user input matches it.

  Returns:
    True if the user input matches the password, False otherwise.
  """
  # Set the password
  password = input("Enter your password to set: ")

  # Create input stream and parser for user input
  user_input_stream = InputStream(input("Enter your password to check: "))
  parser = PasswordParser(user_input_stream)

  # Parse the input
  try:
    tree = parser.password()
  except Exception:
    return False

  # Create a walker and listener to check the parse tree and password match
  listener = MatchPasswordListener(password)
  walker = ParseTreeWalker()
  walker.walk(listener, tree)

  # Return the result from the listener
  return listener.is_match

class MatchPasswordListener(ParseTreeWalker):
  """
  Custom listener to check if user input matches the set password.
  """

  def __init__(self, password):
    self.password = password
    self.is_match = True

  def enterChars(self, ctx):
    # Check if characters in user input match the set password
    for i, child in enumerate(ctx.children):
      if child.type != self.password[i].type:
        self.is_match = False
        break

# Example usage
if set_and_check_password():
  print("Password correct!")
else:
  print("Invalid password! Please try again.")

