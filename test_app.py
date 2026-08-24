from app import add, subtract, multiply


def test_add():
   assert add(2, 3) == 5


def test_subtract():
   assert subtract(5, 2) == 3


def test_multiply():
   assert multiply(3, 3) == 9


if __name__ == "__main__":
   test_add()
   test_subtract()
   test_multiply()
   print("All tests passed!")
