# Reachable: these imports and calls use paths through vulnerable packages
from jwt import algorithms        # PyJWT 0.4.2 (CVE-2022-29217 algorithm confusion)
from django.utils import formats  # Django 1.11.29 (CVE-2019-14234 SQL injection)
from rsa import cli               # rsa 3.4 (CVE-2020-13757 timing attack)
from requests import sessions     # requests 2.21.0 (CVE-2023-32681 proxy bypass)

if __name__ == '__main__':
    formats.get_format()
    algorithms.HMACAlgorithm.prepare_key()
    cli.VerifyOperation.perform_operation()
    sessions.SessionRedirectMixin.resolve_redirects()
