#coding=utf-8

#x1x2...xn
#����xi����2��ֵ
#Ҫ��ӡ������������ Ҳ����2^n
#����ôʵ�֣�

def get_all(s1,s2):
	if len(s1)==0:
		pass
	elif len(s1)==1:
		return [s1,s2]
	else:
		s=[]
		for i in get_all(s1[1::],s2[1::]):
			s.append(s1[0]+i)
			s.append(s2[0]+i)
		return s

#����
#for(i=1:2^n)
#{
# ����ÿһλ��ֵ, �����Ӧ����
#}

def get_all_new(s1,s2):
	n=len(s1)
	for i in range(0,1<<n):
		s=''
		for j in range(0,n):
			if (i & (1<<j)) == 0:
				s += s1[j]
			else:
				s += s2[j]
		print s

s1='123'
s2='abc'
s=get_all(s1,s2)
for i in s:
	print i

print '---new---'
get_all_new(s1,s2)