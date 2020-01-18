from Sorter import Sorter


class InsertionSorter(Sorter):

    def sort(self, data):
        length = data.size

        for i in range(1, length):

            key = data.my_list[i]

            j = i-1
            while j >= 0 and key < data.my_list[j]:
                data.my_list[j+1] = data.my_list[j]
                j -= 1
                self.force_update(data)
            data.my_list[j + 1] = key
            self.force_update(data)




