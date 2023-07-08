import re
import random
import string


class PasswordUtil:
    """
    PasswordUtil is a class that provides functionality to
    - Configure password strength requirements
    - Generate secure password
    - Check the strength of passwords

    """

    def __init__(self):
        """
        Initializes a new instance of the Password class.
        - min_length = 8
        - max_length = 64
        - requires_lowercase = True
        - requires_uppercase = True
        - requires_digits = True
        - requires_special_chars = True
        """
        self.min_length = 8
        self.max_length = 64
        self.requires_lowercase = True
        self.requires_uppercase = True
        self.requires_digits = True
        self.requires_special_chars = True

    def configure_strength(self, **kwargs):
        """
        Configures the strength requirements for password checking.

        Args:
            - **kwargs: Strength configuration parameters.
                - min_length (int): Minimum length requirement.
                - max_length (int): Maximum length requirement.
                - requires_lowercase (bool): Whether lowercase characters are required.
                - requires_uppercase (bool): Whether uppercase characters are required.
                - requires_special_chars (bool): Whether special characters are required.
                - requires_digits (bool): Whether digits are required.

        Raises:
            ValueError: If the configuration values are invalid.
        """
        if "min_length" in kwargs:
            min_length = kwargs["min_length"]
            if isinstance(min_length, int) and min_length > 8:
                self.min_length = min_length
            else:
                raise ValueError("min_length can not be lesser than 8")

        if "max_length" in kwargs:
            max_length = kwargs["max_length"]
            if isinstance(max_length, int) and max_length >= self.min_length:
                self.max_length = max_length
            else:
                raise ValueError("max_length can not be lesser than min_length")

        for key in (
            "requires_lowercase",
            "requires_uppercase",
            "requires_special_chars",
            "requires_digits",
        ):
            if key in kwargs:
                value = kwargs[key]
                if isinstance(value, bool):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} must be a boolean value")

    def is_secure(self, password):
        """
        Checks if the given password meets the configured strength requirements.

        Args:
            password (str): The password to be checked.

        Returns:
            bool: True if the password is secure, False otherwise.
        """
        if len(password) < self.min_length:
            return False

        if self.requires_lowercase and not re.search(r"[a-z]", password):
            return False

        if self.requires_uppercase and not re.search(r"[A-Z]", password):
            return False

        if self.requires_special_chars and not re.search(
            "[" + string.punctuation + "]", password
        ):
            return False

        if self.requires_digits and not re.search(r"\d", password):
            return False

        return True

    def generate_password(self, **kwargs) -> str:
        """Generates a secure password based on specified requirements.

        Args:
        **kwargs: Additional keyword arguments to customize password generation.
            - requires_lowercase (bool): Whether the password requires lowercase letters.
            - requires_uppercase (bool): Whether the password requires uppercase letters.
            - requires_special_chars (bool): Whether the password requires special characters.
            - requires_digits (bool): Whether the password requires digits.
            - min_length (int, optional): Minimum length of the password (default: self.min_length).
            - max_length (int, optional): Maximum length of the password (default: self.max_length).

        Returns:
            str: A randomly generated secure password.

        Raises:
            ValueError: If any argument has an invalid value.
                - requires_lowercase, requires_uppercase, requires_special_chars, requires_digits
                must be boolean values.
                - min_length must be an integer greater than or equal to 8.
                - max_length must be an integer greater than or equal to min_length.
        """
        for key in (
            "requires_lowercase",
            "requires_uppercase",
            "requires_special_chars",
            "requires_digits",
        ):
            if key in kwargs:
                value = kwargs[key]
                if isinstance(value, bool):
                    pass
                else:
                    raise ValueError(f"{key} must be a boolean value")

        if "min_length" in kwargs:
            min_length = kwargs["min_length"]
            if isinstance(min_length, int) and min_length > 8:
                pass
            else:
                raise ValueError("min_length can not be lesser than 8")

        if "max_length" in kwargs:
            max_length = kwargs["max_length"]
            if isinstance(max_length, int) and max_length >= min_length:
                pass
            else:
                raise ValueError("max_length can not be lesser than min_length")

        min_length = kwargs.get("min_length", self.min_length)
        max_length = kwargs.get("max_length", self.max_length)
        requires_lowercase = kwargs.get("requires_lowercase", self.requires_lowercase)
        requires_uppercase = kwargs.get("requires_uppercase", self.requires_uppercase)
        requires_special_chars = kwargs.get(
            "requires_special_chars", self.requires_special_chars
        )
        requires_digits = kwargs.get("requires_digits", self.requires_digits)

        password_length = random.randint(min_length, max_length)
        password = ""

        if requires_lowercase:
            password += random.choice(string.ascii_lowercase)
        if requires_uppercase:
            password += random.choice(string.ascii_uppercase)
        if requires_digits:
            password += random.choice(string.digits)
        if requires_special_chars:
            password += random.choice(string.punctuation)

        charset = string.ascii_letters + string.digits + string.punctuation

        remaining_length = password_length - len(password)
        password += "".join(random.choices(charset, k=remaining_length))

        password_list = list(password)
        random.shuffle(password_list)
        password = "".join(password_list)

        return password
