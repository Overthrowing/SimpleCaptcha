# Simple_Captcha

## Usage
To generate a captcha use the generate_captcha function:

```
Captcha = generate_captcha(<Text>, <Custom Letter Map (Optional)>)
```

## Example

```
import random

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

text = random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet) + random.choice(Alphabet)

Captcha = generate_captcha(text)
print(Captcha)
input = input("\nEnter the phrase in the captcha: ")
if input.upper() == text:
    print("Login Successful")
else:
    print("Login Unsuccessful")
```
