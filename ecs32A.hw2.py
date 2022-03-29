def dot_product(lst1, lst2):
    """Modify the code so it calculates the
    sum of products of each element in lst1 and lst2
    Assume lst1 and lst2 have the same length

    Example:
    >>> dot_product([1, 2], [0, 1])
    2

    # Explanation: lst1[0]*lst2[0] + lst1[1]*lst2[1]
    # = 1*0 + 2*1 = 2
    >>> dot_product([1, 2, -1], [1, 1, 1])
    2
    # Explanation: lst1[0]*lst2[0] + lst1[1]*lst2[1] + lst1[2]*lst2[2]
    # = 1*1 + 2*1 + -1*1 = 2
    """
    ### MODIFY THE CODE HERE ###
    ans = 0
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    elif len(lst1) == 0 or len(lst2) == 0:
        return None
    else:
            ans = lst1[i] * lst2[i] + ans
        return ans

def sum_of_fibonacci(n):
    """Calculate the sum of fibonacci sequence,
    in which the largest value is less than or equal to n
    
    In a fibonnaci sequence, every number starting from the
    third value is the sum of the previous two numbers
    and the initial values are 0 and 1.
    fib(0) = 0
    fib(1) = 1
    fib(2) = 0 + 1 = 1
    fib(3) = 1 + 1 = 2
    >>> sum_of_fibonacci(1)
    2
    
    # Explanation: 0 + 1 + 1 = 2
    >>> sum_of_fibonnaci(8)
    20
    # Explanation: 0 + 1 + 1 + 2 + 3 + 5 + 8 = 20
    """
    ### MODIFY THE CODE HERE ###
    #recursion
    fib1= 0
    fib2= 1
    fib3= 0
    ans = 0
    if n<=0:
        return 0
    elif n>=2:
        while fib2<=n:
            ans= fib2+ ans
            fib3= fib1
            fib1= fib2
            fib2= fib3 + fib2
        return ans
    else:
        return 0

    ### MODIFY THE CODE HERE ###


def page_of_book(page, book):
    """Modify the code so it returns
    True if the page is in the book.
    Note: each book is a list.
    >>> page_of_book('hello', ['hello', 'world'])
    True
    >>> page_of_book(0, [1, 3, 5])
    False
    >>> page_of_book(1.5, ['hello', 1.5, 0])
    True
    """
    ### MODIFY THE CODE HERE ###
    if page in book:
        return True
    else:
        return False
    ### MODIFY THE CODE HERE ###


def square_root(n):
    """Calculate the square root of n, rounded to the
    nearest 2 decimal places if necessary.  If square root
    is an integer, return its float form

    >>> square_root(25)
    5.0
    >>> square_root(1)
    1.0
    >>> square_root(2)
    1.41
    """
    ### MODIFY THE CODE HERE ###
    n= int(n)
    ans= n**(1/2)
    ans= float(ans)
    ans= round (ans,2)
    return ans
    ### MODIFY THE CODE HERE ###

def insecticide(room):
    """Modify the code so it kills all insects in the room.
    Note: only the string 'insect' should be regarded as an insect.
    >>> insecticide(['sofa', 'insect', 'bed', 'chair', 'insect'])
    ['sofa', 'bed', 'chair']
    """
    ### MODIFY THE CODE HERE ###
    n= room.count('insect')
    x=0
    while x<n:
        room.remove('insect')
        x+=1
    return room
    ### MODIFY THE CODE HERE ###

def rev_string(string):
    """
    Modify the code so it returns an string reversed
    >>> rev_string('hello')
    'olleh'
    """
    ### MODIFY THE CODE HERE ###
    string= string[len(string)::-1]
    return string
    ### MODIFY THE CODE HERE ###

def rev_integer(integer):
    """
    Modify the code so it returns an integer reversed
    >>> rev_integer(123)
    321
    """
    ### MODIFY THE CODE HERE ###
    integer = str(integer)
    integer = integer[len(integer)::-1]
    integer = int(integer)
    return integer
    ### MODIFY THE CODE HERE ###

def power_of_five(number):
    """Modify the code so it returns 
    True on any positive integer which is a power of 5
    False Otherwise
    >>> power_of_five(25)
    True
    >>> power_of_five(1)
    True
    >>> power_of_five(10):
    False
    """
    ### MODIFY THE CODE HERE ###
    if number <= 0:
        return False
    elif number/5== number//5:
        for i in range(0, number+1):
            if number/5==1:
                return True
            else:
                return False
    ### MODIFY THE CODE HERE ###

def palindrome_integer(number):
    """Modify the code so it returns
    True when the number is palindrome
    Return False if number is not an integer
    >>> palindrome_integer(12321)
    True
    >>> palindrome_integer(1232)
    False
    >>> palindrome_integer(1.1)
    False
    """
    ### MODIFY THE CODE HERE ###
    if number!= int(number):
        return False
    number= str(number)
    number2= str(number)
    number2= number[len(number2)::-1]
    if number== number2:
        return True
    else:
        return False
    ### MODIFY THE CODE HERE ###



def find_prime(n):
    """Modify the code so it prints 
    all primes less than or equal to n.
    >>> find_prime(10)
    2
    3
    5
    7
    """
    ### MODIFY THE CODE HERE ###
    if n==1:
        return None

    print(2)
    for i in range(2, n + 1):
        for a in range(2, i):
            if i%a == 0:
                break
            elif a == i-1:
                print(i)
    ### MODIFY THE CODE HERE ###