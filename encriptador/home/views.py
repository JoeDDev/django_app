from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
# Create your views here.

key = [-1,1,1],[-2,-3,1],[3,1,-2]
key2 = [-1,1,1,-2,-3,1,3,1,-2]
content_list = ['A',1,'B',2,'C',3,'D',4,'E',5,'F',6,'G',7,'H',8,'I',9,'J',10,'K',11,'L',12,'M',13,'N',14,'O',15,'P',16,'Q',17,'R',18,'S',19,'T',20,'U',21,'V',22,'W',23,'X',24,'Y',25,'Z',26]



# ------------------------------


def de_encript(matrix_de):
	c_key = np.linalg.matrix_power(key,-1)
	
	result = np.dot(c_key,matrix_de)
	#result_list = result.tolist()
	#print("resultado_1-----------------------")
	#print(result_list)
	#print(result[0][0])
	#print("resultado_2-----------------------")
	result = np.array_str(result)
	
	#print(result)
	#print(type(result))
	m = []
	seg = ''
	hobb = ''
	cont = 0
	c = 0

	for x in result:
		c = c + 1
		if x != '[' and x != ']' and x != '.' and x != ' ' and x != '\n':
			
			if cont < 2:
				seg = seg + x
				cont = cont + 1
				if result[c] == '.':
					m.append(str(seg))
					seg = ''
					cont = 0
	
	#print(m)	
	#print("------------------M------------------")		
	mm = []
	count2 = 0

	col = len(m) // 3
	#print("col de arriba: " + str(col))

	for t in range(0,col):
		#input("toque" + str(t))
		for tres in range(3):

			piece = m[count2]
			count2 = count2 + col
			mm.append(piece)
		count2 = t + 1

	#print(mm)
	#print("------------------MM------------------")		

	for z in mm:
		if z == '27':
			hobb = hobb + ' '
		elif z != '27':
			index = content_list.index(int(z))
			hobb = hobb + content_list[index - 1]

#	print(hobb)

	return hobb
	

#	result = result.astype(np.int)





	

	

def encript(matrix_enc):
	a_key = np.array(key)
	a_matrix = np.array(matrix_enc)
	
	#print(matrix_enc)
	a = np.dot(a_key,a_matrix)
	#print(a)
	b = a.tolist()
	#print(type(b))
	#print(b)
	return a


def matrix(mat):
	
	c = len(mat)%3
	#print("########################")
	#print("largo: " + str(len(mat)))
	#print(c)
	col = 0
	if c >= 1:
		col = (len(mat)//3)+1
	elif c == 0:
		col = len(mat) // 3
	#print(col)
	#print("########################")
	supreme_matrix = [],[],[]
	count = 0
	for x in mat:
		if count < 3:
			#print(str(count)+" --> "+str(x))
			supreme_matrix[count].append(int(x))
			count = count + 1

		else:
			count = 0
			#print(str(count)+" --> "+str(x))
			supreme_matrix[count].append(int(x))
			count = count + 1

	for z in range(3):
		if len(supreme_matrix[z-1]) != col:
			supreme_matrix[z-1].append(27)
	
	
	return supreme_matrix



def number_assign(txt):
	upper = txt.upper()
	encripted = []
	#read my dictionary
	#dic = open('diccionario.txt','r')
	#content = dic.read()
	#convert dic in list
	
	
	#convert upper in list
	step_1 = list(upper)


	for let in step_1:
		if let == ' ':
			encripted.append(27)

		for cont in content_list:
			if cont == let:
				var = content_list.index(cont)
				#print("var: " + str(var))
				data = content_list[var + 1]
				encripted.append(data)
	

	return encripted
	


def home(request):
	return render(request,'home.html',{'name':'Jose'})

def add(request):

	text = request.GET['txt']
	arr = number_assign(text)
	sup_matrix = matrix(arr)
	encripcion = encript(sup_matrix)
	txt_den = de_encript(encripcion)
	#num2 = request.GET['num2']
	#res = int(num1) + int(num2)

	return render(request, 'result.html', {'result':encripcion,'text':text,'txt_den':txt_den})


#text = input("Ingrese texto a encriptar: ")






