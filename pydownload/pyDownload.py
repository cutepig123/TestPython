import os,sys
import subprocess
#from selenium import webdriver
#from urllib2 import urlopen
import requests
import wget
import filecache

	
@filecache.filecache	
def requests_get(link):
	return requests.get(link)

@filecache.filecache	
def requests_post(link,data):
	return requests.post(link, data)
	
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
	
@filecache.filecache	
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
	
def get_bookid_raw(main_link):
	main_file = 'main.html'
	my_system('del %s'%main_file)
	download(main_link, main_file)
	main_cont = open(main_file, 'r', encoding='utf-8').read()
	[ebookId, token] = get_value_token(main_cont)
	bookname = get_bookname(main_cont)
	print(bookname)
	return [ebookId, token, bookname]
	
@filecache.filecache	
def get_bookid_cached(main_link):
	return get_bookid_raw(main_link)
	
g_token = ''	

def clear_token():
	global g_token
	g_token = ''	
	
def get_bookid(main_link):
	global g_token
	if len(g_token)==0:
		[ebookId, token, bookname] = get_bookid_raw(main_link)
		g_token = token
	else:
		[ebookId, token, bookname] = get_bookid_cached(main_link)
	return [ebookId, g_token, bookname]
	
def correct_file_path(s):
	return s.replace(':','').replace('/','').replace('\\','').replace('&','')
	
def download_book(main_link):
	resp_json=''
	while True:
		try:
			print('>>>>step a get book id', main_link)
			[ebookId, token, bookname] = get_bookid(main_link)
			bookname = correct_file_path(bookname)
			print('>>>>result', [ebookId, token, bookname])
			
			dest_folder = bookname
			
			my_system('md "%s"'%dest_folder)
			finish_file = '%s\\%s'%(dest_folder, 'finish.txt')
			if os.path.isfile(finish_file): return
			
			print('>>>>get chapter list')
			response = requests_post('http://www.hzcourse.com/web/refbook/queryAllChapterList', data={'ebookId':ebookId,'token':token})
			resp_json = response.json()
			#print('>>>>result', resp_json)
		
			temp = resp_json['data']['data']
			break
		except:
			print("Unexpected error:", sys.exc_info()[0])
			clear_token()
			
	nExcept = 0
	for i in resp_json['data']['data']:
		ref_link = i['ref']
		file = ref_link[ref_link.rfind('/')+1:]
		print('>>>>get chapter', [ref_link, file])
		dest_file = '%s\\%s'%(dest_folder, file)
		if os.path.isfile(dest_file): continue
		
		try:
			download_chapter(ref_link, dest_file)
		except:
			nExcept = nExcept+1
			print("Unexpected error:", sys.exc_info()[0])
			if nExcept>4: return
	print('>>>>write done')
	open(finish_file,'w').write('done')
	
def unique(list1): 
	# insert the list to the set 
	list_set = set(list1) 
	# convert the set to the list 
	unique_list = list(list_set)
	return unique_list

def getStrIn(cont, a, b):
	p1 = cont.find(a)
	p1 = p1 + len(a)

	p2 = cont.find(b, p1)
	name=cont[p1:p2]
	return name

def main2():
	for line in open(os.path.dirname(os.path.realpath(__file__)) + r'\pydownloadurls.txt','r').readlines():
		line = line.strip()
		p1 = line.find('/detail?id')
		if p1>=0:
			link = 'http://ebooks.cmanuf.com/%s'%line[p1:]
			print('-----------')
			print('>>step1 get',link)
			try:
				resp = requests_get(link)
			except:
				print("Unexpected error:", sys.exc_info()[0])
				continue
			#print(dir(resp))
			#print(resp.text)
			s = getStrIn(resp.text, '<div class="read readactive" >', '</div>')
			s = getStrIn(s, '<a href="', '" target="')
			print('>>result', s)
			link2 = 'http://ebooks.cmanuf.com/%s'%s
			try:
				resp2 = requests_get(link2)
			except:
				print("Unexpected error:", sys.exc_info()[0])
				continue
			#print(resp2.text)
			print('>>step2 download book',link2)
			download_book(link2)
			
main2()
