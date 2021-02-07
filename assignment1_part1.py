 ## Final version of Assignment 1
class ListDivideException(Exception):
  """ raising custom ListDivideException for the listDivide function  """
  pass


def listDivide(numbers, divide=2):
    count = 0
    for eachNum in numbers :
      if (eachNum % divide) == 0:
        count += 1
    return count

def testListDivide():
  try:
    assert listDivide([1,2,3,4,5]) == 2
    assert listDivide([2,4,6,8,10]) == 5
    assert listDivide([30, 54, 63,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1,2,3,4,5], 1) == 5   
    print("All assertions work")        
  except AssertionError as ex:    
    raise ListDivideException("An exception occurred") from ex
    
    
if __name__ == "__main__":
   testListDivide()

