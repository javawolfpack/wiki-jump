import urllib2
from binary_tree import Node, BT






mars = urllib2.urlopen("http://en.wikipedia.org/wiki/Mascarpone").read()
war = urllib2.urlopen("http://en.wikipedia.org/wiki/Wars_of_the_Roses").read()
evaluate = ["Mascarpone","Wars_of_the_Roses"]
root = BT(Node("Mascarpone"))
root.insert(Node("Wars_of_the_Roses"))

#root.print_tree()

#print test