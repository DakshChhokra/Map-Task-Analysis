import pickle;
import matplotlib.pyplot as plt


with open('dictionaryAnalysis.pickle', 'rb') as handle:
    data = pickle.load(handle)

#normalization
for i in list(data.keys()):
    print(i);
    print(data[i]);


for i in list(data.keys()):
    if i != 'name' and i != 'roundNumber' and i != 'goalNumber' and i != 'scoreBasedOnOG6Parameters':
        print("normalizing {0}".format(i));
        array = data[i];
        minVal = min(array);
        maxVal = max(array);

        newArray = []
        for j in array:
            newElement = (j - minVal) / (maxVal - minVal);
            newArray.append(newElement);
        data[i] = newArray;



for i in list(data.keys()):
    print(i);
    print(data[i]);

emptyX = [];
for i in range(len(data['terminalPointAverage'])):
    emptyX.append(i);

for i in list(data.keys()):
    if i != 'name' and i != 'roundNumber' and i != 'goalNumber' and i != 'scoreBasedOnOG6Parameters':
        plt.scatter(emptyX, data[i]);
plt.show();


#Writing normalized data to a text file
fileName = "NormalizedData.txt";
fileToWrite =  open(fileName,'w');
fileToWrite.write("name roundNumber goalNumber startPoint endPoint terminalPointAverage basicPointMatching lengthDifference apmGoalUser apmUserGoal apmUserGoalReversed centroidDistance scoreBasedOnOG6Parameters \n");


for i in range(len(data['name'])):
    line = "";
    for j in list(data.keys()):
        line += str(data[j][i]);
        line += " ";
    line += "\n";
    print("Writing the following piece of data now: {0}".format(line));
    fileToWrite.write(line);


fileToWrite.close();