def get_indices_of_item_weights(weights, length, limit):
    arr = dict()
    first = 0
    second = 0

    if length <= 1:
        return None

    for i in range(length):
        arr[weights[i]] = i

    for weight in arr:
        if limit - weight in arr:
            first = arr[weight]
            second = arr[limit - weight]

            # can't figure out how to do this
            if limit - weight == weight:
                first = 1
                second = 0

    print(first, second)
    return (first, second)