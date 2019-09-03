 s1 = {1,2,4,5,6,6,2,3,7}
print s1

s1.add(8)
print s1

_list = [9,10]
s1.update(_list)
print s1

s1.remove(5) #if try to remove - it will cause a key erroe
print s1
# s1 = set(1,2,3,4,5,6)
# print s1

s1.discard(6)
print s1,"\n"

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}

s4 = s1.intersection(s2) #find intersection values
print s4,"intersection"

s4 = s1.intersection(s2,s3) #find intersection values
print s4,"intersection"


s4 = s1.difference(s2) # find difference
print s4,"difference"


s4 = s1.symmetric_difference(s2)
print s4,"symmetric_difference"

l1 = [1,2,3,1,2,3]
l2 = set(l1)
l2 = list(l2)
print l2,"convert to a list and back. remove non unique values"

#==========================================
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

if 'Corey' in developers:
    print('Found!')