import os,sys
print  os.path
print  os.getenv('path')
print os.listdir('')
print dir(os)
#print os.execv('cmd.exe',['/c dir /b'])

print r'*************'
print sys.path
print dir(sys)
#sys.path.append('/my/new/path'')

print __name__



#list
li = ["a", "b", "mpilgrim", "z", "example"] 
print li
print li[-1] #"example"
print li[1:3] #"b", "mpilgrim"
print li[3:]  #"z", "example"
print li.index("example") 
print "c" in li           
li.append(['d', 'e', 'f']) 
print li
li.extend(['d', 'e', 'f']) 
print li
li.remove("d")   
li += ['two'] 
print li
li.remove("e") 
li.pop()          
li = [1, 2] * 3 

#tuple
t = ("a", "b", "mpilgrim", "z", "example") 
t[1:3]

(x, y, z) = ('a',1,123)
print x, z

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
print range(7)

print "%s %s" %('hello','world')

#list mapping
li = [1, 9, 8, 4]
print [elem*2 for elem in li] 

#dictionary
d = {"server":"mpilgrim", "database":"master"} 
print d.items()
print [k for k, v in d.items()]                
print ["%s=%s" % (k, v) for k, v in d.items()] 
print ";".join(["%s=%s" % (k, v) for k, v in d.items()])

print d["server"] 
d["uid"] = "sa"  
print d
del d['uid']

#test join & split
a='--'.join(['1','2','3'])
print a
b1=a.split('--',1)
b2=a.split('--',2)
print b1 #['1', '2--3']
print b2 #['1', '2', '3']
