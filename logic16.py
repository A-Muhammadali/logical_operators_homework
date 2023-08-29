def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 10000<=a<=99999 or -99999<=a<=-10000
print(main(12345)) 