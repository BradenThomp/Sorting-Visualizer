from Sorter import Sorter


class SelectionSorter(Sorter):

    i = 0
    j = i + 1
    min_idx = 0

    def sort(self, data):

        length = data.size

        if self.i < length:

            if self.j < length:
                if data.my_list[self.min_idx] > data.my_list[self.j]:
                    self.min_idx = self.j
                self.j = self.j + 1

            else:
                data.my_list[self.i], data.my_list[self.min_idx] = data.my_list[self.min_idx], data.my_list[self.i]
                self.updatescreen(data)
                self.j = self.i + 1

                self.i = self.i + 1
                self.min_idx = self.i

        else:
            self.is_complete = True




