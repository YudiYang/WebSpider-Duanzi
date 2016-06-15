
import urllib2
import re

class Spider:
	"""docstring for Spider"""

	def __init__(self):
		self.enable = True;
		self.page   = 1;
		pass

	def load_page(self, page):
		'sent duanzi url and get html codes'
		if page == 1:
			url = "http://www.neihan8.com/wenzi/index.html"
		else : 
		    url = "http://www.neihan8.com/wenzi/index_"+str(page)+".html"
		user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
		headers = {"User-Agent": user_agent}
		req = urllib2.Request(url, headers = headers)

		response = urllib2.urlopen(req)

		html = response.read()
		#gbk_html = html.decode("gbk").encode("utf-8")
		##we need to use equaltion to filter html 
		##all duanzi is include in <div class="desc">
		pattern = re.compile(r'<div.*?class="desc">(.*?)</div>',re.S)

		item_list = pattern.findall(html)
		num = 1
		for item in item_list:

			self.page_write(item,num)
			num+=1
		return

	def page_write(self,txt,num):
		'write html to a file '
		##1 open file
		#print "Saving file " + filename
		f = open('mystory.txt','a')
		##2 read and write to file
		f.write('----------------Page: %d--Num: %d-----------------\n' %(self.page,num)) 
		f.write(txt+"\n")
		f.write('--------------------------------------------------\n\n\n')
		##3 close file
		f.close()
		return


	def doWork(self):
		'interface with spider program'
		while self.enable:
			
			print "Enter to go on"
			print "'quit' to quit"
			command = raw_input()
			if command == 'quit':
				self.enable = False
				break;
			print "=========dealing with page %d=================" %(self.page)
			self.load_page(self.page)
			self.page += 1

		return


#main
if __name__ == '__main__':

	#begin_page = int(raw_input('please insert the start page:'))
	#end_page = int(raw_input('please insert the end page:'))
	myspider = Spider();
	myspider.doWork();
	
	