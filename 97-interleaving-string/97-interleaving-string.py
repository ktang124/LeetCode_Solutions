class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
           
        tup = set()
        tup.add((0,0))
        #at the start, we have used none of the letters so 
        #we are pointing at index 0 on s1 and s2
        
        for idx, letter in enumerate(s3):
            if len(tup) == 0:
                return False
            states = set()
            #states keeps track of what possible two pointers
            #we could be at
            for pair in tup:
                if pair[0] < len(s1) and s1[pair[0]] == letter:
                    #use the letter from s1
                    states.add(tuple([pair[0]+1, pair[1]]))
                if pair[1] < len(s2) and s2[pair[1]] == letter:
                    #use the letter from s2
                    states.add(tuple([pair[0], pair[1]+1]))
                    
            tup = states
            
            #did we consume all the letters from s1 and s2 by the end?
        return (len(s1),len(s2)) in tup