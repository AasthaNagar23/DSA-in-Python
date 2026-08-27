def topKFrequent(nums, k):

    freq = {}

    # Frequency count
    for num in nums:
        if num not in freq:
            freq[num] = 0

        freq[num] += 1

    # Frequency ke according sort karo
    sorted_nums = sorted(freq, key=freq.get, reverse=True)

    # First k elements
    return sorted_nums[:k]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))