class checkletters:
    def tell(self,l):
        word="akeotpn"
        ans=[]
        flag=0
        for i in l:
            for m in i.lower():
                if m in word:flag=flag+1
            if flag==len(i):
                        ans.append(i)
                        flag=0
            else:
                        flag=0
        return ans
            
l=['Arun', 'Varun', 'kent', 'Eat', 'Pot', 'Net', 'Peak', 'Peacock', 'Zebra', 'Nato', 'Toe', 'Poke', 'Knife', 'Poet', 'Venus', 'Ant']
obj=checkletters()
for i in obj.tell(l):
    print(i)