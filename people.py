import pyinputplus as pyip

class Person:

  def __init__(self, first_name=None, last_name=None, age=0, mother=None, father=None):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.mother = mother
    self.father = father
    self.love = None

  def __del__(self):
    del self.first_name
    del self.last_name
    del self.age
    del self.mother
    del self.father
    del self.love

  def __str__(self):
    information = f"\n~~~ Info about {self.first_name} {self.last_name} ~~~:\nAge: {self.age}"
    if self.love is None:
      information+=f"\nLove: in the future..."
    else:
      information+=f"\nLove: {self.love}"

    if self.mother is None and self.father is None:
      information+="\nParents: unknown"
    elif self.mother is None:
      information+=f"\nParent: {self.father} {self.last_name}"
    elif self.father is None:
      information+=f"\nParent: {self.mother} {self.last_name}"
    else:
      information+=f"\nParents: {self.mother} and {self.father} {self.last_name}"
    return information
  
  def give_me_name(self, f_name, l_name):
    self.first_name = f_name
    self.last_name = l_name

  def set_parents(self, mom, dad):
    self.mother = mom
    self.father = dad

  def i_love(self, my_love):
    self.love = my_love
  
  @classmethod
  def new_person(cls):
    name = pyip.inputStr(prompt="First name: ", blockRegexes=[r"[0-9]"]).title()
    l_name = pyip.inputStr(prompt="Last name: ", blockRegexes=[r"[0-9]"]).title()
    age = pyip.inputInt(prompt="Age: ", min=0, max=200)
    return cls(name, l_name, age)
  
p1 = Person().new_person()
print(p1)

