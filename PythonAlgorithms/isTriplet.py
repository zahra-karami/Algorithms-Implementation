# returns true 
# if there is a Pythagorean 
# Triplet in a given array. 
def isTriplet(arr):    
    n = len(arr)
    for i in range(n):
        for j in range(i + 1,n):
            for k in range(j + 1,n):
                if (arr[i] ** 2) + (arr[j] ** 2) == (arr[k] ** 2):
                    return True
    return False


# Pythagorean Triplet in an array
# Given an array of integers, write a function that returns true 
# if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

# Input: arr[] = {3, 1, 4, 6, 5}
# Output: True
# There is a Pythagorean triplet (3, 4, 5).
def main():
    arr = [3, 2, 4, 6, 5]
    result = triplet(arr)
    print(result)

if __name__ == "__main__":
    main()


