#_*_ coding:utf-8 _*_
#中文注释
import urllib2

def load_page(url):
	user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
	headers = {'User-Agent': user_agent}
	req = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(req)
	html = response.read()

	return html


def tieba_spider(url,begin_page,end_page):
	'贴吧小爬虫的方法'
	for x in range(begin_page-1,end_page):
		pn = 50 * x
		#组成一个完整的url
		my_url = url + str(pn)
		#print "Adress of requesting: "
		#print my_url
		html = load_page(url)
		#print "-------------page %d ---------------" %(x+1)
		#print html
		file_name = 'page'+str(x+1)+ '.html'
		write_to_file(file_name,html)

def write_to_file(file_name,txt):
	'write html to a file '
	##1 open file
	print "Saving file " + file_name
	f = open(file_name,'a')
	##2 read and write to file
	f.write(txt)
	##3 close file
	f.close()




#main
if __name__ == '__main__':
	url = raw_input("Please Input the Adress of TieBa: ")
	#print url
	begin_page = int(raw_input("Please input the begin page: "))
	end_page = int(raw_input("Please input the end page: "))
	tieba_spider(url, begin_page, end_page)
