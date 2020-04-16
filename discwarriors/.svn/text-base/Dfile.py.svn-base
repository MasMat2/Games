#
#	Dfile.py
#		for importing dfiles
#

import os.path

def getType(path):
	if os.path.isfile(path):
		dfile=open(path)
		cont=dfile.read()
		dfile.close()
		beg=cont.find("[")+1
		end=cont.find(";")
		return cont[beg:end]
	else:
		print "FILE "+path+" NOT FOUND!"
		raise SystemExit
		
def getName(path):
	if os.path.isfile(path):
		dfile=open(path)
		cont=dfile.read()
		dfile.close()
		beg=cont.find(";")+1
		end=cont.find("]")
		return cont[beg:end]
	else:
		print "FILE "+path+" NOT FOUND!"
		raise SystemExit

def getAtr(path,cls,atr):
	if os.path.isfile(path):
		dfile=open(path)
		on=0
		for line in dfile:
			if line.find("["+cls+"]")!=-1:
				on=1
			if line.find("[/"+cls+"]")!=-1:
				on=-1
			if on==1:
				if line.find(atr)!=-1:
					length=len(atr)+1
					ret=line[length:-2]
					if ret[-1]==';':
						ret=ret[0:-1]
					return ret
					dfile.close()
					break;
				elif line=="[NM]":
					return -1
					dfile.close()
			elif on==0:
				continue
			elif on==-1:
				return -1
	else:
		print "FILE "+path+" NOT FOUND!"
		raise SystemExit
