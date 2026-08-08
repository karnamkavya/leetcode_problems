class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        num=0
        curr=''
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch) 
            elif ch=='[':
                st.append((num,curr))
                num=0
                curr=''
            elif ch==']':
                num1,prev=st.pop()
                curr=prev+num1*curr
            else:
                curr+=ch
        return curr
