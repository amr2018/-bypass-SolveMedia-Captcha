
"""
This is a simple script to  bypass SolveMedia Captcha
------------------------------------------------------------------------------------------------------
install 2captcha lib : https://pypi.org/project/2captcha-python/
------------------------------------------------------------------------------
# key from your 2captha account create account from here : https://bit.ly/3MkkuPJ
# You need to make a deposit at least $2
# select "Developer" as account type
# copy your api key from your account
"""

from twocaptcha import TwoCaptcha
import key
import sys

from twocaptcha import TwoCaptcha

solver = TwoCaptcha(key.apikey)

try:
    result = solver.normal('test.jpg')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))
