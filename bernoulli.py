# -*- coding: utf-8 -*-
"""
Summary:
    Intended for calculating partial sums of powers of natural numbers.
    Can also print n+1 Bernoulli numbers,
     do python math, cache crucial numbers.
    Warning: Not fitting for server. Has many vunerabilities.
    Can launch arbitrary code.

Help, usage:
    You can take advantage of command line interface
     to see some available commands.
    Use "python Bernoulli.py help" terminal command for that purpose.

    You can also enter interactive mode by launching Bernoulli.py
     without any parameters.

Caching:
    App saves calculated values that are most vital for calculations.
    These are generally needed to quickly construct
     a sequence of Bernoulli numbers.

    This optimization makes futher uses of bernoulli app faster.
    Overhead for reading/writing these numbers from/to cache file
    dependes on quantity stored numbers
    (it's ~0.5s for 3001 Bernoulli & 3001 generator numbers).
"""

# %% Definitions
from fractions import Fraction as fr
from pickle import loads, dumps
from sys import argv, exc_info, excepthook
from os import rename, remove
from re import compile
import sys
import atexit

sys.set_int_max_str_digits(1 << 30)

glob = globals()
public_functions = []
public_functions.append("exit  aka  quit")
help = help

CACHE_FNAME = "Bernoulli.pycache"
ACTIVE_CFNAME = "Active" + CACHE_FNAME
MAX_NO_NUMS_SAVED_TO_CACHE_FILE = 3_000

try:
    with open(CACHE_FNAME, "rb") as fi:
        # Pickle Errors not handled !
        bernoulli_nums, generator_nums = loads(fi.read())
except FileNotFoundError:
    bernoulli_nums = []
    generator_nums = []
bernoulli_nums_read_from_cache = len(bernoulli_nums)


def ensure_nth_bn(n):
    """
    Ensures that nth Bernoulli number is directly accessible in RAM.
    Concreatly in `bernoulli_nums` collection.

    This function u Akiyama–Tanigawa algorithm"""
    G = generator_nums
    B = bernoulli_nums
    while len(B) <= n:
        G.append(fr(1, len(B) + 1))
        for j in range(len(B), 0, -1):
            G[j - 1] = j * (G[j - 1] - G[j])
        B.append(G[0])


ensure = ensure_nth_bn


def nth_Bernoulli_num(n: int) -> int:
    """Returns `n`th Bernoulli number."""
    ensure_nth_bn(n)
    return bernoulli_nums[n]


def up_to_n_Bernoulli_num(n: int) -> list:
    """Returns list of all Bernoulli numbers up to `n`th term."""
    ensure_nth_bn(n)
    return bernoulli_nums[: n + 1]


def print_up_to_n_Bernoulli_num(n):
    """Prints list of all Bernoulli numbers up to `n`th term
    without creating new sequence inside Python kernel.
    It naturally has smaller overhead than printing
    result of `up_to_n_Bernoulli_num(n)` .
    """
    ensure_nth_bn(n)
    for k in range(0, n + 1):
        print(f"{k:7}: {bernoulli_nums[k]}")


print_up = print_up_to_n_Bernoulli_num
public_functions.append("print_up_to_n_Bernoulli_num  aka  print_up")


def fa_fact(n: int, fall_num: int):
    """Returns falling factorial,
    where `n` is base and `fall_num` is amount of decreasing factors,
    which make up falling factorial"""
    y = 1
    while fall_num > 0:
        y *= n
        n -= 1
        fall_num -= 1
    return y


def sum_of_pows(n: int, p: int) -> int:
    """
    Returns sum of `p` powers of all natural numbers from range [0,`n`].

    This function uses optimized Faulhaber's formula.
    """
    ensure_nth_bn(p)
    B = bernoulli_nums

    n_to_faP = n**p
    tri_nomial = fr(n_to_faP * n, p + 1) + fr(n_to_faP, 2)

    n_to_faP //= n
    n_sq = n * n
    # Optimization
    fact_k = 1
    fa_fact_p = 1
    fa_p = p  # p is not used anymore
    for k in range(2, p + 1):  # Can be well optimized
        fact_k *= k
        fa_fact_p *= fa_p
        fa_p -= 1
        if k & 1 == 0:  # to opt.
            tri_nomial += (
                fr(B[k], fact_k) * fa_fact_p * n_to_faP
            )  # Should this be made one fraction
            n_to_faP //= n_sq
    return tri_nomial


