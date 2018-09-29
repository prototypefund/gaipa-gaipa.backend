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
        digest = hash.hexdigest()
        verified = hmac.compare_digest(digest, sig)
        print("verified: {0}".format(verified))
        decoded_sso = base64.b64decode(sso)
        print("decoded_sso: {0}".format(decoded_sso))
        import pdb; pdb.set_trace()

        return self.index()
