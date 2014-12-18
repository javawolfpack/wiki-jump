import urllib2
from binary_tree import Node, BT

from bs4 import BeautifulSoup


nodes = {}

def parse(node, depth):
	print node.url + " " + str(depth)
	node.parsed = True
	nodedist = depth + 1
	page = urllib2.urlopen("http://en.wikipedia.org"+node.url).read()
	soup = BeautifulSoup(page)
	links = soup.find_all('a')
	
	#f = open('links.txt', 'w')
	#count = 0

	for link in links:
		if "/wiki/" in str(link):
			## Ignore contact us page link on Wikipedia
			if "Wikipedia:Contact_us" in str(link): 
				continue
			## Ignore File links on Wikipedia
			if "File:" in str(link):
				continue
			## Ignore Citation notes
			if "cite_note" in str(link):
				continue
			## Ignore commons media links
			if "commons.wikimedia.org/" in str(link):
				continue
			## Ignore wikimediafoundation links
			if "wikimediafoundation.org" in str(link):
				continue
			## Ignore Wikipedia page links
			if "Wikipedia:" in str(link):
				continue
			## Ignore Special page links
			if "Special:" in str(link):
				continue
			## Ignore Help links
			if "Help:" in str(link):
				continue
			## Ignore Portal page links
			if "Portal:" in str(link):
				continue
			## Ignore other language wikipedia links
			if "wikipedia.org" in str(link):
				continue
			## Ignore discussion page
			if "Talk:" in str(link):
				continue
			## Ignore wikidata links
			if "wikidata" in str(link):
				continue
			## Ignore main page links
			if "Main_Page" in str(link):
				continue
			## Ignore current page links
			if ">Read</a>" in str(link) or ">Article</a>" in str(link):
				continue
			## Ignore template pages
			if "Template:" in str(link) or "Template_talk:" in str(link):
				continue
			## Ignore wiktionary links
			if "wiktionary.org" in str(link):
				continue
			## Ignore wikivoyage links
			if "wikivoyage.org" in str(link):
				continue
			## Ignore wikisource links
			if "wikisource.org" in str(link):
				continue
			## Ignore wikinews links
			if "wikinews.org" in str(link):
				continue
			## Ignore wikiquote links
			if "wikiquote.org" in str(link):
				continue
			## Ignore wikiversity links
			if "wikiversity.org" in str(link):
				continue
			href = str(link.get('href')).rstrip().lstrip()
			if not href in nodes:
				lnode = Node(href,nodedist,node)
				nodes[href]=(lnode,nodedist)
				node.add_link(lnode)
			else:
				node.add_link(nodes[href])
			#f.write(str(link.get('href'))+ "\n")
			#count = count + 1
	#f.close()

def nextNode(depth):
	for node in nodes:
		if nodes[node][1] == depth:
			if not nodes[node][0].get_parsed():
				return nodes[node][0]
	return None


# def findNext(node):
# 	return node.find_parsed()

# def findLinks(root):
# 	node = findNext(root)
# 	while not node is None:
# 		links = parse(node)
# 		if not root.height(2) > 25:
# 			for link in links:
# 				root.insert(link)
# 		#root.print_tree()
# 		node.set_parsed()
# 		node = findNext(root)
		#print node

		#quit()



war = urllib2.urlopen("http://en.wikipedia.org/wiki/Wars_of_the_Roses").read()
evaluate = ["Mascarpone","Wars_of_the_Roses"]
N1 = Node("/wiki/Mascarpone",0)
#N2 = Node("/wiki/Wars_of_the_Roses",0)


depth = 0

nodes["/wiki/Mascarpone"] = (N1,0)
##nodes["/wiki/Wars_of_the_Roses"] = N2


while depth < 14:
	next = nextNode(depth)
	if nextNode(depth) is None:
		depth += 1
	else:
		if "/wiki/Wars_of_the_Roses" in next.url:
			print "Done " + str(depth)
			quit()
		parse(next, depth)

#parse(N1,nodes)
#parse(N2,nodes)


#root.print_tree()
#findLinks(root)
#print test

