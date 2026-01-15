# Method to filter even numbers from a list
def filter_even_numbers(numbers):
    """
    Filter and return only even numbers from a list.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Example:
        >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return [num for num in numbers if num % 2 == 0]

# Method with for loop to filter even numbers
def filter_even_numbers_loop(numbers):
    """
    Filter and return only the even numbers from a given list.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list.
    
    Example:
        >>> filter_even_numbers_loop([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Mehod with lambda to filter even numbers
def filter_even_numbers_lambda(numbers):
    """
    Filter even numbers from a list using a lambda function.

    Args:
        numbers (list): A list of integers to filter.

    Returns:
        list: A new list containing only the even numbers from the input list.

    Example:
        >>> filter_even_numbers_lambda([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return list(filter(lambda num: num % 2 == 0, numbers))

# Method using recursion to filter even numbers
def filter_even_numbers_recursive(numbers):
    """
    Filter and return only the even numbers from a list using recursion.
    
    Args:
        numbers (list): A list of integers to filter.
    
    Returns:
        list: A new list containing only the even numbers from the input list,
              in the same order they appeared in the original list.
    
    Examples:
        >>> filter_even_numbers_recursive([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
        
        >>> filter_even_numbers_recursive([1, 3, 5])
        []
        
        >>> filter_even_numbers_recursive([])
        []
    """
    if not numbers:
        return []
    head, *tail = numbers
    if head % 2 == 0:
        return [head] + filter_even_numbers_recursive(tail)
    else:
        return filter_even_numbers_recursive(tail)