import binarysearch
import sortingalgorithms
import generaterandomarray

def main():
    randomarray = generaterandomarray.generate_random_array(400,1,2000)
    sortingalgorithms.SortingAlgorithms.selectionSort(randomarray)

    currentvalue = int(input("Enter Value: "))
    indexfound = binarysearch.binary_search(currentvalue)

    return 0

if __name__ == '__main__':
    main()
