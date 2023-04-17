
"""
This is a simple script to bypass the captcha
------------
if you have any error with this script
you can ask ai about it 
https://chat.lmsys.org/
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