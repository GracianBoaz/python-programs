set1={1,2,3}
set2={4,5,6}

#print(set1)
unionpp=set1.union(set2)
symet=set1.symmetric_difference(set2)
#asymet=set1.asymmetric_difference(set2)
unionpt=set1.difference(set2)


#print(asymet)
print(unionpt)
print(symet)
print(set2.issubset(set1))
print(set2.issuperset(set1))
print(set1.difference_update(set2))
print("di",set1.isdisjoint(set2))
print("di",set1.isdisjoint(unionpp))
print(set1)

#list
list1=[1,2,34,5,1,2]
list2=[77,88,99]
list3=[list1,list2]
print(list3)
    

#tuples
a=(9,5,6,6)
b=(9,44,6)

c=(a,b)
print(c)