def explain_commands(*commands):
    """It explains commands from CLI."""
    if commands:
        for com in commands:
            help(glob[com])  # Will it print to stdout?
            print("\n")
    else:
        print(
            'Commands are wrappings around functions.'
            'They\'re implemented in "Bernoulli.py".\n'
            'Use "help choosen_command" to print the documentation'
            ' of the underlying function.\n'
            "Command line syntax must be preserved!\n"
            'Sample command: "python Bernoulli.py psum 100 1"\n'
        )
        print("List of available commands:")
        i = 1
        for sh, full in CLI_shorthands.items():
            print(f" {i}. {full}  aka  {sh}")
            i += 1


CLI = {
    "nth_Bernoulli_num": lambda *args: print(nth_Bernoulli_num(*args)),
    "up_to_n_Bernoulli_num": lambda *args: print_up_to_n_Bernoulli_num(*args),
    "sum_of_pows": lambda *args: print(sum_of_pows(*args)),
    "help": explain_commands,
}
CLI_shorthands = {
    "nth": "nth_Bernoulli_num",
    "up_to": "up_to_n_Bernoulli_num",
    "psum": "sum_of_pows",
    "h": "help",
}


def get_cli_func(func_name):
    """Gets CLI function by its name or name shorthand."""
    try:
        func_name = CLI_shorthands[func_name]
    except KeyError:
        pass

    return CLI[func_name]


for shorthand, full in CLI_shorthands.items():
    glob[shorthand] = glob[full]
    public_functions.append(f"{full}  aka  {shorthand}")


def cli_exec(toks):
    f = get_cli_func(toks[0])
    # Correct the type of numbers.
    for i in range(1, len(toks)):
        try:
            toks[i] = int(toks[i])
        except ValueError:
            pass
    # Run appropriate function.
    f(*toks[1:])


cmd_parser = compile(r"\b\w+\b").findall


def exec_command(cmd):
    """Function `exec_command` can be used to emulate command line mode.
    Usage: 'exec_command(your_command)'
    Eg. use: 'exec_command("nth_Bernoulli_num 8")'
    Ommit interpreter name & file name you're inside them!"""
    L = cmd_parser(cmd)
    cli_exec(L)
# From some reason I decided to define this alias here, not in alias dict.
# Don't touch. It works.
ec = exec_command
public_functions.append("exec_command aka ec")


# Exiting: cache saving
def save_key_nums():
    """
    Saves numbers that are most vital for calculations.
    These are generally numbers that are needed
     to quickly reconstruct sequence of Bernoulli numbers.
    This optimization makes futher calculations faster.
    Overhead for reading/writing these numbers from/to cache file
    hasn't been measured.
    """
    no_nums_to_save = min(len(bernoulli_nums), MAX_NO_NUMS_SAVED_TO_CACHE_FILE)
    if no_nums_to_save <= bernoulli_nums_read_from_cache:
        return
    print("Saving the key numbers to cache.")
    with open(ACTIVE_CFNAME, "wb") as fi:
        fi.write(
            dumps(
                (
                    bernoulli_nums[:no_nums_to_save],
                    generator_nums[:no_nums_to_save],
                )
            )
        )
    try:
        remove(CACHE_FNAME)
    except FileNotFoundError:
        pass
    rename(ACTIVE_CFNAME, CACHE_FNAME)
    print("Success. 2*%d numbers saved.\n" % no_nums_to_save)


save = save_key_nums
public_functions.append("save_key_nums  aka  save")


# %% Registering clean-up functions.
atexit.register(save_key_nums)


# %% Interaction with user.
if __name__ == "__main__":
    if len(argv) <= 1:
        print("Welcome to Bernoulli-Interactive!")
        print()
        from math import *

        print(
            "If you intended to use CLI mode,"
            " then you need to know hot to use OS terminal."
        )
        print(
            'CLI has help command, you can run'
            ' "python Bernoulli.py help" from terminal.'
        )
        print()
        print(
            "In this interactive mode you can use either"
            " Python3, Python3 math and Bernoulli.py functions."
        )
        print("Public Bernoulli.py functions:")

        for i, func_name in enumerate(public_functions, 1):
            print(f" {i}. {func_name}")
        print('Type: "help(function_name)" for help.')
        print()
        print(exec_command.__doc__)

        # Using interpreter
        while True:
            try:
                v = eval(input(">> "))
                if v is not None:
                    print(v)
            except (KeyboardInterrupt, EOFError, SystemExit):
                break
            except:
                excepthook(*exc_info())
    else:
        cli_exec(argv[1:])
