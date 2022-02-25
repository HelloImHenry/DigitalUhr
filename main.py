from tkinter import *
import time
import math
root = Tk()
#Offset zum Rand
offset_Border = 50
#Speichert alle Striche sprich die UI Elemente der Zahlen, um sie wieder zu löschen nachdem sich die zeit verändert
uiElements = []
#Der Abstand der Punkte(die ich als Striche Zeichne) von der Mittellinie
offset_PointsFromMiddle = 20
#Der Abstand zwischen den Zahlen und Doppelpunkten in x
offset_PointsToNumber = 30
#Die Länge der Striche, welche die Doppelpunkte repräsentieren.
size_Points =20
#Die Länge einer Linie
sizeLine = 100
#Der Abstand zwischen den Zahlen
sizeOffsetBetweenNumbers = 20
#Der Offset damit die Linien sich nicht Perfekt schneiden. Falls sie perfekt anliegen sollen 0 eingeben.
offsetBetweenLines = 0
#Die Funktion berrechnet die Größe des Fensters.
#7, Weil wir vor der ersten und nach der letzten Zahl noch ein Offset haben wollen, damit das alles nicht so nah am Rand ist.
sizeX = sizeLine*6+offset_Border*2+offset_PointsToNumber*4+size_Points*2 +sizeOffsetBetweenNumbers*3
#Die Funktion berrechnet die Größe des Fensters.
#2, Weil wir über der ersten und unter der letzten Zahl noch ein Offset haben wollen, damit das alles nicht so nah am Rand ist.
sizeY = offset_Border*2+offsetBetweenLines*4+sizeLine*2
sizeRoot = str(sizeX) + "x" +str(sizeY)
root.geometry(sizeRoot)
root.title("7 Widget Uhr")
cv = Canvas(root,width=sizeX,height=sizeY)
cv.pack()
def draw_points():
    for x in range(2):
        offsetX = offset_Border + (x+1)*((2*sizeLine) + sizeOffsetBetweenNumbers) + offset_PointsToNumber + (x)*(2*offset_PointsToNumber+size_Points)
        offsetX2 = offsetX+size_Points
        for y in range(2):
            reverse = 1
            if y == 1:
                reverse = -1
            offsetY = offset_Border+offsetBetweenLines+sizeLine+offsetBetweenLines+ reverse*(offset_PointsFromMiddle+(size_Points*y))
            offsetY2 = offsetY+size_Points
            cv.create_oval(offsetX,offsetY,offsetX2,offsetY2,fill = "black")
draw_points()
#Enthält die Linien welche für die Koresspondierende Zahl gezeichnet werden müssen.
numberIDs = [[0,1,2,4,5,6],[2,5],[0,2,3,4,6],[0,2,3,5,6],[1,2,3,5],[0,1,3,5,6],[0,1,3,4,5,6],[0,2,5], [0,1,2,3,4,5,6], [0,1,2,3,5,6]]
def draw_Vertical_Line(numberPos,id):
    #Sieze draw_Horizontal_Line
    pointMultiplier = int(numberPos/2)
    lineMultiplier = int(math.ceil(numberPos/2))
    #Speichert ob es sich bei der ID um eine Obere oder Untere Linie Handelt.
    lower = 0
    #Speichert ob es Die linke oder Rechte Linie ist.
    right = 0
    #Hier wird zwischen den Positionen entschieden indem die Position -4 Gerrechnet wird. Ist die ID dann >= 0 haben wir die untere linie. Sonst die obere.
    if id == 4 or id == 5:
        lower = 1
    if id == 2 or id == 5:
        right = 1
    #Die Erste und 2 X:
    offsetX = offset_Border + pointMultiplier*(2*offset_PointsToNumber+size_Points) + lineMultiplier*(sizeOffsetBetweenNumbers)+numberPos*sizeLine+sizeLine*right    
    #Die ErsteY:
    offsetY = offset_Border + offsetBetweenLines + lower*(sizeLine+2*offsetBetweenLines)
    #Die ZweiteY:
    offsetY2 = offsetY+sizeLine
    id = cv.create_line(offsetX,offsetY,offsetX,offsetY2)
    uiElements.append(id)
def draw_Horizontal_Line(numberPos,id):
    #PointMultipliere Speichert die Doppelpunkte die bis zu der numberPos bereits gezeichnet Wurden
    pointMultiplier = int(numberPos/2)
    #lineMultiplier berrechnet die Anzahl der Abstände zwischen den Zahlen, welche bis zu dieser Position zurückgelegt wurden.
    lineMultiplier = int(math.ceil(numberPos/2))
    print(str(lineMultiplier)+ "__" +str(numberPos))
    offsetY = offset_Border + (id/3)*(sizeLine) + 2*(id/3)*offsetBetweenLines
    #Die Erste X:
    offsetX = offset_Border + pointMultiplier*(2*offset_PointsToNumber+size_Points) + lineMultiplier*(sizeOffsetBetweenNumbers)+numberPos*sizeLine
    #Die Zweite X:
    offsetX2 = offsetX+sizeLine
    #Die Erste und Zweite Y:
    id = cv.create_line(offsetX,offsetY,offsetX2,offsetY)
    uiElements.append(id)
def draw_Number(numberPos,number):
    horizontal = [0,3,6]
    for x in (numberIDs[number]):
        if x in horizontal:
            draw_Horizontal_Line(numberPos,x)
        else:
            draw_Vertical_Line(numberPos,x)
def draw_Time(time):
    numbersInTime = time.split(':')
    timeConverted = str(numbersInTime[0]) + str(numbersInTime[1]) + str(numbersInTime[2])
    for x in range(len(timeConverted)):
        draw_Number(x,int(timeConverted[x]))
def update_Time():
    for x in uiElements:
        cv.delete(x)
    uiElements.clear()
    draw_Time(time.strftime('%H:%M:%S'))
    root.after(1000,update_Time)
update_Time()
root.mainloop()