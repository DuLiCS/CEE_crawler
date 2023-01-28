"""
This file contains functions of tools using in the CEE crawler
"""

import base64
import hmac
from hashlib import sha1, md5


def hash_hmac(code, key='D23ABC@#56'):
    hmac_code = hmac.new(key.encode(), code.encode(), sha1).digest()
    b_64_t = base64.b64encode(hmac_code).decode()
    return md5(b_64_t.encode()).hexdigest()



