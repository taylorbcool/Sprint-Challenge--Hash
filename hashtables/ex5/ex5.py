# hash function
def hash_func(key):
    fnv_offset_basis = 0xcbf29ce484222325
    fnv_prime = 0x100000001b3
    fnv_size = 2**64

    fnv_hash = fnv_offset_basis

    for char in key:
        fnv_hash = (fnv_hash * fnv_prime) % fnv_size
        fnv_hash = fnv_hash ^ ord(char)

    return fnv_hash

# change input to paths because why was it paths in the example input but not here??
def finder(paths, queries):
    cache = {}
    result = []

    for path in paths:
        # create file name from path for storing as key
        file_name = path.split('/')[-1]
        hash_key = hash_func(file_name)
        
        # if file name is in cache add the current path to that key
        if hash_key in cache:
            cache[hash_key].append(path)

        # if file name isn't in cache, add it and its path
        if hash_key not in cache:
            cache[hash_key] = [path]
    
    for query in queries:
        hash_key = hash_func(query)
        if hash_key in cache:
            result.append(cache[hash_key])

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
