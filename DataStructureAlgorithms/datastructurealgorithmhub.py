import binarysearch
import sortingalgorithms
import generaterandomarray

def main():
    randomarray = generaterandomarray.generate_random_array(400,1,2000)
    #sortingarray = sortingalgorithms.SortingAlgorithms.selectionSort(randomarray)
    insertionarray = sortingalgorithms.SortingAlgorithms.insertionSort(randomarray)

    print(insertionarray)

    currentvalue = int(input("Enter Value: "))
    indexfound = binarysearch.binary_search(currentvalue)

    return 0

if __name__ == '__main__':
    main()
