from django.utils.crypto import get_random_string


def key_generator():
    """
    Generate Django secret key.
    """
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    res = get_random_string(50, chars)
    print(res)


if __name__ == '__main__':
    key_generator()
