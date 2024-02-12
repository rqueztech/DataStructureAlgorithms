class SortingAlgorithms:
    # set the class for the insertion sort
    def insertionSort(arr):
        print(arr)

    # set the class for the selection sort
    def selectionSort(arr):
        # create your outer loop which is going to iterate through array
        for currentIndex in range(0, len(arr) - 1):
            # set the current index as the current minimum index
            currentMinimumIndex = currentIndex

            # iterate through every single element after the current minimum index
            for innerIndex in range(currentMinimumIndex + 1, len(arr) - 1):
                # if the inner index is less than, capture it
                if arr[currentMinimumIndex] > arr[innerIndex]:
                    currentMinimumIndex = innerIndex

            # once you are done capturing both indexes, do a swap
            swap = arr[currentMinimumIndex]
            arr[currentMinimumIndex] = arr[currentIndex]
            arr[currentIndex] = swap

        print(arr)

        print("\nExplanation: Time complexity of selection sort: o(n^2). Why is this? because you are iterating thorugh the array again within an iteration. when you do this, the time complexity is exponential because for every iteration. This is one of the worse time complexities, hence completely unideal for real world use, maybe limited cases.")
