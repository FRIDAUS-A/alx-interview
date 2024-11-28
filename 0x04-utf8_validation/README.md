UTF-8 Validation - Tasks

Task Description
In this task, you are required to implement a method that determines whether a given data set represents a valid UTF-8 encoding.

Prototype
The method prototype is as follows:

python

def validUTF8(data)
Return Value
The method should return True if the provided data is a valid UTF-8 encoding, and False otherwise.

Constraints
In UTF-8 encoding, a character can be represented by 1 to 4 bytes.
The input data set can contain multiple characters.
The data set will be represented by a list of integers, where each integer represents 1 byte of data. Therefore, you only need to consider the 8 least significant bits of each integer.
Example
Here's an example demonstrating the usage of the validUTF8 method:

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
Repository Information
GitHub Repository: alx-interview
Directory: 0x04-utf8_validation
File: 0-validate_utf8.py

License
This project is licensed under the MIT License - see the LICENSE file for details.
