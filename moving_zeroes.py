"""https://www.codewars.com/kata/52597aa56021e91c93000cb0"""
def move_zeros(lst):
# This list assures we copy the non-zero elements in the right order
    output = [item for item in lst if item != 0]

# Then we count how many zeroes we need to add to the end of the previous list
    zeroes = lst.count(0)
    for number in range(zeroes):
    # And we do so
        output.append(0)
    return output
