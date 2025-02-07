# Ethiopian Arithmetic Library 

### (`ethiomultlib`)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/ethiopian-arithmetic-lib.svg)](https://badge.fury.io/py/ethiopian-arithmetic-lib)

**A Python library providing an implementation of the ancient Ethiopian Multiplication algorithm.**

This library offers a function, `ethiopian_multiplication`, to perform multiplication of two positive integers using the elegant and historically significant Ethiopian Multiplication method. This technique relies solely on doubling, halving (integer division), and addition. The method involves halving the first number and doubling the second number in parallel columns. Rows where the first number is odd contribute the corresponding second number to the final sum. This sum represents the product. It's a fascinating demonstration of binary arithmetic principles in a pre-modern algorithmic form, offering a unique perspective on arithmetic operations.

## Installation

```bash
pip install ethiomultlib
```

## Usage

```bash
import ethiomultlib

# Use the function from the library
result = ethiomultlib.ethiopian_multiplication(45, 12)
print(f"Result of Ethiopian Multiplication: {result}") # Output: 540
```

## Ethiopian Multiplication Explained

The method involves halving the first number and doubling the second number in parallel columns. Rows where the first number is odd contribute the corresponding second number to the final sum. This sum represents the product. It's a fascinating demonstration of binary arithmetic principles in a pre-modern algorithmic form.

## Author
Daniel Gessese Amdework, Software Engineer, Data Scientist, and ML/DL Enthusiast. ([LinkedIn](https://linkedin.com/in/daniel-gessese-3b744543))

## License

This library is released under the MIT License. See the LICENSE file for details.

### Giving Credit where Credit is due

If you use `ethiomultlib` in your research, projects, or publications, we appreciate it if you would cite it. This helps give recognition to the work, and it also helps other users discover this library.

You can use the following formats to give credit. Simply copy and paste the format that is most appropriate for your needs:

**Option 1: Simple Attribution (for general use, project READMEs, websites, etc.)**