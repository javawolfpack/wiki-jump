from math import log

"""
Initial adapted from code found here under MIT License

https://github.com/laurentluce/python-algorithms
"""

class Node:
    def __init__(self, url):
        self.url = url
        self.parsed = False
        self.links = []

    def add_link(self, node):
        self.links = self.links + [node]

    def get_links(self):
        return self.links

    def set_parsed(self):
        self.parsed = True

    def get_parsed(self):
        return self.parsed

    def __gt__(self, node):
        return self.url > node.url

    def __lt__(self, node):
        return self.url < node.url

    def __str__(self):
        return self.url




class BT:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = BT(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = BT(data)
            else:
                self.right.insert(data)

    def find_parsed(self, depth=0):
        if not self.data.get_parsed():
            return self.data
        else:
            if not self.left is None:
                if self.left.find_parsed(depth) is None:
                    if not self.right is None:
                        return self.right.find_parsed(depth)
                    else:
                        return None
                else: 
                    return self.left.find_parsed(depth)
            elif not self.right is None:
                return self.right.find_parsed(depth)
            else:
                return None



    def lookup(self, url, parent=None):
        """
        Lookup node containing data

        @param url node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if url < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(url, self)
        elif url > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(url, self)
        else:
            return url.url

    def delete(self, data):
        """
        Delete node containing data

        @param data node's content to delete
        """
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                # if node has no children, just remove it
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                # if node has 1 child
                # replace node by its child
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                del node
            else:
                # if node has 2 children
                # find its successor
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right

    def compare_trees(self, node):
        """
        Compare 2 trees

        @param node tree to compare
        @returns True if the tree passed is identical to this tree
        """
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)
        if res is False:
            return False
        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res
                
    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print self.data,
        if self.right:
            self.right.print_tree()

    def tree_data(self):
        """
        Generator to get the tree nodes data
        """
        # we use a stack to traverse the tree in a non-recursive way
        stack = []
        node = self
        while stack or node: 
            if node:
                stack.append(node)
                node = node.left
            else: # we are returning so we pop the node and we yield it
                node = stack.pop()
                yield node.data
                node = node.right

    def children_count(self):
        """
        Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def node_count(self, cnt):
        cnt = 1
        if self.left:
            cnt += self.left.node_count(cnt)
        if self.right:
            cnt += self.right.node_count(cnt)
        return cnt


    def height(self, high):
        children = self.node_count(0)
        #print children
        h = log(children,2)
        return h
