import os,sys

def ver_version():
	return sys.version

"""
FICHEROS




"""

def crearDirectorio(path_file):
	if (os.access(path_file,1) == False):
		os.mkdir(path_file)
	else:
		print "Ya existe el directorio"
		

def VerVariablesEntorno():
#Funcion que devuevla el usuario, la shell y el path con el que estamos trabajando	
	for x,y in os.environ.iteritems():
		if x=="USER" or x=="PATH" or x=="SHELL":
			print x+"-->"+y
	print os.environ.get('USER')
	print os.environ.get('PATH')
	print os.environ.get('SHELL')
	


def gordos(path_dir,size):
#Funcion que devuelva los ficheros que ocupan mas de un tamanio indicado
	if str(size).count("M"):
		size_final=int(str(size)[:-1])*1024
	elif str(size).count("G"):
		size_final=int(str(size)[:-1])*1024*1024
	else:
		size_final=size
	for x in os.listdir(path_dir):
		path_completo=path_dir+"/"+str(x)
		size_file=os.path.getsize(path_completo)
		if os.path.isfile(path_completo) and size_file>size_final:
			print x+" --> "+str(size_file)+" Bytes"
