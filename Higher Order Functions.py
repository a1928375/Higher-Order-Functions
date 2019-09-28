# Solution 1: use lambda
def filter_maker(f):
    
	return lambda l: [elt for elt in l if f(elt)]

def map_maker(f):
    
	return lambda l: [f(elt) for elt in l]

# # Solution 2: define function
# def filter_maker(f):

# 	def your_filter(lst):

# 		return filter(f, lst)

# 	return your_filter

# def map_maker(f):

# 	def your_map(lst):

# 		return map(f, lst)

# 	return your_map


numbers = [1,2,3,4,5,6,7]

filter_odds = filter_maker(lambda n : n % 2 == 1)

print (filter_odds(numbers) == [1,3,5,7])
        
length_map = map_maker(len)

words = "Scholem Aleichem wrote Tevye the Milkman, which was adapted into the musical Fiddler on the Roof.".split()

print (length_map(words) == [7, 8, 5, 5, 3, 8, 5, 3, 7, 4, 3, 7, 7, 2, 3, 5])

string_reverse_map = map_maker(lambda str : str[::-1])

# str[::-1] is cute use of the Python string slicing notation that reverses str. A hidden gem in the homework!

print (string_reverse_map(words) == ['melohcS', 'mehcielA', 'etorw', 'eyveT', 'eht', ',namkliM', 'hcihw', 'saw', 'detpada', 'otni', 'eht', 'lacisum', 'relddiF', 'no', 'eht', '.fooR'])

square_map = map_maker(lambda n : n * n)

print ([n*n for n in numbers if n % 2 == 1] == square_map(filter_odds(numbers)))
