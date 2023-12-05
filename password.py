import hashlib

def hasher_mot_de_passe(mot_de_passe):
    sha256 = hashlib.sha256()
    mot_de_passe_bytes = mot_de_passe.encode('utf-8')
    sha256.update(mot_de_passe_bytes)
    mot_de_passe_hache = sha256.hexdigest()
    return mot_de_passe_hache

def password():
    while True:
        user_password = input('Enter a password: ')
        password_length = len(user_password)
        has_capital = False
        has_lower = False
        has_digit = False
        has_special = False
        
        for char in user_password:
            if char.isupper():
                has_capital = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if not char.isalnum():
                has_special = True

        if password_length < 8:
            print('Your password does not contain enough characters.')
        elif not has_capital:
            print('Make sure your password has at least one capital letter.')
        elif not has_lower:
            print('Make sure your password has at least one lowercase letter.')
        elif not has_digit:
            print('Make sure your password has at least one digit.')
        elif not has_special:
            print('Make sure your password has at least one special character.')
        else:
            # Hacher le mot de passe
            mot_de_passe_hache = hasher_mot_de_passe(user_password)
            
            print('Password hashed (SHA-256):', mot_de_passe_hache)
            print('Password set successfully!')
            break

# Appeler la fonction password
password()