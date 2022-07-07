#Merging of collections 
#  list merging 
# l=[10,20,30,40,50]
# s=[100,200,'Surendra']
# z=l+s
# print(z)

# l=[10,20,30,40,50]
# s=[100,200,'Surendra']
# z=[*l,*s]
# print(z)




#tuple merging 
# l=(10,20,30,40,50)
# s=(100,200,'Surendra')
# z=l+s
# print(z)

#set merging
# s1={10,20,30,40}
# s2={50,'surendra',100}
# s3=s1+s2  #TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(s3)

# solution 
# s1={10,20,30,40}
# s2={50,'surendra',100}
# s3={*s1,*s2}
# print(s3)

# d1={1:'surendra',2:'priyanka'}
# d2={3:'rahul',4:'zini'}

# d3={*d1,*d2}
# print(d3)

#solution
# d1={1:'surendra',2:'priyanka'}
# d2={3:'rahul',4:'zini'}

# d3={**d1,**d2}
# print(d3)
