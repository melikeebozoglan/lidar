from PIL import Image
import math

file1 = open('data.txt', 'r')
Lines = file1.readlines()
file1.close()

im = Image.open('empty.png')  
width, height = im.size

pix = im.load()  

for line in Lines:
    part = line.split("->")

    #print(Lines[0]+"\n")
    #print(part[0]+"\n" +part[1])

    angDis = part[1].split(":/:")
    #print("Ang : "+ angDis[0].strip() +", Dis:"+angDis[1].strip())

    angle = float(angDis[0])
    distance = float(angDis[1])

    
    x = int(width / 2 + distance * math.cos(math.radians(angle)))
    y = int(height / 2 + distance * math.sin(math.radians(angle)))
    #print(x , y)

    pix[x, y] = (0, 0, 0)  

im.save("output.png")

#im.show()
