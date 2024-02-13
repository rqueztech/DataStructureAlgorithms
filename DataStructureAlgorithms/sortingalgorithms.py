class SortingAlgorithms:
    # set the class for the insertion sort
    def insertionSort(arr):
        # iterate through the entire array
        for currentIndex in range(0,len(arr)):
            # capture your current key
            key = arr[currentIndex]

            # capture the value previous to the currentIndex
            decreasingIndex = currentIndex - 1

            # create a while loop to iterate down until greater than -1]
            while decreasingIndex > -1 and key <= arr[decreasingIndex]:
                arr[decreasingIndex + 1] = arr[decreasingIndex]
                decreasingIndex = decreasingIndex - 1

            arr[decreasingIndex + 1] = key

        print("Explanation: Insertion Sort. Time complexity: o(n^2):\n\n")
        print(arr)

        return arr


    # set the class for the selection sort
    def selectionSort(arr):
        # create your outer loop which is going to iterate through array
        for currentIndex in range(0, len(arr)):
            # set the current index as the current minimum index
            currentMinimumIndex = currentIndex

            # iterate through every single element after the current minimum index
            for innerIndex in range(currentMinimumIndex + 1, len(arr)):
                # if the inner index is less than, capture it
                if arr[currentMinimumIndex] > arr[innerIndex]:
                    currentMinimumIndex = innerIndex

            # once you are done capturing both indexes, do a swap
            swap = arr[currentMinimumIndex]
            arr[currentMinimumIndex] = arr[currentIndex]
            arr[currentIndex] = swap

        print("Explanation: Time complexity of selection sort: o(n^2). Why is this? because you are iterating thorugh the array again within an iteration. when you do this, the time complexity is exponential because for every iteration. This is one of the worse time complexities, hence completely unideal for real world use, maybe limited cases.\n\n")

        print(arr)

        return arr

    # set the bubble sort
    def bubbleSort(arr):
        print(arr)
        # iterate through the array
        for outerCounter in range(0,len(arr)):
            # create an innerCounter, which will also iterate through every position in the array
            for innerCounter in range(0, len(arr)):
                # if the value at outer counter is greater than inner counter, swap the values
                if arr[outerCounter] < arr[innerCounter]:
                    swap = arr[outerCounter]
                    arr[outerCounter] = arr[innerCounter]
                    arr[innerCounter] = swap

        print(arr)
        return arr








