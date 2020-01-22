from Sorter import Sorter


class MergeSorter(Sorter):

    def sort(self, data):

        current_size = 1

        # Outer loop for traversing Each
        # sub array of current_size
        while current_size < len(data.my_list) - 1:

            left = 0
            # Inner loop for merge call
            # in a sub array
            # Each complete Iteration sorts
            # the iterating sub array
            while left < len(data.my_list) - 1:
                # mid index = left index of
                # sub array + current sub
                # array size - 1
                mid = left + current_size - 1

                # (False result,True result)
                # [Condition] Can use current_size
                # if 2 * current_size < len(a)-1
                # else len(a)-1
                right = ((2 * current_size + left - 1,
                          len(data.my_list) - 1)[2 * current_size
                                      + left - 1 > len(data.my_list) - 1])

                # Merge call for each sub array
                self.merge(data, left, mid, right)
                left = left + current_size * 2

            # Increasing sub array size by
            # multiple of 2
            current_size = 2 * current_size

    def merge(self, data, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = data.my_list[l + i]

        for i in range(0, n2):
            R[i] = data.my_list[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i].height > R[j].height:
                data.my_list[k] = R[j]
                j += 1
            else:
                data.my_list[k] = L[i]
                i += 1
            k += 1
            self.force_update()

        while i < n1:
            data.my_list[k] = L[i]
            self.force_update()
            i += 1
            k += 1

        while j < n2:
            data.my_list[k] = R[j]
            self.force_update()
            j += 1
            k += 1