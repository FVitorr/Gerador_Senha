import random
import string

len_ = 16
chars = string.ascii_letters + string.digits + 'çÇ5@#!%¨&*()_-+/^~´][}{'

rnd = random.SystemRandom()


print(''.join(rnd.choice(chars) for i in range(len_)))