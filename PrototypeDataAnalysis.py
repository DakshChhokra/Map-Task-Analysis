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


file = open("actualData/goal_key_3.28.2019_9.52.txt", "r")

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


player_object = Extractor("actualData/coordinates_3.28.2019_9.52.txt");
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
    print("length of player array is: " + str(get_length(player_array_current_round)));
    print("The size of player array is " + str(len(player_array_current_round)));
    if len(player_array_current_round) > 1:
        print("Closeness number is " + str(compare_two_paths(goalArray, player_array_current_round)));
        Extractor.plot_array(goalArray, player_array_current_round);
    print("**************");

