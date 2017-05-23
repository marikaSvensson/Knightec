#By Marika Svensson 170523

#------------------------------------------------
#--------------   NODE    -------------------------
#------------------------------------------------
class Node:
 lft = None
 rgt = None
 lvl = 1                                 # We've added a level...
 
 def __init__(self, key, val):            # initiate with key and value! /constructor
  self.key = key
  self.val = val
#------------------------------------------------
#------------------SKEW------------------------------
#------------------------------------------------  
def skew(node):                           # Basically a right rotation
 if None in [node, node.lft]: return node # No need for a skew
 if node.lft.lvl != node.lvl: return node # Still no need
 
 lft = node.lft                           # The 3 steps of the rotation
 node.lft = lft.rgt
 lft.rgt = node
 return lft                               # Switch pointer from parent
 #------------------------------------------------
 #---------------------SPLIT---------------------------
 #------------------------------------------------
def split(node):                           # Left rotation & level incr.
 if None in [node, node.rgt, node.rgt.rgt]: return node
 if node.rgt.rgt.lvl != node.lvl: return node
 
 rgt = node.rgt
 node.rgt = rgt.lft
 rgt.lft = node
 rgt.lvl += 1                               # This has moved up
 return rgt                                 # This should be pointed to
 #------------------------------------------------
 #--------------------INSERT----------------------------
 #------------------------------------------------
def insert(node, key, val):
 if node is None: return Node(key, val)
 
 if node.key == key: node.val = val
 elif key < node.key:
  node.lft = insert(node.lft, key, val)
 else:
   node.rgt = insert(node.rgt, key, val)
 
 node = skew(node)                          # In case it's backward
 node = split(node)                         # In case it's overfull
 return node
#------------------------------------------------
#------------------end------------------------------
#------------------------------------------------