#!/usr/bin/python3.5 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# © 2016 Lev Maximov

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3].
# Исходный список должен остаться неизменным
def remove_adjacent(nums):
	# I don't understand why it's worked
	#return [*{*nums}]
	out=[]
	#print("input:"+str(nums))
	if(len(nums)>1):
		out=nums[:1]
		#print("output0:"+str(nums[:1]))
		#print("medres0:"+str(nums[1:]))
		for i in range(1,len(nums)):
			#print("medres :"+str(i)+" "+str(nums[i]))
			if nums[i]==nums[i-1]:
				#print("thrown:"+str(i)+" "+str(i-1)+" "+str(nums[i])+" "+str(nums[i-1]))
				continue
			else:
				out.append(nums[i])
				#print("output:"+str(nums[i]))
	else:
		out=nums
	return out


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(a, b):
	# +++your code here+++
	if(len(a)==0):
		return b
	if(len(b)==0):
		return a
	else:
		if a[0]<b[0]:
			return [a[0],*linear_merge(a[1:],b)]
		else:
			return [b[0],*linear_merge(a,b[1:])]

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
	print('remove_adjacent')
	test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
	test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
	test(remove_adjacent([2, 3, 2, 3, 2]), [2, 3, 2, 3, 2])
	test(remove_adjacent([]), [])

	print()
	print('linear_merge')
	test(linear_merge([], []), [])
	test(linear_merge([3], []), [3])
	test(linear_merge([], [5]), [5])
	test(linear_merge([7], [2]), [2, 7])
	test(linear_merge([1, 5], [2]), [1, 2, 5])
	test(linear_merge([2, 3, 10], [5, 7]), [2, 3, 5, 7, 10])
	test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
			 ['aa', 'bb', 'cc', 'xx', 'zz'])
	test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
			 ['aa', 'bb', 'cc', 'xx', 'zz'])
	test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
			 ['aa', 'aa', 'aa', 'bb', 'bb'])



if __name__ == '__main__':
	main()
