#!/usr/bin/env python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# © 2016 Lev Maximov

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
	# +++your code here+++
	s=0;
	for i in words:
		if len(i)>=2:
			if i[0]==i[-1]:
				s+=1;
	return s;

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
	# +++your code here+++
	witx=[];
	witoutx=[];
	for i in words:
		if i[0]=='x':
			witx.append(i);
		else:
			witoutx.append(i);
	#witx.sort();
	#witoutx.sort();
	return	sorted(witx)+sorted(witoutx);

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
# PS исходный список должен остаться неизменным (аналогично тому, как делает sorted)
def sort_last(tuples):
	# +++your code here+++
	return sorted(tuples,key=lambda s:s[-1]);

# D. stable_sort_last
# Отсортируйте их так, чтобы при совпадающем последнем элементе
# сортировка проводилась по предидущим
def stable_sort_last(tuples):
    # +++your code here+++
	return sorted(tuples,key=lambda s:s[-1::-1]);

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))))

# Calls the above functions with interesting inputs.
def main():
    print('match_ends')
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    test(match_ends(['абв', 'арра', 'ок', '']), 1)
    test(match_ends(['中文', '中文中', '中文中文', '中']), 1)

    print()
    print('front_x')
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
             ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
             ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
             ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

             
    print()
    print('sort_last')
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
             [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
             [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2,)]),
             [(2,), (1, 3), (3, 4, 5), (1, 7)])

    print()
    test(stable_sort_last([(4, 1), (1, 2), (2, 1), (3, 1)]),
             [(2, 1),(3, 1), (4, 1), (1, 2)])
    test(stable_sort_last([(3, 1), (1, 2), (2, 1)]),
             [(2, 1),(3, 1), (1, 2)])
	

if __name__ == '__main__':
    main()
