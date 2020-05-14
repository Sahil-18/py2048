#Matrix dimensions input
n=5  #default
print("Do you want to change the dimension n if yes enter 'Y' and if no enter 'N'")
m=input("Enter your option: ")
if m =='Y':
	n=int(input("Enter the dimension of matrix: "))
else:
	pass

#Cross check for w
def check():
	w=int(input("Enter the winning tile no: "))
	for p in range(1,13):
		if 2**p==w:
			return w
			break
		else:
			continue
	print("You have entered incorrect value for winning tile no")
	print("Input must be equal to some power of 2. Please try again!!")
	w=check()
	return w

#winnig tile no initializatiom
w=2048  #default
print("Do you want to change the winning tile no if yes enter 'Y' and if no enter 'N'")
b=input("Enter your option: ")
if b =='Y':
	w=check()
else:
	pass

#Initialize matrix
matrix=[]
#Building the matrix with all position are 0
for i in range(n):
	x=[]
	for j in range(n):
		x.append('0')
	matrix.append(x)

#Placing 2 at random position in matrix
import random
i=random.randint(0,n-1)
j=random.randint(0,n-1)
matrix[i][j]=2


#Printing of matrix
def matrixout(matrix,n):
	for i in range(n):
		for j in range(n):
			print(matrix[i][j],end="  ")
		print( )


#To clear screen
def clear():
	import os
	os.system('cls')

#defining all move control function for 'W','A,'S','D' inputs
def moveup(matrix,n):
	for k in range(n):
		for i in range(n-1):
			if matrix[i][k]==0:
				continue
			else:
				for j in range(i+1,n):
					if matrix[j][k]==matrix[i][k]:
						matrix[i][k]=matrix[i][k]+matrix[j][k]
						matrix[j][k]=0
						break
					else:
						continue

	
	for k in range(n):
		for i in range(n-1):
			if matrix[i][k]==0:
				for j in range(i+1,n):
					if matrix[j][k]==0:
						continue
					else:
						matrix[i][k]=matrix[j][k]
						matrix[j][k]=0
						break
			else:
				continue
	
	return matrix

def moveleft(matrix,n):
	for k in range(n):
		for i in range(n-1):
			if matrix[k][i]==0:
				continue
			else:
				for j in range(i+1,n):
					if matrix[k][j]==matrix[k][i]:
						matrix[k][i]=matrix[k][i]+matrix[k][j]
						matrix[k][j]=0
						break
					else:
						continue
	
	for k in range(n):
		for i in range(n-1):
			if matrix[k][i]==0:
				for j in range(i+1,n):
					if matrix[k][j]==0:
						continue
					else:
						matrix[k][i]=matrix[k][j]
						matrix[k][j]=0
						break
			else:
				continue
	return matrix

# Rotation of matrix for up down motion
def rotateup(matrix,n):
	for i in range(n//2):
		for j in range(n):
			store=matrix[i][j]
			matrix[i][j]=matrix[n-1-i][j]
			matrix[n-1-i][j]=store
	return matrix
# Rotation of matrix for side motion
def rotateside(matrix,n):
	for i in range(n//2):
		for j in range(n):
			store=matrix[j][i]
			matrix[j][i]=matrix[j][n-1-i]
			matrix[j][n-1-i]=store
	return matrix

def movedown(matrix,n):
	for k in range(n):
		i=n-1
		while i>0:
			if matrix[i][k]==0:
				continue
			else:
				j=n-2
				while j>=0:
					if matrix[j][k]==matrix[i][k]:
						matrix[i][k]=matrix[i][k]+matrix[j][k]
						matrix[j][k]=0
						break
					else:
						continue
				j-=1
		i-=1

	
	for k in range(n):
		i=n-1
		while i>0:
			if matrix[i][k]==0:
				j=n-2
				while j>=0:
					if matrix[j][k]==0:
						continue
					else:
						matrix[i][k]=matrix[j][k]
						matrix[j][k]=0
						break
				j-=1
			else:
				continue
		i-=1
	return matrix

def moveright(matrix,n):
	for k in range(n):
		i=n-1
		while i>0:
			if matrix[k][i]==0:
				continue
			else:
				j=n-2
				while j>=0:
					if matrix[k][j]==matrix[k][i]:
						matrix[k][i]=matrix[k][i]+matrix[k][j]
						matrix[k][j]=0
						break
					else:
						continue
				j-=1
		i-=1

	
	for k in range(n):
		i=n-1
		while i>0:
			if matrix[k][i]==0:
				j=n-2
				while j>=0:
					if matrix[k][j]==0:
						continue
					else:
						matrix[k][i]=matrix[k][j]
						matrix[k][j]=0
						break
				j-=1
			else:
				continue
		i-=1
	return matrix

#Random insertion of 2
def insert(matrix,n):
	'''a=[]
	count=0
	import random
	for i in range(n):
		x=[]
		for j in range(n):
			if matrix[i][j]==0:
				x.append(i)
				x.append(j)
				count+=1
		a.append(x)

	if count<=4:
		[i,j]=random.choice(a)
		matrix[i][j]=2	
	else:'''
	while True:
		i=random.randint(0,n-1)
		j=random.randint(0,n-1)
		if matrix[i][j]==0:
			matrix[i][j]=2
			break
		else:
			continue
	return matrix

# Winnig condition
def win(matrix,n):
	for i in range(n):
		for j in range(n):
			if matrix[i][j]==w:
				clear()
				matrixout(matrix,n)
				print("Hurray!!! You won this game")
				exit()
	lost(matrix,n)

#Loosing condition Check
def defeat(matrix,n):
	count=0
	for i in range(n-1):
		for j in range(n-1):
			if matrix[i][j]==matrix[i+1][j] or matrix[i][j]==matrix[i][j+1]:
				count +=1
				break
		if count ==1:
			break

	for i in range(n-1):
		if matrix[i][n-1]==matrix[i+1][n-1]:
			count+=1
			break
	for i in range(n-1):
		if matrix[n-1][i]==matrix[n-1][i+1]:
			count+=1
			break
	if count==0:
		print("You lost the game.Try it again!!")
		exit()

def lost(matrix,n):
	count=0
	for i in range(n):
		for j in range(n):
			if matrix[i][j]==0:
				count+=1
				break
		if count==1:
			break

	if count==0:
		defeat(matrix,n)

#Game starts here
while True:
	clear()
	print("Moves are 'W'=Up, 'A'=Left, 'S'=Down, 'D'=Right")
	matrixout(matrix,n)
	q=input("Your next move: ")
	if q=='W':
		matrix=moveup(matrix,n)
		matrix=insert(matrix,n)
		win(matrix,n)
	elif q=='A':
		matrix=moveleft(matrix,n)
		matrix=insert(matrix,n)
		win(matrix,n)
	elif q=='S':
		matrix=rotateside(matrix,n)
		matrix=moveleft(matrix,n)
		matrix=rotateside(matrix,n)
		matrix=insert(matrix,n)
		win(matrix,n)
	elif q=='D':
		matrix=rotateup(matrix,n)
		matrix=moveup(matrix,n)
		matrix=rotateup(matrix,n)
		matrix=insert(matrix,n)
		win(matrix,n)
	else:
		print("Incorrect input!! Please enter corrct input again")





























