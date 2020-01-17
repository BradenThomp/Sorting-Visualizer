from Sorter import Sorter


class BubbleSorter(Sorter):

    i = 0
    j = 0

    def sort(self, data):
        length = data.size

        if self.i < length:

            if self.j < length-self.i-1:

                if data.my_list[self.j] > data.my_list[self.j + 1]:
                    temp = data.my_list[self.j]
                    data.my_list[self.j] = data.my_list[self.j+1]
                    data.my_list[self.j+1] = temp

                    self.updatescreen(data)
                self.j = self.j + 1

            else:
                self.j = 0
                self.i = self.i + 1






