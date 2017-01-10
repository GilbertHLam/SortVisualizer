#Created by Gilbert Lam
#Sorting Algorithm Visualizer
#This program will create a visual representation of how each sorting algorithm work. Users will be given the option to select the data size and the speed at which the animation occurs
#Current Bugs: -If a sort is performed, but a new one is started before the old one has completed, it will show the old one right after the new one is done



from tkinter import *
from graph import Sort

mainWindow = Tk()

listOfInstance = []

def enter():
	temp = speedChoice.get()
	if temp == "Slow":
		speed = 0.1
	elif temp == "Medium":
		speed = 0.01
	elif temp == "Fast":
		speed = 0.001
	else:
		speed = 0.0001
	listOfInstance.append(Sort(sortChoice, dataSizeChoice.get(), caseChoice, graphArea, speed))
	
dataSizes = [5, 10, 50, 100, 250]
sortOptions = ["Bubble", "Selection", "Insertion", "Bogo"]
caseOptions = ["Random", "Best Case", "Worst Case"]
speedOptions = ["Slow", "Medium", "Fast", "Very Fast"]

speedChoice = StringVar(mainWindow)
speedChoice.set(speedOptions[1])

dataSizeChoice = IntVar(mainWindow)
dataSizeChoice.set(dataSizes[0]) 

sortChoice = StringVar(mainWindow)
sortChoice.set(sortOptions[0])

caseChoice = StringVar(mainWindow)
caseChoice.set(caseOptions[0])

sortBox = OptionMenu(mainWindow, sortChoice,*sortOptions)
sortBox.grid(row = 0, column = 1)

speedBox = OptionMenu(mainWindow, speedChoice, *speedOptions)
speedBox.grid(row = 3, column = 1)

speedPrompt = Label(mainWindow, text = "Speed: ")
speedPrompt.grid(row = 3, column = 0)

userInput = OptionMenu(mainWindow, dataSizeChoice,*dataSizes)
userInput.grid(row = 1, column = 1)

caseMenu = OptionMenu(mainWindow,caseChoice,*caseOptions)
caseMenu.grid(row = 2, column = 1)

visualizeButton = Button(mainWindow, text="Visualize!", command = enter)
visualizeButton.grid(row = 1, column = 2)

sortPrompt = Label(mainWindow, text = "Type of sort: ")
sortPrompt.grid(row = 0, column = 0)

sizePrompt = Label(mainWindow, text = "Data Size: ")
sizePrompt.grid(row = 1, column = 0)

orderPrompt = Label(mainWindow, text = "Data order: ")
orderPrompt.grid(row = 2, column = 0)

graphArea = Canvas(mainWindow, width = 1250, height = 500)
graphArea.grid(row = 4, column = 0, columnspan = 2)

graphArea.create_rectangle(0,0,1250,500, fill = "black")


mainWindow.mainloop()