# Higher-Order-Functions

List Comprehensions -- a concise syntax for specifying a new list in terms of a transformation of an old one. For exmaple:

    numbers = [1,2,3,4,5]
    odds = [n for n in numbers if n % 2 == 1] 
    squares = [n * n for n in numbers] 

That code assigns [1,3,5] to odds and [1,4,9,16,25] to squares. The first operation is sometimes called "filter" (because we are filtering out unwanted elements) and the second operation is sometimes called "map" (because we are mapping, or transforming, all of the elements in a list). 

Python also has functions behave similarly: 

    odds = filter(lambda n : n % 2 == 1, numbers) 
    squares = map(lambda n : n * n, numbers) 

The filter() and map() definitions for odds and squares produce the same results as the list comprehension approaches. In other words, we can define (or implement) list comprehensions in terms of map and filter. In this exercise we take that notion one step beyond, by making
specialized maps and filters. For example, suppose that we know that we will be filtering many lists down to only their odd elements. Then we might want something like this:

    filter_odds = filter_maker(lambda n : n % 2 == 1)
    odds = filter_odds(numbers) 

In this example, "filter_maker()" is a function that takes a function as an argument and returns a function as its result. We say that
filter_maker is a *higher order function*. Complete the code below with definitions for filter_maker() and map_maker(). Hint: You can use either "lambda" or nested Python function definitions. Both will work. The function you return from filter_maker(f) will have to reference f, so you'll want to think about nested environments.
