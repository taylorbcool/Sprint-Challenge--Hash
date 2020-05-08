def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    first = 0
    second = 0

    if length <= 1:
        return None

    for i in range(length):
        cache[weights[i]] = i

    for weight in cache:
        if limit - weight in cache:
            first = cache[weight]
            second = cache[limit - weight]

            # can't figure out how to do this
            if limit - weight == weight:
                first = 1
                second = 0

    return (first, second)