import re


class MyString:
    
    import re

    def __init__(self, value=""):
        self.value = value  


    def count_sentences(self):
      sentences = re.split(r'(?<=[.!?])\s+', self.value.strip())
      return len([s for s in sentences if s.strip()])

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
      return self.value.endswith("?")
    
    def is_exclamation(self):
      return self.value.endswith("!")
    
    
string = MyString("This is a string! It has three sentences. Right?")
print(string.value)