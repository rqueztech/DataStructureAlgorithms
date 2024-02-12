class SortingAlgorithms:
    # set the class for the selection sort
    def selectionSort(arr):
        # create your outer loop which is going to iterate through array
        for currentIndex in range(0, len(arr) - 1):
            # set the current index as the current minimum index
            currentMinimumIndex = currentIndex

            # iterate through every single element after the current minimum index
            for innerIndex in range(currentIndex + 1, len(arr) - 1):
                # if the inner index is less than, capture it
                if arr[currentMinimumIndex] < arr[innerIndex]:
                    currentMinimumIndex = innerIndex

            # once you are done capturing both indexes, do a swap
            swap = arr[currentMinimumIndex]
            arr[currentMinimumIndex] = arr[innerIndex]
            arr[innerIndex] = swap

        print(arr)
