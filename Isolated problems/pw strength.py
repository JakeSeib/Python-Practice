# password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one
# digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII
# latin letters or digits

import string

def checkio(data: str) -> bool:

    pw_check = len(data)>=10 and any(x in data for x in string.ascii_lowercase) and any(x in data for x in string.ascii_uppercase) and any(x in data for x in string.digits)
    return pw_check

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
