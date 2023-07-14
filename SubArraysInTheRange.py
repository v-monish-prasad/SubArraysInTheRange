def findSubArraysInTheRange(array, B, C):
    if not array:
        return "Empty Array."

    subarray = []

    for i in range(B, C + 1):
        subarray.append(array[i])

    return subarray


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    B = int(input())
    C = int(input())
    print(findSubArraysInTheRange(array, B, C))
