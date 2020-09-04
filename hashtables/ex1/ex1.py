def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    data = {}

    for i in range(len(weights)):


        data[weights[i]] = i

    for i in range(len(weights)):


        limitweight = limit-weights[i]

        if limitweight in data:

            return(max(i, data[limitweight]), min(i, data[limitweight]))
 
 
    return None
