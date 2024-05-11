import people

def test_create__first_ready_person(): #wihout family, first
  p1 = people.Person("Anna", "Hill", 36)
  assert p1.first_name=="Anna"
  assert p1.last_name=="Hill"
  assert p1.age==36
  assert p1.mother==None
  assert p1.father==None

def test_create_first_unready_person(): #wihout family, first with
  p1 = people.Person()
  assert p1.first_name==None
  assert p1.last_name==None
  assert p1.age==0
  assert p1.mother==None
  assert p1.father==None

def test_birth_new_person():
  pass

