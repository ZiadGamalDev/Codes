# i. Array Concatenation
def concatenate_arrays(arr1, arr2):
    return arr1 + arr2

# ii. Array Compression
def compress_array(arr):
    if not arr:
        return []
    compressed = [arr[0]]
    for elem in arr[1:]:
        if elem != compressed[-1]:
            compressed.append(elem)
    return compressed

# iii. Array of Arrays
def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def access_element(matrix, row, col):
    return matrix[row][col]

def modify_element(matrix, row, col, value):
    matrix[row][col] = value

# iv. Copying Array
def copy_array(arr):
    return arr[:]

# v. Copying Inverted Array
def copy_inverted_array(arr):
    return arr[::-1]

# Example usage
if __name__ == "__main__":
    # Array Concatenation
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    print("Concatenated Array:", concatenate_arrays(arr1, arr2))

    # Array Compression
    arr = [1, 1, 2, 2, 3, 3, 3, 4, 4]
    print("Compressed Array:", compress_array(arr))

    # Array of Arrays
    matrix = create_matrix(3, 3)
    modify_element(matrix, 1, 1, 5)
    print("Accessed Element:", access_element(matrix, 1, 1))

    # Copying Array
    arr = [1, 2, 3, 4]
    copied_arr = copy_array(arr)
    print("Copied Array:", copied_arr)

    # Copying Inverted Array
    inverted_arr = copy_inverted_array(arr)
    print("Inverted Array:", inverted_arr)
