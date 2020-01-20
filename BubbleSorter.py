from Sorter import Sorter


class BubbleSorter(Sorter):

    # data: data to be sorted
    def sort(self, data):
        length = data.size

        for i in range(length):
            for j in range(0, length - i - 1):
                if data.my_list[j].height > data.my_list[j+1].height:
                    data.my_list[j], data.my_list[j + 1] = data.my_list[j+1], data.my_list[j]
                    self.force_update(data)






