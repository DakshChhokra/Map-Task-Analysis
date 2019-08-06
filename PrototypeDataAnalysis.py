import re;
import pickle;
from extractor import Extractor;
import math;
import sys;
import numpy as np;
from os import listdir
from os.path import isfile, join

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


# def compare_two_path_with_deletions(arr1, arr2):
#     goal = arr1[:]
#     player = arr2[:]
#     smallestDistance = []
#
#     for x in range(len(goal)):
#         current_goal_point = goal[x];
#         current_smallest_distance = 9999;
#         current_smallest_point = None;
#         for y in range(len(player)):
#             if len(player) > 0:
#                 current_player_point = player[y];
#                 temp_distance = distance(current_goal_point[0], current_player_point[0], current_goal_point[1], current_player_point[1]);
#                 if temp_distance < current_smallest_distance:
#                     current_smallest_distance =  temp_distance;
#                     current_smallest_point = y;
#         else:
#             break;
#     smallestDistance.append(current_smallest_distance);
#     player.pop(current_smallest_point);
#
#     return sum(smallestDistance)/len(smallestDistance);


def distance_short(a1, a2):
    return distance(a1[0], a2[0], a1[1], a2[1]);



def centeroid_python(data):
    if (len(data) != 0):
        x, y = zip(*data)
        l = len(x)
        return sum(x) / l, sum(y) / l


def break_into_segments(array):
    length = len(array);
    totalDistance = sum_given_array(array);
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
    # for x in arrayOfCentroidPoints:
    #     print(l, x, sum_given_array(x));
    #     # if len(x) == 0:
    #     #     arrayOfCentroidPoints.pop(l);
    #     #     print("removed");
    #     l+=1;
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
    return  distance_point;

def getAverage(array):
    return sum(array)/len(array);

def advancedPointMatchingBothWays(a1, a2):
    arr1 = a1.copy();
    arr2 = a2.copy();
    a1a2 = []
    for x in range(len(arr1)):
        minDistance = 100000;
        minPointIndex = -1;
        second_loop = len(arr2);
        if second_loop > 0:
            for y in range(second_loop):
                comparison = distance_short(arr1[x], arr2[y]);
                if comparison < minDistance:
                    minDistance = comparison;
                    minPointIndex = y;
            print("Closest point to {0}, is {1}. Distance between them is {2}".format(arr1[x], arr2[minPointIndex],
                                                                                      minDistance));
            a1a2.append(minDistance);
            arr2.pop(minPointIndex);



    arr1 = a1.copy();
    arr2 = a2.copy();
    a2a1 = []

    for x in range(len(arr2)):
        minDistance = 100000;
        minPointIndex = -1;
        second_loop = len(arr1);
        if second_loop > 0:
            for y in range(second_loop):
                comparison = distance_short(arr2[x], arr1[y]);
                if comparison < minDistance:
                    minDistance = comparison;
                    minPointIndex = y;
            print("Closest point to {0}, is {1}. Distance between them is {2}".format(arr2[x], arr1[minPointIndex],
                                                                                      minDistance));
            a2a1.append(minDistance);
            arr1.pop(minPointIndex);

    arr1 = a1.copy();
    arr2 = a2[::-1];
    a2a1reversed = []

    for x in range(len(arr2)):
        minDistance = 100000;
        minPointIndex = -1;
        second_loop = len(arr1);
        if second_loop > 0:
            for y in range(second_loop):
                comparison = distance_short(arr2[x], arr1[y]);
                if comparison < minDistance:
                    minDistance = comparison;
                    minPointIndex = y;
            print("Closest point to {0}, is {1}. Distance between them is {2}".format(arr2[x], arr1[minPointIndex],
                                                                                      minDistance));
            a2a1reversed.append(minDistance);
            arr1.pop(minPointIndex);

    return getAverage(a1a2), getAverage(a2a1), getAverage(a2a1reversed);


goalKeyAddress = "goal_key_4.20.2019_20.24.txt";
coordinateAddress = "coordinates_4.20.2019_20.24.txt";

all_the_data = {
                'name':[], 'roundNumber':[], 'goalNumber':[],
                'startPoint':[],
                'endPoint':[],
                'terminalPointAverage':[],
                'basicPointMatching':[],
                'lengthDifference':[],
                'apmGoalUser':[],
                'apmUserGoal':[],
                'apmUserGoalReversed':[],
                'centroidDistance':[],
                'scoreBasedOnOG6Parameters':[]
                }

