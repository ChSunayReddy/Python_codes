from collections import Counter

def countAnagrams(dictionay, query):
    # Create a list of character frequency counts for each word in dictionay
    dictionay_counts = [Counter(word) for word in dictionay]
    
    result = []
    
    # For each word in query, check how many anagrams exist in dictionay
    for word in query:
        word_count = Counter(word)
        anagram_count = sum(1 for count in dictionay_counts if count == word_count)
        result.append(anagram_count)
    
    return result

# Driver code
dictionay = ["listen", "silent", "enlist", "hello", "world"]
query = ["inlets", "silent", "elloh", "hello"]
print(countAnagrams(dictionay, query))  