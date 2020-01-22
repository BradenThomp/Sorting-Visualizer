from Sorter import Sorter


class QuickSorter(Sorter):

    def sort(self, data):
        self.quick_sort_iterative(data, 0, 63)

    # sorts a partition
    def partition(self, data, starting_index, ending_index):
        i = (starting_index - 1)
        x = data.my_list[ending_index]

        for j in range(starting_index, ending_index):
            if data.my_list[j].height <= x.height:
                # increment index of smaller element
                i = i + 1
                data.my_list[i], data.my_list[j] = data.my_list[j], data.my_list[i]
                self.force_update()

        data.my_list[i + 1], data.my_list[ending_index] = data.my_list[ending_index], data.my_list[i + 1]
        self.force_update()
        return i + 1

    # data: Array to be sorted
    def quick_sort_iterative(self, data, starting_index, ending_index):

        # Create an auxiliary stack
        size = ending_index - starting_index + 1
        stack = [0] * size

        # initialize top of stack
        top = -1

        # push initial values of l and h to stack
        top = top + 1
        stack[top] = starting_index
        top = top + 1
        stack[top] = ending_index

        # Keep popping from stack while is not empty
        while top >= 0:

            # Pop h and l
            ending_index = stack[top]
            top = top - 1
            starting_index = stack[top]
            top = top - 1

            # Set pivot element at its correct position in
            # sorted array
            p = self.partition(data, starting_index, ending_index)

            # If there are elements on left side of pivot,
            # then push left side to stack
            if p - 1 > starting_index:
                top = top + 1
                stack[top] = starting_index
                top = top + 1
                stack[top] = p - 1

            # If there are elements on right side of pivot,
            # then push right side to stack
            if p + 1 < ending_index:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = ending_index
