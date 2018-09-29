# -*- coding: utf-8 -*-

from gaipa.backend import _
from Products.Five.browser import BrowserView

import base64
import hashlib
import hmac


class DiscourseSso(BrowserView):
    def __call__(self):
        secret = 'f#jfUQ^yw9a*X@3%#Kn5xF#0k'
        sso = self.request.get('sso')
        sig = self.request.get('sig')
        hash = hmac.new(
            secret,
            sso,
            hashlib.sha256,
        )
        hmac_calculated = base64.b64encode(hash.digest())
        verified = hmac.compare_digest(hmac_calculated, sig)
        print("verified: {0}".format(verified))

        return self.index()
