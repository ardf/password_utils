# Overview

`password-lib` is a Python library for generating secure passwords, configuring strength requirements, and checking password strength. With customizable length and requirements, it enhances application security. Use password-lib to easily generate strong passwords and ensure password security.

## Requirements

- python 3.9 or higher

## Installation

```sh
py -m pip install password-lib
```

## Usage

```sh
> from password_lib.utils import PasswordUtil

> # Create an instance of the PasswordUtil class
> password_util = PasswordUtil()

> # Configure the password strength requirements
> password_util.configure_strength(min_length=10)
> password = password_util.generate_password()
> is_secure = password_util.is_secure(password)
> password
0GpDjb@4M.RZRQY_HHCq7CzJI
> is_secure
True

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
