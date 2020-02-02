import os,sys
import subprocess
#from selenium import webdriver
#from urllib2 import urlopen
import requests
import wget

def my_system(cmd):
	print(cmd)
	os.system(cmd)
	
def download(url, file):
	cmd = 'python -m wget %s -o "%s"'%(url, file)
	#my_system(cmd)
	print(cmd)
	ret = subprocess.run(cmd, timeout=8).returncode
	print(' %s return %d'%(cmd, ret))
	if ret != 0:
		raise  'error, %s return %d'%(cmd, ret)
	#wget.download(url, file)
	
def download_chapter(click_url, file):
	download('http://www.hzcourse.com/resource/readBook?path=%s'%click_url, file)
	
def get_bookname(cont):
	s='<div class="book-name">'
	p1 = cont.find(s)
	p1 = p1 + len(s)
	p1 = cont.find('<span>', p1)
	p1 = p1 + len('<span>')
	
	p2 = cont.find('</span>', p1)
	#print(p1, p2)
	name=cont[p1:p2]
	return name
	
def get_value_token(cont):
	s='"ebookId" value="'
	p1 = cont.find(s)
	p1 = p1 + len(s)
	p2 = cont.find('"/>', p1)
	#print(p1, p2)
	ebookId=cont[p1:p2]
	s2 = 'name="token" value="'
	p3 = cont.find(s2, p2)
	p3 = p3 + len(s2)
	p4 = cont.find('"/>', p3)
	#print(p3, p4)
	token=cont[p3:p4]
	print('ebookId, token %s %s'%(ebookId, token))
	return [ebookId, token]
	
def download_book(main_link):
	main_file = 'main.html'
	my_system('del %s'%main_file)
	try:
		download(main_link, main_file)
	except:
		print("Unexpected error:", sys.exc_info()[0])
		return
	main_cont = open(main_file, 'r', encoding='utf-8').read()
	[ebookId, token] = get_value_token(main_cont)
	bookname = get_bookname(main_cont)
	print(bookname)

	dest_folder = bookname
	
	my_system('md "%s"'%dest_folder)
	my_system('copy /y "%s" "%s"'%(main_file, dest_folder))
	finish_file = '%s\\%s'%(dest_folder, 'finish.txt')
	if os.path.isfile(finish_file): return
	
	#response = requests.post('http://www.hzcourse.com/web/refbook/queryAllChapterList', data={'ebookId':15917,'token':"aec187ed5b3a41728b0fb8bd82c3be22"})
	try:
		response = requests.post('http://www.hzcourse.com/web/refbook/queryAllChapterList', data={'ebookId':ebookId,'token':token})
		resp_json = response.json()
	except:
		print("Unexpected error:", sys.exc_info()[0])
		return
	#print(resp_json)
	nExcept = 0
	for i in resp_json['data']['data']:
		ref_link = i['ref']
		file = ref_link[ref_link.rfind('/')+1:]
		print(ref_link, file)
		dest_file = '%s\\%s'%(dest_folder, file)
		if os.path.isfile(dest_file): continue
		
		try:
			download_chapter(ref_link, dest_file)
		except:
			nExcept = nExcept+1
			print("Unexpected error:", sys.exc_info()[0])
			if nExcept>4: return
	
	open(finish_file,'w').write('done')
	
files = [	
'http://www.hzcourse.com/web/refbook/probationAll/6736/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6736/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6856/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7899/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7249/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7165/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7186/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7523/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6965/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6826/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6166/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6188/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6853/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/4599/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6759/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6772/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6754/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6755/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6856/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6965/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/7027/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6736/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6821/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6622/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6606/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6751/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6652/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6050/aec187ed5b3a41728b0fb8bd82c3be22',
'http://www.hzcourse.com/web/refbook/probationAll/6965/aec187ed5b3a41728b0fb8bd82c3be22',
]

def unique(list1): 
	# insert the list to the set 
	list_set = set(list1) 
	# convert the set to the list 
	unique_list = list(list_set)
	return unique_list

def main():	
	files2= unique(files)

	for file in files2:
		download_book(file)
		
#main()
def getStrIn(cont, a, b):
	p1 = cont.find(a)
	p1 = p1 + len(a)

	p2 = cont.find(b, p1)
	name=cont[p1:p2]
	return name
	
def main2():
	for line in open(r'G:\_codes\pydownloadurls.txt','r').readlines():
		line = line.strip()
		p1 = line.find('/detail?id')
		if p1>=0:
			link = 'http://ebooks.cmanuf.com/%s'%line[p1:]
			print(link)
			try:
				resp = requests.get(link)
			except:
				print("Unexpected error:", sys.exc_info()[0])
				continue
			#print(dir(resp))
			#print(resp.text)
			s = getStrIn(resp.text, '<div class="read readactive" >', '</div>')
			s = getStrIn(s, '<a href="', '" target="')
			print(s)
			link2 = 'http://ebooks.cmanuf.com/%s'%s
			try:
				resp2 = requests.get(link2)
			except:
				print("Unexpected error:", sys.exc_info()[0])
				continue
			#print(resp2.text)
			download_book(link2)
			
main()
