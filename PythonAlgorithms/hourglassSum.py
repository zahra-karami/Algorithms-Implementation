import numpy as np

# Print the largest (maximum) hourglass sum found in arr
def hourglassSum(arr):
    maxsum = 0
    i = 0
    for i in range (4):
        for j in range(4):
            # get a sub array of 3*3
            sub_arr = arr[i:i+3,j:j+3]

            # calculate the sum of 
            # a b c
            #   d 
            # e f g
            sum_arr = sub_arr[0, :].sum() + sub_arr[1, 1].sum() + sub_arr[2, :].sum()

            if sum_arr > maxsum:
                maxsum = sum_arr       

    print(maxsum)


def main():
    arr = np.array( [
    1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0,
    1, 1, 1, 0, 0, 0,
    0, 0, 2, 4, 4, 0,
    0, 0, 0, 2, 0, 0,
    0, 0, 1, 2, 4, 0]).reshape(6,6)



    hourglassSum(arr)
    

if __name__ == "__main__":
    main()



