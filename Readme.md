# Overview

`password_lib` is a Python package for strong password checking. It validates password strength based on length, lowercase/uppercase characters, special characters, and digits. Enhance your application's security with ease.

## Requirements

- python 3.8 or higher

## Installation

```sh
py -m pip install password_lib
```

## Usage

```py
from password_utils.checker import PasswordStrengthChecker

PasswordStrengthChecker.configure_strength(min_length=10, requires_special_chars=True)
checker = PasswordStrengthChecker()

if checker.is_password_secure(password):
    print("Password is strong!")
else:
    print("Password is not strong!")
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Links

https://github.com/ardf/password_utils
