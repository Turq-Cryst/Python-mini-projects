import string


class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] = self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r') as file:
            return {line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    @staticmethod
    def has_sequential(password: str, window: int = 3):
        for i in range(len(password) - window + 1 ):
            chars = password[i: i + window]
            if chars[0] == chars[1] and chars[1] == chars[2]:
                return True
        return False


    def rate(self, password: str) -> dict[str, list[str]]:
        result: dict[str, list[str]|str] = dict()

        if self.is_common(password):
            result['missing'] = ['Password too common']
            result['rating'] = 'poor'
            return result

        score: int = 0
        missing: list[str] = ['uppercase', 'digit', 'symbol', 'length']

        if any(c.isupper() for c in password):
            score += 1
            missing.remove('uppercase')
        if any(c in string.digits for c in password):
            score += 1
            missing.remove('digit')
        if any(c in string.punctuation for c in password):
            score += 1
            missing.remove('symbol')
        if len(password) >= 10:
            score += 1
            missing.remove('length')

        if self.has_sequential(password):
            score -= 1
            missing.append('avoid repeating characters, e.g., "aaa", "111"')

        result['missing'] = missing

        if score == 4:
            result['rating'] = 'secure'
        elif score == 3:
            result['rating'] = 'good'
        elif score == 2:
            result['rating'] = 'moderate'
        else:
            result['rating'] = 'poor'
          
        return result
      

def main() -> None:
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        result = validator.rate(password)
        rating: str = result['rating']
        missing: list[str] = result['missing']

      
        if rating == 'secure':
            print('✅ Your password is secure! ')
        elif rating == 'good':
            print('✅ Your password is of good strength.')
            print(f'Try adding this to your password: {missing}')
        elif rating == 'moderate':
            print('⚠️ Your password is of medium strength.')
            print(f'Try adding these to your password: {missing}')
        else:
            print('⚠️ That password sucks!')
            print(f'Tips: {missing}')


if __name__ == '__main__':
    main()


