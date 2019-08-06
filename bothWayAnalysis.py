from extractor import Extractor;
import re;
import pickle;
import math;

def distance_long(xi,xii,yi,yii):
    sq1 = (xi-xii)*(xi-xii)
    sq2 = (yi-yii)*(yi-yii)
    return math.sqrt(sq1 + sq2)

def distance(a1, a2):
    return distance_long(a1[0], a2[0], a1[1], a2[1]);

def compare_two_path_with_deletions(arr1, arr2):
    goal = arr1[:]
    player = arr2[:]
    smallestDistance = []

    for x in range(len(goal)):
        current_goal_point = goal[x];
        current_smallest_distance = 9999;
        current_smallest_point = None;
        for y in range(len(player)):
            if len(player) > 0:
                current_player_point = player[y];
                temp_distance = distance_long(current_goal_point[0], current_player_point[0], current_goal_point[1], current_player_point[1]);
                if temp_distance < current_smallest_distance:
                    current_smallest_distance =  temp_distance;
                    current_smallest_point = y;
        else:
            break;
        smallestDistance.append(current_smallest_distance);
        player.pop(current_smallest_point);

    print("smallest distance array is: {0}".format(smallestDistance));
    return sum(smallestDistance)/len(smallestDistance);

def sum_given_array(arr):
    if len(arr) == 0 or arr is None:
        return 0;
    else:
        returnable = 0.0;
        for x in range(len(arr)):
            if x != 0:
                returnable += distance_long(arr[x][0], arr[x-1][0], arr[x][1], arr[x-1][1]);
        return returnable;

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
                comparison = distance(arr1[x], arr2[y]);
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
                comparison = distance(arr2[x], arr1[y]);
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
                comparison = distance(arr2[x], arr1[y]);
                if comparison < minDistance:
                    minDistance = comparison;
                    minPointIndex = y;
            print("Closest point to {0}, is {1}. Distance between them is {2}".format(arr2[x], arr1[minPointIndex],
                                                                                      minDistance));
            a2a1reversed.append(minDistance);
            arr1.pop(minPointIndex);

    return a1a2, a2a1, a2a1reversed;




goalKeyAddress = "goal_key_4.20.2019_20.24.txt";
coordinateAddress = "coordinates_4.20.2019_20.24.txt";
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

finaldataset = [[],[],[]];
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
    print('***************************************************************************')
    print('***************************************************************************')
    print('***************************************************************************')
    print('***************************************************************************')

    if(len(player_array_current_round) > 0):
        returned = advancedPointMatchingBothWays(goalArray, player_array_current_round);
        finaldataset[0].append(sum(returned[0]) / len(returned[0]));
        finaldataset[1].append(sum(returned[1]) / len(returned[1]));
        finaldataset[2].append(sum(returned[2]) / len(returned[2]));
        print("averages", sum(returned[0]) / len(returned[0]), sum(returned[1]) / len(returned[1]),
              sum(returned[2]) / len(returned[2]));

        print("Old way is this: " + str(compare_two_path_with_deletions(goalArray, player_array_current_round)))
    else:
        print("DO NOT DO ANALYSIS");



    print('***************************************************************************')
    print('***************************************************************************')
    print('***************************************************************************')
    print('***************************************************************************')
    print('***************************************************************************')

#
#
# sample1 = [1, 2, 3, 4];
# sample2 = [1.1, 2.1, 3.3, 4.2, 4.5];
#
# returned = advancedPointMatchingBothWays(sample1, sample2);
#
# print("sample1", sample1);
# print("sample2", sample2);
# print("result", returned);
# print("averages", sum(returned[0])/len(returned[0]), sum(returned[1])/len(returned[1]), sum(returned[2])/len(returned[2]));
#


print("############################################################################################################")
print("############################################################################################################")
print("############################################################################################################")


from numpy import cov;
from scipy.stats import pearsonr;
covariance = cov(finaldataset[0], finaldataset[1])
print(covariance)
corr, _ = pearsonr(finaldataset[2], finaldataset[1])
print('Pearsons correlation: %.3f' % corr)