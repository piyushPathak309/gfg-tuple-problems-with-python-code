#************************************************************** Tuple Programming *****************************************************






# Python program to Find the size of a Tuple

tup=(3,4,5,6)
print(len(tup))



# Python – Maximum and Minimum K elements in Tuple

# Input : test_tup = (3, 7, 1, 18, 9), k = 2
# Output : (3, 1, 9, 18)

list=[]
test_tup = (3, 7, 1, 18, 9)
lis=sorted(test_tup)
list.append( ( lis[-1],lis[-2],lis[0],lis[1] ) )
print(list[0])


# Create a list of tuples from given list having number and its cube in each tuple

# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

list = [1, 2, 3]
lis1=[]
for i in list:
    lis1.append(i*i*i)
k=list(zip(list,lis1))
print(k)



# Python – Adding Tuple to List and vice – versa

# test_tup = (9, 10)
# The original list is : [5, 6, 7]
# The container after addition : [5, 6, 7, 9, 10]

final_list =  [5, 6, 7] +  list((9, 10))





# Python – Sum of tuple elements






# Python – Modulo of tuple elements


# The original tuple 1 : (10, 4, 5, 6)
# The original tuple 2 : (5, 6, 7, 5)
# The modulus tuple : (0, 4, 5, 1)

tup1=(10, 4, 5, 6)
tup2=(5, 6, 7, 5)
lis=[]
for i in tuple(zip(tup1,tup2)):
    for j in range(len(i)-1):
        lis.append(i[j]%i[j+1])
print(lis)


# Python – Row-wise element Addition in Tuple Matrix

#
# Input : test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]] cus_eles = [1, 2]
# Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]
test_list = [[('Gfg', 3)], [('best', 1)]]
cus_eles = [1,2]
lis=[]
for key,  val in zip(test_list, cus_eles):
    for i in key:
        lis.append([i+(val,)])






# Python – Update each element in tuple list

elem=4
# The original list ,
lis =[(1, 3, 4), (2, 4, 6), (3, 8, 1)]
# List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]

updated_list = [(a + elem, b + elem, c + elem) for idx, (a, b, c) in enumerate(lis)]



# Python – Multiply Adjacent elements

# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : (5, 35, 56, 80)
k=list((1, 5, 7, 8, 10))
lis=[]
for i in range(len(k)-1):
    lis.append(k[i]*k[i+1])





# ***************************************************************Advance Tuple Programs********************************************
#






# Python – Sort lists in tuple
# The original tuple is : ([7, 5, 4], [8, 2, 4], [0, 7, 5])
# The tuple after sorting lists : ([4, 5, 7], [2, 4, 8], [0, 5, 7])

test_tup=([7, 5, 4], [8, 2, 4], [0, 7, 5])

res = tuple((sorted(sub) for sub in test_tup))






# Python – Intersection in Tuple Records Data

# The original list 1 is : [('gfg', 1), ('is', 2), ('best', 3)]
# The original list 2 is : [('i', 3), ('love', 4), ('gfg', 1)]
# The Intersection of data records is : [('gfg', 1)]
test_list1=[('gfg', 1), ('is', 2), ('best', 3)]
test_list2=[('i', 3), ('love', 4), ('gfg', 1)]

res = [ele1 for ele1 in test_list1
       for ele2 in test_list2 if ele1 == ele2]



