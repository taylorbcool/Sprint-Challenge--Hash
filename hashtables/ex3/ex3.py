def intersection(arrays):
    cache = {}
    result = []

    for arr in arrays:
        for item in arr:
            # if item isn't in cache, start counter var
            if item not in cache:
                cache[item] = 1
            # if item is in cache, increase counter var
            elif item in cache:
                cache[item] += 1
            # if counter var is equal to length of the array of arrays, it must be an intersect, add it to result
            if cache[item] == len(arrays):
                result.append(item)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
