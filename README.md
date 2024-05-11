# Bernoulli
This Python package offers robust tools for calculating partial sums of powers of natural numbers and managing Bernoulli numbers with optimized caching techniques. Ideal for mathematicians, researchers, and software developers interested in number theory or computational mathematics. 

## Features 🌟
- **Compute Partial Sums:** Utilize Faulhaber's formula to compute sums of powers of natural numbers.
- **Bernoulli Numbers Generation:** Efficiently generate Bernoulli numbers using the Akiyama–Tanigawa algorithm.
- **Caching System:** Persistent caching of computations to enhance performance of successive operations.
- **Command Line Interface:** Versatile CLI support for interactive and script-based usage.

## Getting Started 🚀
To get started with `bernoulli`.
1. Clone the repository
```bash
git clone https://github.com/Siiir/bernoulli
```
2. Run the following command in your terminal:
```bash
python bernoulli.py help
```

## Examples
Here are some quick examples to show you the power of the Bernoulli package:

### Calculating the nth Bernoulli Number
This command prints the 5th Bernoulli number.
```bash
python bernoulli.py nth 5
```
**Or** in interactive mode type `nth(5)`.

### Printing Bernoulli Numbers up to n
Lists the first 11 Bernoulli numbers (0 to 10).
```bash
python bernoulli.py up_to 10
```
**Or** in interactive mode type `up_to(10)`.

### Sum of Powerful Powers
Calculates the sum of the the first 1 milion positive natural numbers each taken to the power of 1800.
```bash
python bernoulli.py psum 1_000_000 1800
```
**Or** in interactive mode type `psum(10, 3)`.
### Complex equations using Python3's `math` functions and builtins
#### Interactive mode only.
sin(psum(20, 3) - psum(10, 3)) + 2**6

## Documentation 📚
### [Online documentation](https://siiir.github.io/bernoulli/)
### Interactive documentation
Detailed documentation is available within the module. Use the help command for more information on specific functions:
```bash
python bernoulli.py help nth_Bernoulli_num
```
**Or** in interactive mode type
```python
help(nth_Bernoulli_num)
```
You can even **use short aliases**.
```python
help(nth)
```

## Contributing
Interested in contributing? We're always looking for help to improve documentation, fix issues, or make optimizations. Please read `CONTRIBUTING.md` for more information on how you can contribute to the Bernoulli project.

## License
Distributed under the Apache License. See `LICENSE` for more information.

## Author
Bernoulli was created by Tomasz Nehring, a passionate mathematician and software engineer dedicated to building high-quality, open-source mathematical tools.

---

⚠️ **Note:** Not suitable for server use. Has many vunerabilities. Can launch arbitrary code.
