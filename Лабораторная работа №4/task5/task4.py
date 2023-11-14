from random import sample
symbols = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz0123456789'
def get_random_password(n=8) -> str:
    return ''.join(sample(symbols, 8))



print(get_random_password())
