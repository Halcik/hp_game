
class Family:
  def __init__(self, person, dad=None, mom=None, love=None):
    self.me = person
    self.father = dad
    self.mother = mom
    self.love = love

  def __del__(self):
    del self.me
    del self.father
    del self.mother
    del self.love

  def set_parents(self, mom, dad):
    self.mother = mom
    self.father = dad

  def love(self, my_love):
    self.love = my_love

############################
class Person(Family):
  features = ('chivalry', 'shrewdness', 'intelligence', 'wit', 'creativity', 'patience', 'courage', 'pride', 'learning', 'daring', 'wisdom', 'hard-working', 'just', 'determination', 'modesty', 'ambition', 'nerve', 'cunning', 'acceptance', 'loyalty', 'bravery', 'resourcefulness', 'fairness', 'self-preservation')

  def __init__(self, first_name=None, last_name=None, age=0):
    super().__init__(self)
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.personality = []

  def __del__(self):
    del self.first_name
    del self.last_name
    del self.age


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
  
  @classmethod
  def new_person(cls):
    name = input("First name: ").title()
    l_name = input("Last name: ").title()
    age = input("Age: ")
    if not name or not l_name or name.isalpha()==False or l_name.isalpha()==False:
      print("The character name does not meet the requirements. Make sure that the first name and last name contain only letters")
      return -1
    if age.isnumeric()==False:
      print("Age must be an integer")
      return -1
    age = int(age)
    if age<0:
      return -1
    return cls(name, l_name, age)
  
  @classmethod
  def create_person(cls):
    person = -1
    while person==-1:
      try:
        person = Person().new_person()
        if person==-1:
          raise Exception("Character creation error occurred")
      except Exception:
        print("Try again")
      else:
        print("Successfully created a character")
        return person
  
class School(Person):
  pass

class Student(School):
  Gryff = ('daring', 'nerve', 'chivalry', 'courage', 'bravery', 'determination')
  Slyth = ('cunning', 'ambition', 'resourcefulness', 'determination', 'pride', 'self-preservation', 'shrewdness')
  Huff = ('loyalty', 'just', 'hard-working', 'patience', 'fairness', 'modesty')
  Rav = ('wit', 'learning', 'wisdom', 'acceptance', 'intelligence', 'creativity')

class Topic(School):
  pass

class Teacher(School, Topic):
  pass
if __name__ == '__main__':
  p1 = Person().create_person()
  print(p1)