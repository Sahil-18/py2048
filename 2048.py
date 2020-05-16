#Matrix dimensions input
#Winning tile no input
import argparse
p=argparse.ArgumentParser()
p.add_argument("--n",help="Provide Board size",type=int,nargs='?',default=5)
p.add_argument("--w",help="win value",type=int,nargs='?',default=2048)
arg=p.parse_args()

n=arg.n
w=arg.w
#Cross check for w
def check(w):
	for p in range(1,1000):
		if 2**p<=w:
			pass
		else:
			w=2**(p-1)
			break
	return w

w=check(w)
#Initialize matrix
matrix=[]
#Building the matrix with all position are 0
for i in range(n):
	x=[]
	for j in range(n):
		x.append(0)
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
			print(matrix[i][j],end="   ")
		print( )

#To clear screen
def clear():
	import os
	if os.name=="nt":
		os.system('cls')
	else:
		os.system('clear')
#defining all move control function for 'W','A,'S','D' inputs
def moveup(matrix,n):
	count=0
	for k in range(n):
		for i in range(n-1):
			if matrix[i][k]==0:
				continue
			else:
				for j in range(i+1,n):
					if matrix[j][k]==matrix[i][k]:
						matrix[i][k]=matrix[i][k]+matrix[j][k]
						matrix[j][k]=0
						count+=1
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
						count+=1
						break
			else:
				continue
	
	return (matrix,count)

def moveleft(matrix,n):
	count=0
	for k in range(n):
		for i in range(n-1):
			if matrix[k][i]==0:
				continue
			else:
				for j in range(i+1,n):
					if matrix[k][j]==matrix[k][i]:
						matrix[k][i]=matrix[k][i]+matrix[k][j]
						matrix[k][j]=0
						count+=1
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
						count+=1
						break
			else:
				continue
	
	return (matrix,count)

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

#Random insertion of 2
def insert(matrix,n):
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
	import msvcrt #taking input without pressing Enter 
	print("Your next move: ")
	q=msvcrt.getche().upper()
	if q==b'W':
		matrix,count=moveup(matrix,n)
		if count!=0:
			matrix=insert(matrix,n)
		win(matrix,n)
	elif q==b'A':
		matrix,count=moveleft(matrix,n)
		if count!=0:
			matrix=insert(matrix,n)
		win(matrix,n)
	elif q==b'S':
		matrix=rotateup(matrix,n)
		matrix,count=moveup(matrix,n)
		matrix=rotateup(matrix,n)
		if count!=0:
			matrix=insert(matrix,n)		
		win(matrix,n)
	elif q==b'D':
		matrix=rotateside(matrix,n)
		matrix,count=moveleft(matrix,n)
		matrix=rotateside(matrix,n)
		if count!=0:
			matrix=insert(matrix,n)
		win(matrix,n)
	else:
		print("Incorrect input!! Please enter corrct input again")





























