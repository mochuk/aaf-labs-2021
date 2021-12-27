class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __getitem__(self, item):
      return self.data[item]

class Tree_list():

  def __init__(self):
    self.storage = {}

  def __getitem__(self, name):
    return self.storage[name]

  def __setitem__(self, key, value):
    tree = Tree(value)
    self.storage[key] = tree
    return f"Tree with name {{value}} appended to tree_list"

class Tree():

    def __init__(self, name):
        self.size = 0
        self.root = None
        self.name = name

    def add(self, to_add):
        node = Node(to_add)
        if self.root == None:
            self.root = node

        else: self.add_node(self.root, node, True)

    def add_node(self, subroot, point, bool):
        if (bool and (point[0] <= subroot[0])):
            if(subroot.left == None):
                subroot.left = point
                self.size +=1
                # print('Went to left')
            else: self.add_node(subroot.left, point, False)

        elif bool:
            if (subroot.right == None):
              subroot.right = point
              self.size += 1
              # print('Went to right')
            else: self.add_node(subroot.right, point, False)

        elif (not bool and (point[1] <= subroot[1])):
            if (subroot.left == None):
              subroot.left = point
              self.size += 1
              # print('Went to left')
            else: self.add_node(subroot.left, point, True)

        elif (not bool):
          if (subroot.left == None):
              subroot.left = point
              self.size += 1
              # print('Went to right')
          else: self.add_node(subroot.right, point, True)
        return f"Alles Gut"

    def contains(self, subroot, value):
      try:
        if subroot.data == value:
          print("Yes, it's here")
        elif subroot.left != None:
          self.contains(subroot.left, value)
        elif subroot.right != None:
          self.contains(subroot.right, value)
        else:
          print("No, it's isn't in tree")
      except AttributeError:
        pass

    def recursive_search(self, point):
      print(point.data)
      if point.right != None:
        self.recursive_search(point.right)
      if point.left != None:
        self.recursive_search(point.left)


# tree_list = Tree_list()
# tree_list['ipt'] = []
#
# tree_list["ipt"].add([5, 10])
# tree_list["ipt"].add([3, 4])
# tree_list["ipt"].add([2, 7])
# tree_list["ipt"].add([1, 4])
# tree_list["ipt"].add([6, 7])
#
# tree_list["ipt"].recursive_search(tree_list["ipt"].root)
# tree_list["ipt"].contains(tree_list['ipt'].root,[5,10])
# # tree.recursive_search(tree.root)
# print(tree.contains(tree.root, [4,3]))

# print(tree.size)
