
import matplotlib.pyplot as plt
import numpy as np


def getNumber(my_str):
    return int(''.join(list(filter(str.isdigit, my_str.split(" ")[1]))));

file = open("coordinates_KEY.txt","r")

singleLine = file.readline();






filereader = file.readlines();
print(len(filereader));

prevX = []
prevY = []
mainArrayX = []
mainArrayY = []

for i in range(21):
    prevX.append("");
    prevY.append("");

    mainArrayX.append([]);
    mainArrayY.append([]);





for i in range(26853):
    singleLine = filereader[i];
    roundNumber = getNumber(singleLine);

    counter = 0;
    for char in filereader[i]:
        if char == "(":
            coordArray = singleLine[counter:(len(singleLine) - 1)].split(",");
            x = (coordArray[0])[1:];
            y = (coordArray[1])[:-1]

            if prevX[roundNumber] != x or prevY[roundNumber] != y:
                mainArrayX[roundNumber].append(x);
                mainArrayY[roundNumber].append(y);
                prevX[roundNumber] = x;
                prevY[roundNumber] = y;

        counter += 1;





for i in range(5):
    if i == 0 or i == 7 or i == 14:
        print("NAH")
    else:
        print("This is round " + str(i));
        print("Are sizes equal? ");
        mainArrayX[i] = mainArrayX[i][:-1];
        mainArrayY[i] = mainArrayY[i][:-1];
        print( len(mainArrayX[i]) == len(mainArrayY[i]) );
        print(mainArrayX[i]);
        print(mainArrayY[i]);
        print("********");
        # plt.scatter(mainArrayX[i], mainArrayY[i])
        # plt.scatter(mainArrayX[i][0], mainArrayX[i][0], color = "green");
        # plt.scatter(mainArrayX[i][-1], mainArrayX[i][-1], color = "red");
        # plt.plot(mainArrayX[i], mainArrayY[i], linewidth=3)

        # lists = sorted(zip(*[mainArrayX[i], mainArrayY[i]]))
        # new_x, new_y = list(zip(*lists))
        # plt.plot(new_x, new_y)


        
        plt.show()

