from os import listdir
from os.path import isfile, join

coordinates = "allData/coordinates/"
goalKeys = "allData/goalKey/"


coords = [f for f in listdir(coordinates) if isfile(join(coordinates, f))];
goals = [f for f in listdir(goalKeys) if isfile(join(goalKeys, f))];

coords.sort();
goals.sort();

coords = [coordinates + e  for e in coords];
goals = [goalKeys + e  for e in goals];



for i in range(len(coords)):
    print(coords[i]);
    print(goals[i]);
    print("----------------")
