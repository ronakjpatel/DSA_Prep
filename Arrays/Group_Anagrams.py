''' 
#49 Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

strs = ["eat","tea","tan","ate","nat","bat"]
h_map ={}

#approach 1
for word in strs:
    sorted_word = ''.join(sorted(word))
    print(sorted_word)
    print(word)
    if sorted_word in h_map:
        h_map[sorted_word].append(word)
    else:
        h_map[sorted_word] = [word]
        
print(h_map.values())

#apprach 2 

'''
rather than sorting the each word and then sotring in the hashmap, we can actually 
make one hot encoding type of array of 26 (total # of alphabets) and then as we iterate 
through the each character by character of the each word we can basically store 1 on
the appropriate indexes of the array(tuple is more precise word here)

for example:
first letter is a suppose its ASCII val is 80
now second letter b should be having ASCII val of 81 and so on for all 26 alphabets

so inorder to find the right index to make 1 in the one hot tuple, we can use this simple trick

ord(curr_character) - ord('a') # this will give you index suppose curr_character = b then it will be 81-80=1

and then simply use this one hot tuple as a key and value as a list of words that are similart 

in this way we saved the sorting efforts we were doing previously making it a effective algo. 
'''

