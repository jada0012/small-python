import random, string

def password(length):
    src = string.ascii_letters + string.digits + string.punctuation
    pwd = random.choice(string.ascii_uppercase)
    pwd += random.choice(string.ascii_lowercase)
    pwd += random.choice(string.digits)
    pwd += random.choice(string.punctuation)

    for i in range(length - 4):
        pwd += random.choice(src)
    pwdlst = list(pwd)
    random.SystemRandom().shuffle(pwdlst)
    password = ''.join(pwdlst)
    return password
len = input('how logn do you want the password to be')
print(password(int(len)))