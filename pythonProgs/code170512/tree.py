class BinaryTree:
  def __init__(self, left, right):
    self.left = left
    self.right = right

class MultiwayTree:
  def __init__(self, kids, next=None):
    self.kids = self.val = kids
    self.next = next
    
class Bunch(dict):
  def __init__(self, *args, **kwds):
    super(Bunch, self).__init__(*args, **kwds)
    self.__dict__ = self