from Sorter import Sorter


class QuickSorter(Sorter):

    def sort(self, data):
        self.quickSortIterative(data, 0, 63)

    # This function is same in both iterative and recursive
    def partition(self, data, l, h):
        i = (l - 1)
        x = data.my_list[h]

        for j in range(l, h):
            if data.my_list[j].height <= x.height:
                # increment index of smaller element
                i = i + 1
                data.my_list[i], data.my_list[j] = data.my_list[j], data.my_list[i]
                self.force_update(data)

        data.my_list[i + 1], data.my_list[h] = data.my_list[h], data.my_list[i + 1]
        self.force_update(data)
        return i + 1

        # Function to do Quick sort

    # arr[] --> Array to be sorted,
    # l  --> Starting index,
    # h  --> Ending index
    def quickSortIterative(self, data, l, h):

        # Create an auxiliary stack
        size = h - l + 1
        stack = [0] * size

        # initialize top of stack
        top = -1

        # push initial values of l and h to stack
        top = top + 1
        stack[top] = l
        top = top + 1
        stack[top] = h

        # Keep popping from stack while is not empty
        while top >= 0:

            # Pop h and l
            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            # Set pivot element at its correct position in
            # sorted array
            p = self.partition(data, l, h)

            # If there are elements on left side of pivot,
            # then push left side to stack
            if p - 1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            # If there are elements on right side of pivot,
            # then push right side to stack
            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h
