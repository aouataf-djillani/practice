"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".

"""

class Solution:
    def sortSentence(self, s:str)-> str:
        if type(s)==str:
            s=[word for word in s.split()]
        
        if len(s)<=1:
            return ''.join(e[:-1] for e in s)
        """
        divide
        """
        
        
        mid=len(s)//2
        left=s[:mid]
        right=s[mid:]
        self.sortSentence(left)
        self.sortSentence(right)
        """
        merge
        """
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i][-1]<right[j][-1]:
                s[k]=left[i]
                i+=1
            else:
                s[k]=right[j]
                j+=1
                
            k+=1
        """
        if left sublist is longer than the right one 
        """  
       
        while i<len(left):
            s[k]=left[i]
            i+=1
            k+=1
        """
        if right sublist is longer than the left one 
        """       
        while j<len(right):
            s[k]=right[j]
            j+=1
            k+=1
        
        return ' '.join(e[:-1] for e in s)
        