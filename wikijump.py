import urllib2
from binary_tree import Node, BT
import signal, sys

from bs4 import BeautifulSoup
from time import sleep

import Queue
import time
import thread
import threading

q = Queue.Queue()

lock = threading.Lock()

maxnode = 0 
nodes = {}
exitapp = False

THREADS = []

def handler(signal, frame):
    global THREADS
    global exitapp
    print "Ctrl-C.... Exiting"
    exitapp = True
    sys.exit(0)

def parse(node):
	global q
	global nodes
	global maxnode
	global exitapp
	node.parsed = True
	nodedist = node.distance + 1
	if "/wiki/Vaginal_lubrication" == node.url:
 		print "Done " + str(nodedist)
 		exitapp = True
 		quit()
	print node.url + " " + str(nodedist)
	page = urllib2.urlopen("http://en.wikipedia.org"+node.url).read()
	soup = BeautifulSoup(page)
	links = soup.find_all('a')
	
	#f = open('links.txt', 'w')
	#count = 0
	n = []
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
			## Ignore wikibooks links
			if "wikibooks.org" in str(link):
				continue
			if "kpi.ac.th" in str(link):
				continue
			try:
				href = str(link.get('href')).rstrip().lstrip()
			except:
				print link.get('href') 
			if not href in nodes:
				lnode = Node(href,nodedist,node)
				nodes[href]=lnode
				#nodes[href]
				n = n + [lnode]
				node.add_link(lnode)
			else:
				node.add_link(nodes[href])
			#f.write(str(link.get('href'))+ "\n")
			#count = count + 1
	lock.acquire() # will block if lock is already held
	maxnode = nodedist
	for no in n:
		q.put(no)
	lock.release()
	#f.close()


def parsethread():
	global q
	global maxnode
	global exitapp
	while maxnode < 10 and not exitapp:
		lock.acquire()
		while q.empty():
			lock.release()
			sleep(0.005)
			lock.acquire() # will block if lock is already held
		node = q.get()
		lock.release()
		parse(node)

# def nextNode(depth):
# 	for node in nodes:
# 		if nodes[node].distance == depth:
# 			if not nodes[node][0].get_parsed():
# 				return nodes[node][0]
# 	return None


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

numThreads = 5

#war = urllib2.urlopen("http://en.wikipedia.org/wiki/Wars_of_the_Roses").read()
#evaluate = ["Mascarpone","Wars_of_the_Roses"]
N1 = Node("/wiki/Mascarpone",0)
q.put(N1)
nodes["/wiki/Mascarpone"] = N1
#N2 = Node("/wiki/Wars_of_the_Roses",0)




# depth = 0

def main():
	global THREADS
	try:
		for i in range(numThreads):
			thread = threading.Thread(target=parsethread)
			THREADS.append(thread)
			thread.start()
	except:
		print "Error: unable to start thread"

	for t in THREADS:
	 	t.join()


signal.signal(signal.SIGINT, handler)
main()

##nodes["/wiki/Wars_of_the_Roses"] = N2


# while depth < 14:
# 	next = nextNode(depth)
# 	if nextNode(depth) is None:
# 		depth += 1
# 		print depth
# 	else:
# 		if "/wiki/Wars_of_the_Roses" in next.url:
# 			print "Done " + str(depth)
# 			quit()
# 		q.put((next, depth))

#parse(N1,nodes)
#parse(N2,nodes)


#root.print_tree()
#findLinks(root)
#print test

