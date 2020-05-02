from enggames_site import bcrypt


def hashpassword(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')