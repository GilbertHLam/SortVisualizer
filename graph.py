#Created by Gilbert Lam
#Sorting Algorithm Visualizer
#This program will create a visual representation of how each sorting algorithm work. Users will be given the option to select the data size and the speed at which the animation occurs
#Current Bugs: -If a sort is performed, but a new one is started before the old one has completed, it will show the old one right after the new one is done


from random import *

from time import sleep





class Sort:
	def __init__(self, sortChoice, dataSize, caseChoice, graphArea, speed):
		self.sortChoice = sortChoice.get()
		self.caseChoice = caseChoice.get()
		self.dataSize = int(dataSize)
		self.data = []
		self.width = 5
		self.graphArea = graphArea
		self.speed = speed
		if self.caseChoice == "Random":
			for i in range (0, self.dataSize, 1):
				self.data.append(randint(0,500))
		elif self.caseChoice == "Best Case":
			for i in range (0, self.dataSize, 1):
				self.data.append(i*2)
		else:
			for i in range (self.dataSize, 0, -1):
				self.data.append(i*2)
		if self.sortChoice == "Bubble":
			self.bubbleSort()
		elif self.sortChoice == "Insertion":
			self.insertionSort()
		elif self.sortChoice == "Selection":
			self.selectionSort()
		else:
			self.bogo()

	
	def draw(self, indexOne, indexTwo):
		
		sleep(self.speed)
		self.graphArea.delete("all")
		self.graphArea.create_rectangle(0,0,1250,500, fill = "black")
		
		for i in range (0, len(self.data), 1):
			fillColor = "white"
			if i == indexOne or i == indexTwo:
				if i != len(self.data) - 1 or i != len(self.data) - 2:
					fillColor = "red"
			self.graphArea.create_rectangle(i*self.width,500-self.data[i],i*self.width+self.width,500-self.data[i]+self.data[i], fill = fillColor)
		self.graphArea.update()
	
	def bubbleSort(self):
		for i in range (len(self.data)):
			for k in range(len(self.data) - 1, i, -1):
				if (self.data[k] < self.data[k-1]):
					temp = self.data[k]
					self.data[k] = self.data[k-1]
					self.data[k-1] = temp
				self.draw(k,k-1)
	
	def selectionSort(self):
		for i in range(len(self.data)):
			smallest = min(self.data[i:])
			min_index = self.data[i:].index(smallest) 
			self.data[i + min_index] = self.data[i] 
			self.data[i] = smallest                
			self.draw(i, i + min_index)
	
	def insertionSort(self):
		for i in range(1,len(self.data)): 
			j = i                   
			while j > 0 and self.data[j] < self.data[j-1]: 
				self.data[j], self.data[j-1] = self.data[j-1], self.data[j] 
				j=j-1
			self.draw(j, j-1)
	
	def inorder(self):
		i = 0
		j = len(self.data)
		while i + 1 < j:
			if self.data[i] > self.data[i + 1]:
				return False
			i += 1
		return True

	def bogo(self):
		while not self.inorder():
			shuffle(self.data)
			self.draw(10000,100000)
	
	

		
		
		
