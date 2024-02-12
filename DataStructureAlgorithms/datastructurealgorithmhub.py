import binarysearch
import sortingalgorithms
import generaterandomarray
import copy

def compare_memory_addresses(randomarray, sortingarray, insertionarray):
    areunique = False

    if randomarray is not sortingarray or sortingarray is not insertionarray:
        areunique = True

    else:
        areunique = False

    return areunique

def main():
    randomarray = generaterandomarray.generate_random_array(400,1,2000)
    sortingarray = sortingalgorithms.SortingAlgorithms.selectionSort(copy.deepcopy(randomarray))
    insertionarray = sortingalgorithms.SortingAlgorithms.insertionSort(copy.deepcopy(randomarray))

    currentvalue = int(input("Enter Value: "))
    indexfound = binarysearch.binary_search(currentvalue)

    areunique = compare_memory_addresses(randomarray, sortingarray, insertionarray)

    print(areunique)

    return 0

if __name__ == '__main__':
    main()
