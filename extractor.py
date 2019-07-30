import numpy as np
import matplotlib.pyplot as plt


class Extractor:
    def __init__(self, file_name):
        self.file_name = file_name;
        self.mainArray = [];

    def return_extracted_array(self):
        self.do_extraction();
        return self.mainArray;

    def do_extraction(self):
        file = open(self.file_name, "r")


        file_reader = file.readlines();
        print(len(file_reader));

        prev_x = []
        prev_y = []
        main_array = []

        for i in range(21):
            prev_x.append("");
            prev_y.append("");

            main_array.append([]);

        for i in range(len(file_reader)):

            single_line = file_reader[i];

            if len(single_line) > 0 and "disconnected" not in single_line:
                round_number = self.get_number(single_line);

                counter = 0;
                for char in file_reader[i]:
                    if char == "(":
                        coord_array = single_line[counter:(len(single_line) - 1)].split(",");
                        x = (coord_array[0])[1:];
                        y = (coord_array[1])[:-1]

                        if x != "-1" and y != "-1" and x != "-" and y != "-" and self.check_prev(x, y, prev_x, prev_y,
                                                                                                 round_number):
                            current_cood = [x, y];
                            main_array[round_number].append(current_cood);
                            prev_x[round_number] = x;
                            prev_y[round_number] = y;

                    counter += 1;
            else:
                print("Line is empty");



        for i in range(len(main_array)):
            for j in range(len(main_array[i])):
                main_array[i][j][0] = float(main_array[i][j][0]);
                main_array[i][j][1] = 0.0 - float(main_array[i][j][1]);


        main_array.pop(0);
        self.mainArray = main_array;

    def check_prev(self, x_val, y_val, x_array, y_array, round_number):
        if x_val == x_array[round_number] and y_val == y_array[round_number]:
            return False;
        else:
            return True;


    @staticmethod
    def plot_array(plottable_array_1, plottable_array_2, centroid1, centroid2, nameOfImage):

        plt.scatter(plottable_array_1[0][0], plottable_array_1[0][1], color="green");
        plt.scatter(plottable_array_1[-1][0], plottable_array_1[-1][1], color="red");
        data = np.array(plottable_array_1)
        plt.plot(data[:, 0], data[:, 1])

        plt.scatter(plottable_array_2[0][0], plottable_array_2[0][1], color="green");
        plt.scatter(plottable_array_2[-1][0], plottable_array_2[-1][1], color="red");
        data = np.array(plottable_array_2)
        plt.plot(data[:, 0], data[:, 1])

        p = 0;
        for x in centroid1:
            if x is not None:
                plt.scatter(x[0], x[1], color="orange");
            p+=1
        for x in centroid2:
            if x is not None:
                plt.scatter(x[0], x[1], color="purple");
            p+=1

        plt.savefig("analysisImage/" + nameOfImage + ".png", dpi=100);
        # plt.show()


        # for i in range(len(plottable_array_1)):
        #     print("This is round " + str(i));
        #     print(plottable_array_1[i]);
        #     print("********");
        #     if len(plottable_array_1[i]) < 1:
        #         print("NOT PLOTTING")
        #     else:
        #         plt.scatter(plottable_array_1[i][0][0], plottable_array_1[i][0][1], color="green");
        #         plt.scatter(plottable_array_1[i][-1][0], plottable_array_1[i][-1][1], color="red");
        #
        #         data = np.array(plottable_array_1[i])
        #         plt.plot(data[:, 0], data[:, 1])
        # for i in range(len(plottable_array_2)):
        #     print("This is round " + str(i));
        #     print(plottable_array_2[i]);
        #     print("********");
        #     if len(plottable_array_2[i]) < 1:
        #         print("NOT PLOTTING")
        #     else:
        #         plt.scatter(plottable_array_2[i][0][0], plottable_array_2[i][0][1], color="green");
        #         plt.scatter(plottable_array_2[i][-1][0], plottable_array_2[i][-1][1], color="red");
        #
        #         data = np.array(plottable_array_2[i])
        #         plt.plot(data[:, 0], data[:, 1])
        # plt.show()

    @staticmethod
    def get_number(my_str):
        return int((''.join(list(filter(str.isdigit, my_str.split(" ")[1])))));




