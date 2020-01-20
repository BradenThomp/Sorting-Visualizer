from Sorter import Sorter


class SelectionSorter(Sorter):

    def sort(self, data):
        length = data.size

        for i in range(length):

            min_index = i
            for j in range(i+1, length):
                if data.my_list[min_index].height > data.my_list[j].height:
                    min_index = j

            data.my_list[i], data.my_list[min_index] = data.my_list[min_index], data.my_list[i]
            self.force_update(data)



