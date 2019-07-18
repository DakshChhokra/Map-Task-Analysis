import numpy as np;
import math;

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
    segmentedDistance = totalDistance/10;
    arrayOfCentroidPoints = [];
    for i in range(10):
        arrayOfCentroidPoints.append([]);

    counter = 0;
    currentDistance = 0;
    current_point = array[0];
    for element in array:
        currentDistance += distance(element[0], current_point[0], element[1], current_point[1]);
        if(currentDistance > segmentedDistance):
            counter+= 1;
            currentDistance = 0;

        arrayOfCentroidPoints[counter].append(element);

    arrayOfMeans = []
    for centroidArray in arrayOfCentroidPoints:
        arrayOfMeans.append(centeroidnp(centroidArray));
    return arrayOfMeans;

