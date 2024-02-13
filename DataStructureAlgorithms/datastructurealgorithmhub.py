import binarysearch
import sortingalgorithms
import generaterandomarray
import copy

def compare_memory_addresses(randomarray, sortingarray, insertionarray):
    areunique = False

    if randomarray is not sortingarray and sortingarray is not insertionarray:
        areunique = True

    else:
        areunique = False

    return areunique

def main():
    while 1:
        option = input("Enter Operation: ")
        randomarray = generaterandomarray.generate_random_array(400,1,3001)

        if option == '1':
            print("\nselectionSort()")
            sortingarray = sortingalgorithms.SortingAlgorithms.selectionSort(copy.deepcopy(randomarray))

        elif option == '2':
            print("\ninsertionSort()")
            insertionarray = sortingalgorithms.SortingAlgorithms.insertionSort(copy.deepcopy(randomarray))

        elif option == '3':
            bubblearray = sortingalgorithms.SortingAlgorithms.bubbleSort(copy.deepcopy(randomarray))
            print("\nbubbleSort()")

    return 0

if __name__ == '__main__':
    main()
