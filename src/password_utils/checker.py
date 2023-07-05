import re


class PasswordStrengthChecker:
    """
    PasswordStrengthChecker is a class that provides functionality to check the strength of passwords based on configurable requirements.
    """

    min_length = 8
    requires_lowercase = True
    requires_uppercase = True
    requires_special_chars = False
    requires_digits = True

    def __init__(self):
        """
        Initializes a new instance of the PasswordStrengthChecker class.
        """
        pass

    @classmethod
    def configure_strength(cls, **kwargs):
        """
        Configures the strength requirements for password checking.

        Args:
            - **kwargs: Strength configuration parameters.
                - min_length (int): Minimum length requirement.
                - requires_lowercase (bool): Whether lowercase characters are required.
                - requires_uppercase (bool): Whether uppercase characters are required.
                - requires_special_chars (bool): Whether special characters are required.
                - requires_digits (bool): Whether digits are required.

        Raises:
            ValueError: If the configuration values are invalid.
        """
        if "min_length" in kwargs:
            min_length = kwargs["min_length"]
            if isinstance(min_length, int) and min_length > 0:
                cls.min_length = min_length
            else:
                raise ValueError("min_length must be a positive integer")

        for key in (
            "requires_lowercase",
            "requires_uppercase",
            "requires_special_chars",
            "requires_digits",
        ):
            if key in kwargs:
                value = kwargs[key]
                if isinstance(value, bool):
                    setattr(cls, key, value)
                else:
                    raise ValueError(f"{key} must be a boolean value")

    def is_password_secure(self, password):
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
            r'[!@#$%^&*(),.?":{}|<>]', password
        ):
            return False

        if self.requires_digits and not re.search(r"\d", password):
            return False

        return True


password = "Hellow2jwjb"
checker = PasswordStrengthChecker()
PasswordStrengthChecker.configure_strength(min_length=100, requires_special_chars=True)
# print(checker.is_password_secure(password))
