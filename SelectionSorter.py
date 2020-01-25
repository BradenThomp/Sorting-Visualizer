from Sorter import Sorter
from Colors import *


class SelectionSorter(Sorter):

    # data: data to be sorted
    def sort(self, data):
        length = data.size

        for i in range(length):

            min_index = i
            for j in range(i+1, length):
                data.my_list[j].set_color(RED)
                self.force_update()
                if data.my_list[min_index].height > data.my_list[j].height:
                    data.my_list[min_index].set_color(WHITE)
                    min_index = j
                    data.my_list[min_index].set_color(GREEN)
                else:
                    data.my_list[j].set_color(WHITE)

            data.my_list[i], data.my_list[min_index] = data.my_list[min_index], data.my_list[i]
            data.my_list[i].set_color(WHITE)
            self.force_update()



