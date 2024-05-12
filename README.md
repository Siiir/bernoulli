# Bernoulli
![Bernoulli using bernoulli.py](Bernoulli_using_bernoulli.png)

This Python package offers robust tools for calculating partial sums of powers of natural numbers and managing Bernoulli numbers with optimized caching techniques. Ideal for mathematicians, researchers, and software developers interested in number theory or computational mathematics. 

## Features 🌟
- **Compute LARGE Partial Sums:** Utilize Faulhaber's formula to compute sums of powers of **very long** natural numbers.
- **Bernoulli Numbers Generation:** Efficiently generate Bernoulli numbers using the Akiyama–Tanigawa algorithm.
- **Caching System:** Persistent caching of computations to enhance performance of successive operations.
- **Command Line Interface:** Versatile CLI support for **interactive** and **script-based** usage.
- **Library for your app:** You can `import bernoulli` to make it a part of your app. 

## Getting Started 🚀
To get started with `bernoulli`.
1. Clone the repository.
```bash
git clone https://github.com/Siiir/bernoulli
```
2. Go to the repo folder.
```bash
cd bernoulli
```
3. Run the following command in your terminal:
```bash
python bernoulli.py help
```

## Examples
Here are some quick examples to show you the power of the Bernoulli package.

### Calculating the nth Bernoulli Number
This command prints the 6th Bernoulli number.
```bash
python bernoulli.py nth 6
```
**Or**, in interactive mode type `nth(6)`.

### Printing Bernoulli Numbers up to `k`
Lists the first 11 Bernoulli numbers (0 to 10).
```bash
python bernoulli.py up_to 10
```
**Or**, in interactive mode type `up_to(10)`.

### Sum of Powerful Powers
* Calculates the sum of the the first (1 vigintillion + ...) of positive natural numbers, **each taken to the power** of `k`=1873.
```bash
python bernoulli.py psum 1509096632309561804061385286158050392946131124427766465467743034  1873
```  
* **Or**, in interactive mode type
```python
psum(1509096632309561804061385286158050392946131124427766465467743034, 1873)
```  
* I have choosen a **"small"** `n` for the purpose of readability. You can try increasing the first argument quite freely. Whereas increasing the `k` will have a noticable computional cost.

### Complex equations using Python3's `math` functions and builtins
#### Interactive mode only.
```python
sin(psum(20, 3) - psum(10, 3)) + 2**6
```

## Documentation 📚
### [Online documentation](https://siiir.github.io/bernoulli/)
### Interactive documentation
Detailed documentation is available within the module. Use the help command for more information on specific functions:
```bash
python bernoulli.py help nth_Bernoulli_num
```
**Or**, in interactive mode type
```python
help(nth_Bernoulli_num)
```
You can even **use short aliases**.
```python
help(nth)
```

# Thinking in *big terms*
* As of time of writing the **most optimized is the _interactive mode_** as it doesn't need to perform the startup (big cache deserialization) between calls to different app commands. It also supports session-local, in-RAM caching.  
* Currently caching is set to 3000 \[u\], but only 2000\*u+2 numbers are saved on GitHub. This means that performing operations like `nth k` or `psum n k` with  
  1. `k` ≤ 2000 from GitHub clone should be almost const time.
  2. `k` ≤ 3000 will trigger full caching increasing the app startup time and enhancing large `k` computations.
  3. `k` > 3000 will trigger only in-RAM caching enhancing computations during one interactive session..

## Contributing
Interested in contributing? We're always looking for help to improve documentation, fix issues, or make optimizations.

## License
Distributed under the Apache License. See `LICENSE` for more information.

## Author
Bernoulli was created by Tomasz Nehring, a creative mathematician and software engineer.

---

⚠️ **Note:** Not suitable for server use. Has many vulnerabilities. Can launch arbitrary code.
