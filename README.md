# mround
Rounding functions compatible with Python 2 and 3.

The mround package provides the following functions:

* round_half_up: Round a number to nearest with ties going away from zero (Python 2 built-in round behavior).
* round_half_even: Round a number to nearest with ties going to nearest even (Python 3 built-in round behavior).
* round_down: round a number towards zero
* round_up: round a number away from zero

## Installation

### From Source Code

Clone or download the source code, generate wheel file, and install the wheel file using pip.

```bash
python setup.py bdist_wheel
cd dist
python -m pip install --no-index --find-links=. mround
```

## Usage

```python
from mround import round_down, round_up, round_half_up, round_half_even

round_half_up(3.5) # returns 4.0
round_half_up(4.5) # returns 5.0
round_half_up(4.55, 1) # returns 4.6

round_half_even(3.5) # returns 4.0
round_half_even(4.5) # returns 4.0
round_half_even(4550, -2) # returns 4600.0

round_down(3.9) # returns 3.0
round_up(3.1) # returns 4.0
```

## Running the tests

```python
python -m unittest tests.test_mround.MroundTestCase
```

## License
[MIT](https://choosealicense.com/licenses/mit/)