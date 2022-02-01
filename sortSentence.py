class Solution:
    def sortSentence(self, s:str)-> str:
        s=[word for word in s.split()]
        print(s)
        
        mid=len(s)//2
        left=s[:mid]
        right=s[mid:]
        self.sortSentence(left.split())
        self.sortSentence(right.split())
        
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
              
        while j<len(right):
            s[k]=right[j]
            j+=1
            k+=1
        print(type(s))
        return s
s = "is2 sentence4 This1 a3"
print(Solution.sortSentence(s,"is2 sentence4 This1 a3"))