def ethiopian_multiplication(num1: int, num2: int) -> int:
    """
    Multiplies two positive integers using the Ethiopian Multiplication method.

    Ethiopian Multiplication, is an ancient method for multiplying two numbers
    using only doubling, halving, and addition.

    Algorithm Steps:
    ===============

    1. Write the two numbers to be multiplied at the top of two columns (A and B).
    2. In column A, repeatedly halve the number (integer division), discarding any remainder,
       until you reach 1.
    3. In column B, repeatedly double the number, keeping the same number of rows as in column A.
    4. Look at column A and identify the rows where the number in column A is odd.
    5. Sum the corresponding numbers in column B for the rows identified in step 4.
    6. The sum obtained in step 5 is the product of the original two numbers.

    
For example, Let's multiply 77 and 69 using Ethiopian Multiplication step-by-step:

Step 1: Set up two columns.

        Column A	Column B
        77	        69

Step 2: Halve Column A and Double Column B.

        Column A	Column B
        77	        69
        38	        138
        19	        276
        9	        552
        4	        1104
        2	        2208
        1	        4416

Step 3: Identify Odd Numbers in Column A and Select Corresponding Numbers in Column B.

        Column A	Column B	Keep/Discard
        77	        69	        Keep
        38	        138	        Discard
        19	        276	        Keep
        9	        552	        Keep
        4	        1104	    Discard
        2	        2208	    Discard
        1	        4416	    Keep

Step 4: Sum the Kept Numbers from Column B.

    The kept numbers from Column B are: 69, 276, 552, and 4416.

    Sum = 69 + 276 + 552 + 4416 = 5313

Therefore, 77 multiplied by 69 using Ethiopian Multiplication is 5313.


    The History of Ethiopian Multiplication:
    =======================================

    This method is ancient and has been used in various cultures. While often called
    "Ethiopian" or "Russian Peasant," similar methods were known and used in
    ancient Egypt. It's a testament to early arithmetic techniques that predate
    modern multiplication algorithms. The method relies on the binary representation
    of numbers and effectively decomposes one number into a sum of powers of two.


    Args:
        num1 (int): The first positive integer to be multiplied.
        num2 (int): The second positive integer to be multiplied.

    Returns:
        int: The product of num1 and num2 calculated using Ethiopian Multiplication.

    Raises:
        TypeError: if num1 or num2 is not an integer.
        ValueError: if num1 or num2 is not a positive integer.

    Author:
        Your Name: Daniel Gessese Amdework
        Your Email: dnlmdwrk@gmail.com

    Application Standard and Deployment Considerations:
    ==================================================

    - Input Validation: The function includes input validation to ensure that
      inputs are positive integers. This is important for robustness.
    - Readability: The code is written to be clear and follows the steps of the
      Ethiopian Multiplication algorithm closely, enhancing readability.
    - Testability:  The function can be easily tested with various inputs to ensure
      correctness. Unit tests should be implemented for robust application development.
    - Limited Scope: This function is specifically for demonstrating Ethiopian Multiplication
      and may not be the most efficient method for general-purpose multiplication,
      especially for very large numbers in production environments where optimized
      built-in multiplication operations are preferred.
    - Educational Use:  The primary application of this function is educational,
      to understand and demonstrate the Ethiopian Multiplication method.
    """

    if not isinstance(num1, int) or not isinstance(num2, int):
        raise TypeError("Both inputs must be integers.")
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Both inputs must be positive integers.")

    column_a = []
    column_b = []

    # Step 1 & 2: Set up columns and halve Column A, double Column B
    a = num1
    b = num2
    while a >= 1:
        column_a.append(a)
        column_b.append(b)
        a //= 2  # Integer division (halving)
        b *= 2   # Doubling

    # Step 3 & 4: Identify odd numbers in Column A and sum corresponding numbers in Column B
    product = 0
    for i in range(len(column_a)):
        if column_a[i] % 2 != 0:  # Check if number in Column A is odd
            product += column_b[i]

    return product