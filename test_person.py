import people
from unittest import mock
from unittest import TestCase

def test_first_ready_person(): #wihout family, first
  p1 = people.Person("Anna", "Hill", 36)
  assert p1.first_name=="Anna"
  assert p1.last_name=="Hill"
  assert p1.age==36
  assert p1.mother==None
  assert p1.father==None

def test_first_unready_person(): #wihout family, first with
  p1 = people.Person()
  assert p1.first_name==None
  assert p1.last_name==None
  assert p1.age==0
  assert p1.mother==None
  assert p1.father==None

class Test_new_person(TestCase):
  @mock.patch('people.input', create=True)
  def test_good_person(self, mocked_input):
    mocked_input.side_effect = ['july', 'rose', '5']
    result = people.Person().new_person()
    assert result.first_name=='July'
    assert result.last_name=='Rose'
    assert result.age == 5

  @mock.patch('people.input', create=True)
  def test_no_name(self, mocked_input):
    mocked_input.side_effect = ['', '', 0]
    result = people.Person().new_person()
    assert result==-1

  @mock.patch('people.input', create=True)
  def test_number_in_name(self, mocked_input):
    mocked_input.side_effect = ['5', '4', 5]
    result = people.Person().new_person()
    assert result.first_name.isalpha()==True

  @mock.patch('people.input', create=True)
  def test_str_in_age(self, mocked_input):
    mocked_input.side_effect = ['Aka', 'Deka', 'fefs']
    result = people.Person().new_person()
    assert result==-1

  @mock.patch('people.input', create=True)
  def test_negative_age(self, mocked_input):
    mocked_input.side_effect = ['Aka', 'Deka', -10]
    result = people.Person().new_person()
    assert (result.age>0)==True