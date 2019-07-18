import numpy as np;
import math;
import sys;

def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

def get_length(array):
    length_of_array = 0;
    current_x = array[0][1];
    current_y = array[0][1]
    for arr1_elements in array:
        length_of_array += distance(current_x, arr1_elements[0], current_y, arr1_elements[1]);
        current_x = arr1_elements[0];
        current_y = arr1_elements[1];
    return  length_of_array;

def centeroidnp(arr):
    length = arr.shape[0]
    sum_x = np.sum(arr[:, 0])
    sum_y = np.sum(arr[:, 1])
    return sum_x/length, sum_y/length

def break_into_segments(array):
    length = len(array);
    totalDistance = get_length(array);
    segmentedDistance = totalDistance/5;
    arrayOfCentroidPoints = [];
    for i in range(10):
        arrayOfCentroidPoints.append([]);

    counter = 0;
    currentDistance = 0;
    current_point = array[0];
    for element in array:
        currentDistance += distance(element[0], current_point[0], element[1], current_point[1]);
        print("element", element);
        print("currentDistance", currentDistance);
        if(currentDistance > segmentedDistance):
            print("arrayOfCentroidPoints[counter]", arrayOfCentroidPoints[counter]);
            print("counter", counter);
            counter+= 1;
            currentDistance = 0;

        arrayOfCentroidPoints[counter].append(element);

    arrayOfMeans = []
    for centroidArray in arrayOfCentroidPoints:
        arrayOfMeans.append(centeroidnp(centroidArray));
    return arrayOfMeans;

testArray = []
for i in range(20):
    currentArray = [0, (5 * i)];
    testArray.append(currentArray);

print(testArray);
print("length of goal Array is: " + str(get_length(testArray)));
print("The size of goal array is " + str(len(testArray)));
print("Threshold is " + str(95/5));
returned = break_into_segments(testArray);
print(returned);



sys.stdout.flush()
