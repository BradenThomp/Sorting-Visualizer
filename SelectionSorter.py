from Sorter import Sorter


class SelectionSorter(Sorter):

    i = 0
    j = i + 1
    min_idx = i

    def sort(self, data):

        length = data.size

        for i in range(length):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, length):
                if data.my_list[min_idx] > data.my_list[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            data.my_list[i], data.my_list[min_idx] = data.my_list[min_idx], data.my_list[i]

        for i in range(length):
            self.is_complete = True
            #print(data.my_list[i])



