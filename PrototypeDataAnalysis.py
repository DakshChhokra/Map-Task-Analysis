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


def compare_two_centroid_arrays(arr1, arr2):
    final_array = [];
    for x in range(len(arr1)):
        if (arr1[x] is not None) and (arr2[x] is not None):
            final_array.append(distance(arr1[x][0], arr2[x][0], arr1[x][1], arr2[x][1]));
    return sum(final_array)/len(final_array);

def sum_given_array(arr):
    if len(arr) == 0 or arr is None:
        return 0;
    else:
        returnable = 0.0;
        for x in range(len(arr)):
            if x != 0:
                returnable += distance(arr[x][0], arr[x-1][0], arr[x][1], arr[x-1][1]);
        return returnable;

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


def compare_two_path_with_deletions(arr1, arr2):
    goal = arr1[:]
    player = arr2[:]
    small_distance_array = [];
    for player_point in player:
        current_smallest_distance = sys.maxsize;
        current_smallest_point = None;
        if len(goal) != 0:
            for goal_point in goal:
                current_distance = distance(player_point[0], goal_point[0], player_point[1], goal_point[1]);
                if current_distance < current_smallest_distance:
                    current_smallest_distance = current_distance;
                    current_smallest_point = goal_point;
            small_distance_array.append(current_smallest_distance);
            goal.remove(current_smallest_point);
        else:
            break;
    return sum(small_distance_array) / len(small_distance_array);

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
    if (len(data) != 0):
        x, y = zip(*data)
        l = len(x)
        return sum(x) / l, sum(y) / l


def break_into_segments(array):
    length = len(array);
    totalDistance = get_length(array);
    segmentedDistance = totalDistance/10;
    print("Cutoff is: " + str(segmentedDistance));
    arrayOfCentroidPoints = [];
    for i in range(15):
        arrayOfCentroidPoints.append([]);

    counter = 0;
    currentDistance = 0;
    current_point = array[0];
    for element in array:
        added_distance = distance(element[0], current_point[0], element[1], current_point[1]);
        tempDistance = currentDistance + added_distance;
        if tempDistance > segmentedDistance:
            # print("counter", counter);
            # print("length of current segment is: " + str(currentDistance));
            # print("arrayOfCentroidPoints[counter]", arrayOfCentroidPoints[counter]);
            counter+= 1;
            currentDistance = 0;

        currentDistance += added_distance;
        arrayOfCentroidPoints[counter].append(element);
        current_point = element;

    # print("************************************************************************************************************");
    l = 0;
    # print("The segmented arrays are")
    for x in arrayOfCentroidPoints:
        print(l, x, sum_given_array(x));
        # if len(x) == 0:
        #     arrayOfCentroidPoints.pop(l);
        #     print("removed");
        l+=1;
    # print("Final length of this is: " + str(len(arrayOfCentroidPoints)));
    # print("************************************************************************************************************");

    array_of_means = []
    for centroidArray in arrayOfCentroidPoints:
        array_of_means.append(centeroid_python(centroidArray));

    # print("Array of means");
    # m = 0;
    # for x in array_of_means:
    #     print(m, x);
    #     m+=1;

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

        compare_path = compare_two_paths(goalArray, player_array_current_round);
        print("Closeness number is " + str(compare_path));

        compare_path_with_deletions = compare_two_path_with_deletions(goalArray, player_array_current_round);
        print("Closeness number when comparing with advanced deletions is " + str(compare_path_with_deletions));

        centroid_number = compare_two_centroid_arrays(centroid_goal, centroid_player);
        print("Centroid closeness number is " + str(centroid_number));


        print("--------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        print("Start Point and End Point Analysis with a tolerance of 75")
        if sp and ep:
            print("SIMILAR");
        else:
            print("NOT SIMILAR");
        print("--------------------------------------------------------------------------------------------")
        print("Basic Point matching analysis with a tolerance of 50");
        if compare_path < 50:
            print("SIMILAR");
        else:
            print("NOT SIMILAR");
        print("--------------------------------------------------------------------------------------------")
        print("Slightly advanced Point matching analysis with a tolerance of 40");
        if compare_path_with_deletions < 40:
            print("SIMILAR");
        else:
            print("NOT SIMILAR");
        print("--------------------------------------------------------------------------------------------")
        print("Centroid analysis with a tolerance of 40");
        if centroid_number < 40:
            print("SIMILAR");
        else:
            print("NOT SIMILAR");
        print("--------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        Extractor.plot_array(goalArray, player_array_current_round, centroid_goal, centroid_player);
    print("***************************************************************************");




