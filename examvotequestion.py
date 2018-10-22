class Poll: 
    #My solution for Poll/tally differs a little bit from the intended solution but I think it is still correct. 
    #Rather than storing objects in Poll.s, I store dictionaries (one unique dictionary for each object). 
    #In each dictionary, the key is the choice name and the value is a pair with the name of the Poll as the first element
    #and the number of times this given Poll has voted for the given choice as the second element. 
    #Since each dictionary corresponds to a unique object and contains the name of that object, my solution can access the information needed
    #from each distinct class, just like the intended solution. 
    s = []
    def __init__(self, n): 
        self.name = n
        self.votes = {}
        #Add dictionary to Poll.s (the program processes each update/query using a list of dictionaries rather than a list of objects)
        Poll.s.append(self.votes)
    def vote(self, choice): 
        #modify self.votes[choice], the first element in the pair will always be the name of the object
        #if the choice has not been seen in the dictionary before the second value would be one since it's the first vote (first condition)
        #if the choice has been seen before, access the current number of times it has been seen and increment it by 1 (second condition)
        self.votes[choice] = (self.name, 1 if not choice in self.votes else self.votes[choice][1]+1)
        
def tally(c): 
    '''
    Tally all votes for a choice c as a list of (poll name, vote count) pairs. 
    >>> a, b, c = Poll('A'), Poll('B'), Poll('C')
    >>> c.vote('dog')
    >>> a.vote('dog')
    >>> a.vote('cat')
    >>> b.vote('cat')cd Des
    >>> a.vote('dog')
    >>> tally('dog')
    [('A', 2), ('C', 1)]
    >>> tally('cat')
    [('A', 1), ('B', 1)]
    '''
    #list comprehension, loop through list of dictionaries, if a dictionary contains the given choice, return the corresponding pair (object name, frequency)
    return [dic[c] for dic in Poll.s if dic.get(c, 0) != 0]

def main(): 
    # Run the tests given in the exam, (the same doctests are also typed up if you want to run it in terminal). 
    a, b, c = Poll('A'), Poll('B'), Poll('C')
    c.vote('dog')
    a.vote('dog')
    a.vote('cat')
    b.vote('cat')
    a.vote('dog')
    print(tally('dog'))
    print(tally('cat'))
main()
