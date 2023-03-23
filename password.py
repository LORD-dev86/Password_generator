import sys
import string
import random

if __name__ == '__main__':
        length = int(sys.argv[1])
        count = int(sys.argv[2])

        alfabet = string.ascii_letters + '0123456789' + '%*()?@#$~'

        password: str = ''
        for i in range(count):
            for j in range(length):
                password += alfabet[random.randrange(len(alfabet))]
            print(password)
            password = ''