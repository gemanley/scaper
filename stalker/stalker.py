import re
import urllib2
import time
#import StringIO
print "Strating  Tracking program... please wait"
f = open('majors.txt','r')
StudentLink=[]
filepath = 'majors.txt'
list=[]
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
        start = line.find( '<' )
        end = line.find( '>' )
        if start != -1 and end != -1:
                result = line[start+1:end-1]
                result = result.replace('"',"")
                result = result.replace("option value=","")
		result = result.replace("&amp;","&")
		result = result.replace(" ","%20")
#                print result
		list.append(result)
		

#        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1
lines=f.read()
lol="lol"
#list=["Advertising"]
for degree in list:
	for  number in  range(1,120):
		url ="https://www.info.iastate.edu/individuals/advanced?last_name=&first_name=&email=&department=" 
		major=degree
		print "#" + major
		url2= "&individual_type=students&orderby=0&orderdir=0&page="
		nextnumber=str(number+1)
		number=str(number)
		string= url+major+url2+number
#		print string
		contents = urllib2.urlopen(url+major+url2+number).read()
#		print contents
		bar = contents.splitlines()
		present=str(contents)
		next="individual_type=students&amp;orderby=0&amp;orderdir=0&amp;page="+str(nextnumber)
	#	print next
		item= present.find(next)
#		print item
#		print bar
#		time.sleep(3)
		sub = "/individuals/info/"		
		Found=0
		for  line in bar:
			#print line
			if "/individuals/info/" in line:
				start = line.find( 'href' )
				Found=1
		      	        end = line.find( 'span' )
        			if start != -1 and end != -1:
                			result = line[start+7:end]
					result = result.replace('<',"")
		               		result = result.replace(">","")
					result = result.replace('"',"")
#					print result
					
					if result not in StudentLink:
						StudentLink.append(result)
					if result in StudentLink:
						number=180

			if int(item) <= int(0):
				break
		if Found==0:
			print "Error"
			while True:
    				start = contents.find(sub, start)
				if start == -1: break
				start += len(sub)# use start += 1 to find overlapping matches
				contents=str(contents)
				newstr=contents[start-18:start+30]
				newstr=newstr.split('"')
#				print newstr[0]
				StudentLink.append(newstr[0])
#				print start
			number=1000	
			break			
print "done"

#for major in list:
#	print major
thefile = open("linker.txt", 'w')
for user in StudentLink:
	url="https://www.info.iastate.edu/"
	student=user
	link=url+student
	thefile.write(link)

