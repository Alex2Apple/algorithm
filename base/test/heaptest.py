from heapsort.heapsort import *

def main():
    l1 = [67, 64, 60, 58, 57, 55, 52, 43, 40, 32, 28, 20, 18, 15, 8, 3]
    l1.reverse()
    l2 = [55, 45, 38, 29, 25, 23, 20, 18, 12, 6, 4]
    l2.reverse()
    l3 = [47, 35, 31, 22, 17, 14, 9, 5, 1]
    l3.reverse()
    l4 = [51, 43, 40, 37, 35, 31, 25, 19, 17, 13, 7]
    l4.reverse()
    output = []
    heap = Heap(4, False)
    source = [d for d in generator(l1, l2, l3, l4)]
    heap.build(source)
    recursive_merge([l1, l2, l3, l4], out = output, sort = heap)
    print(output)
    
if __name__ == '__main__':
    main()