class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for ch in s:
            if ch  in "({[":
                st.append(ch)
            else:
                if not st:
                    return False
                if ch== ')' and st[-1]!='(':
                    return False
                if ch== '}' and st[-1]!='{':
                    return False
                if ch== ']' and st[-1]!='[':
                    return False
                st.pop()

        if len(st) == 0 : 
            return True 
        else : 
            return False