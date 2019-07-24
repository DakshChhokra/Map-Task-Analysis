import re;
import pickle;
from extractor import Extractor;
import math;
import sys;
import numpy as np;

def distance(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

def compare_two_paths(goal, player):
    small_distance_array = []
    for player_point in player:
        current_smallest_distance = sys.maxsize;
        for goal_point in goal:
            current_distance = distance(player_point[0], goal_point[0], player_point[1], goal_point[1]);
            if current_distance < current_smallest_distance:
                current_smallest_distance = current_distance;
        small_distance_array.append(current_smallest_distance);
    return sum(small_distance_array)/len(small_distance_array);

def get_length(array):
    length_of_array = 0;
    current_x = array[0][1];
    current_y = array[0][1]
    for arr1_elements in array:
        length_of_array += distance(current_x, arr1_elements[0], current_y, arr1_elements[1]);
        current_x = arr1_elements[0];
        current_y = arr1_elements[1];
    return  length_of_array;

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

def centeroid_python(data):
    #Remove empty arrays. terrible idea in practice


    # print("big boii")
    # print(data);
    # for x in data:
    #     print("small boi")
    #     print(x);

    if (len(data) != 0):
        x, y = zip(*data)
        l = len(x)
        return sum(x) / l, sum(y) / l


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
        if currentDistance > segmentedDistance:
            print("arrayOfCentroidPoints[counter]", arrayOfCentroidPoints[counter]);
            print("counter", counter);
            print("currentDistance", currentDistance);
            counter+= 1;
            currentDistance = 0;

        arrayOfCentroidPoints[counter].append(element);

        current_point = element;

    array_of_means = []
    print("full array", arrayOfCentroidPoints);
    for centroidArray in arrayOfCentroidPoints:
        array_of_means.append(centeroid_python(centroidArray));

    return array_of_means;
def check_terminal_position(p1, p2):
    distance_point = distance(p1[0], p2[0], p1[1], p2[1]);
    print("distance  between terminal points is " + str(distance_point));
    return  distance_point < 75;


file = open("goal_key_4.20.2019_20.24.txt", "r")

file_reader = file.readlines();

array_of_rounds = [];
for singleLine in file_reader:
    search_box_result = "";
    try:
        search_box_result = re.search('/goal(.*?)\?', singleLine).group(0);
        search_box_result = search_box_result[1:-5];
        array_of_rounds.append(search_box_result);

    except AttributeError:
        search_box_result = singleLine;


player_object = Extractor("coordinates_4.20.2019_20.24.txt");
player_array = player_object.return_extracted_array();

for round_number in range(len(array_of_rounds)):
    address = "cleanedGoalDirectory/" + array_of_rounds[round_number] + ".p";
    goalArray = pickle.load(open(address, "rb"));
    player_array_current_round = player_array[round_number];
    print("This is round " + str(round_number + 1));
    print("The current goal is " + array_of_rounds[round_number]);
    print(goalArray);
    print("length of goal Array is: " + str(get_length(goalArray)));
    print("The size of goal array is " + str(len(goalArray)));
    print(player_array_current_round);

    if len(player_array_current_round) == 0:
        print("Array is empty");
    else:
        print("length of player array is: " + str(get_length(player_array_current_round)));
        print("The size of player array is " + str(len(player_array_current_round)));

    print('***************************************************************************')

    print("Centroid Time");
    print("Goal Array centroid are: ")
    centroid_goal = break_into_segments(goalArray);
    print(centroid_goal);
    print("---------------------------------")
    print("Player Array centroid are: ")
    if len(player_array_current_round) == 0:
        print("Array is empty and has centroid");
    else:
        centroid_player = break_into_segments(player_array_current_round);
        print(centroid_player);



    print("Advanced Closeness level is ")
    print('***************************************************************************')





    if len(player_array_current_round) > 1:
        print("Checking start Point");
        sp = check_terminal_position(goalArray[0], player_array_current_round[0]);

        print("Checking end Point");
        ep = check_terminal_position(goalArray[-1], player_array_current_round[-1]);

        cn = compare_two_paths(goalArray, player_array_current_round);
        print("Closeness number is " + str(cn));

        if sp and ep and (cn < 75):
            print("SIMILAR");
        else:
            print("NOT SIMILAR");

        Extractor.plot_array(goalArray, player_array_current_round);
    print("**************");




