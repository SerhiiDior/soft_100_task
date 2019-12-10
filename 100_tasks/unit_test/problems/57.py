def valid_email(*args):
    email=str(*args)
    email= email.split('@')
    return email[0]

