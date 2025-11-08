## What is the Luhn Algorithm?

The **Luhn Algorithm**, also known as the "modulus 10" algorithm, is a simple checksum formula used to validate various identification numbers, including:

- Credit card numbers
- IMEI numbers
- National provider identifier numbers
- Canadian Social Insurance Numbers

Created by IBM researcher Hans Peter Luhn in 1954, this algorithm is widely used for error-checking in various applications to detect simple errors in typing or transmission of credit card numbers.

## How it Works

The Luhn Algorithm follows these steps:

1. **Reverse the number**: Start from the rightmost digit
2. **Separate digits**: Split into odd and even positioned digits (from right to left)
3. **Process odd positions**: Sum all digits in odd positions (1st, 3rd, 5th, etc.)
4. **Process even positions**: 
   - Double each digit in even positions (2nd, 4th, 6th, etc.)
   - If the result is ≥ 10, add the digits together (e.g., 16 → 1+6 = 7)
   - Sum all processed even position digits
5. **Final check**: Add both sums together
6. **Validation**: If the total is divisible by 10, the number is valid


## Example

**Input**: `4111-1111-4555-1141`

**Step-by-step process**:
1. Remove formatting: `4111111145551141`
2. Reverse: `1411555411111114`
3. Odd positions (1st, 3rd, 5th...): `1, 1, 5, 5, 1, 1, 1, 1` → Sum = 16
4. Even positions (2nd, 4th, 6th...): `4, 1, 5, 4, 1, 1, 1, 4`
   - Double: `8, 2, 10, 8, 2, 2, 2, 8`
   - Adjust (10 → 1+0): `8, 2, 1, 8, 2, 2, 2, 8` → Sum = 33
5. Total: 16 + 33 = 49
6. 49 % 10 ≠ 0 → **INVALID**

## Test Cases

You can test with these sample card numbers:

**Valid Cards**:
- `4532015112830366` (Visa)
- `5555555555554444` (MasterCard)
- `4111111111111111` (Test Visa)

**Invalid Cards**:
- `4111111111111112` (Modified test card)
- `1234567890123456` (Random number)
