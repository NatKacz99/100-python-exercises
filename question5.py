class EnterString:
  def get_string(self):
    self.enteredText = input()

  def print_string(self):
    self.printedString = self.enteredText.upper() 
    print(self.printedString)

enteredString = EnterString()
enteredString.get_string()
enteredString.print_string()