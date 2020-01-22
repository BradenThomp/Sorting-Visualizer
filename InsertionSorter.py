from Sorter import Sorter


class InsertionSorter(Sorter):

    # data: data to be sorted
    def sort(self, data):
        length = data.size

        for i in range(1, length):

            key = data.my_list[i]

            j = i-1
            while j >= 0 and key.height < data.my_list[j].height:
                data.my_list[j+1] = data.my_list[j]
                j -= 1
                self.force_update()
            data.my_list[j + 1] = key
            self.force_update()