def mainAnalysis(goalKeyAddress, coordinateAddress):
    file = open(goalKeyAddress, "r")

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

    player_object = Extractor(coordinateAddress);
    player_array = player_object.return_extracted_array();

    for round_number in range(len(array_of_rounds)):
        address = "cleanedGoalDirectory/" + array_of_rounds[round_number] + ".p";
        goalArray = pickle.load(open(address, "rb"));
        player_array_current_round = player_array[round_number];
        print("This is round " + str(round_number + 1));
        print("The current goal is " + array_of_rounds[round_number]);
        print(goalArray);
        print("length of goal Array is: " + str(sum_given_array(goalArray)));
        print("The size of goal array is " + str(len(goalArray)));
        print(player_array_current_round);

        if len(player_array_current_round) == 0:
            print("Array is empty");
        else:
            print("length of player array is: " + str(sum_given_array(player_array_current_round)));
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

        print('***************************************************************************')
        print('***************************************************************************')
        print("Starting Similarity Checks")
        print('***************************************************************************')
        print('***************************************************************************')

        if len(player_array_current_round) > 1:
            print("Checking start Point");
            sp = check_terminal_position(goalArray[0], player_array_current_round[0]);

            print("Checking end Point");
            ep = check_terminal_position(goalArray[-1], player_array_current_round[-1]);

            compare_path = compare_two_paths(goalArray, player_array_current_round);
            print("Closeness number is " + str(compare_path));

            length_difference = abs(sum_given_array(goalArray) - sum_given_array(player_array_current_round));
            print("Difference in length is: " + str(length_difference));

            compare_path_with_deletions = advancedPointMatchingBothWays(goalArray, player_array_current_round);
            print("Closeness number when comparing with advanced deletions is " + str(compare_path_with_deletions[0]));

            centroid_number = compare_two_centroid_arrays(centroid_goal, centroid_player);
            print("Centroid closeness number is " + str(centroid_number));

            scores = 0.0;
            print("--------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------")
            print("Start Point Analysis with a tolerance of 50")
            if sp < 50:
                print("SIMILAR");
                scores += 0.5
            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("End Point Analysis with a tolerance of 50")
            if ep < 50:
                print("SIMILAR");
                scores += 0.5
            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("Basic Point matching analysis with a tolerance of 50");
            if compare_path < 50:
                print("SIMILAR");
                scores += 0.5
            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("Basic length analysis with a tolerance of 150");
            if length_difference < 150:
                print("SIMILAR");
                scores += 0.5
            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("Slightly advanced Point matching analysis with a tolerance of 30");
            if compare_path_with_deletions[0] < 30:
                print("SIMILAR");
                scores += 1.0
            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("Centroid analysis with a tolerance of 40");
            if centroid_number < 40:
                print("SIMILAR");
                scores += 1.0;

            else:
                print("NOT SIMILAR");
            print("--------------------------------------------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------")

            print("Final Similarity Score is: " + str(scores) + " / 4");
            nameOfPlot = coordinateAddress[32:-4] + "_" +  str(array_of_rounds[round_number]);
            # Extractor.plot_array(goalArray, player_array_current_round, centroid_goal, centroid_player, nameOfPlot);

            fN = "AnalysisFile.txt";
            f2W = open(fN, 'a');
            f2W.write(coordinateAddress[32:-4] + " " + str(round_number) + " " + array_of_rounds[round_number] + " " +
                      str(round(sp, 4)) + " " + str(round(ep, 4)) + " " + str(round(compare_path, 4)) + " " +
                      str(round(length_difference, 4)) + " " + str(round(compare_path_with_deletions[0], 4)) + " " + str(round(centroid_number, 4)) +
                      " " + str(scores) + " " + "/4.0 \n")
            f2W.close();


            all_the_data['name'].append(coordinateAddress[32:-4]);
            all_the_data['roundNumber'].append(round_number);
            all_the_data['goalNumber'].append(array_of_rounds[round_number]);
            all_the_data['startPoint'].append(sp);
            all_the_data['endPoint'].append(ep);
            all_the_data['terminalPointAverage'].append( (ep + sp)/2.0 );
            all_the_data['basicPointMatching'].append(compare_path);
            all_the_data['lengthDifference'].append(length_difference);
            all_the_data['apmGoalUser'].append(compare_path_with_deletions[0]);
            all_the_data['apmUserGoal'].append(compare_path_with_deletions[1]);
            all_the_data['apmUserGoalReversed'].append(compare_path_with_deletions[2]);
            all_the_data['centroidDistance'].append(centroid_number);
            all_the_data['scoreBasedOnOG6Parameters'].append(scores);

    print("***************************************************************************");




# mainAnalysis(goalKeyAddress, coordinateAddress)

coordinates = "allData/coordinates/"
goalKeys = "allData/goalKey/"









coords = [f for f in listdir(coordinates) if isfile(join(coordinates, f))];
goals = [f for f in listdir(goalKeys) if isfile(join(goalKeys, f))];

coords.sort();
goals.sort();

coords = [coordinates + e  for e in coords];
goals = [goalKeys + e  for e in goals];

fileName = "AnalysisFile.txt";
fileToWrite =  open(fileName,'w');
fileToWrite.write("fileName Round GoalNumber StartPointDifference EndPointDifference SimplePointMatchingDistance LengthDifference AdvancedPointMatchingDistance CentroidDistance FinalSimilarityScoreBasedOnSubjectiveHeuristics \n");
fileToWrite.close();

for i in range(len(coords)):
    print(coords[i]);
    print(goals[i]);
    print("----------------")
    mainAnalysis(goals[i], coords[i]);




print(all_the_data);

# Store data (serialize)
with open('dictionaryAnalysis.pickle', 'wb') as handle:
    pickle.dump(all_the_data, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Load data (deserialize)
with open('dictionaryAnalysis.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

print(all_the_data == unserialized_data)






