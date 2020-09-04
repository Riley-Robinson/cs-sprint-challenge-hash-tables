def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    d = dict()
    #sets the dictionary

    result = []
    #set and empty array

    for i in a:
    #loop through
        
        d[i] = 1
        if i != 0 and -i in d:
        # runs a check to see if the number is not 0, and that it also has a negative number counterpart

            result.append(abs(i))
            # appendit to the results

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
