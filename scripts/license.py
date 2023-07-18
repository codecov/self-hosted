"""
Note: Script requires use of pycryptodome. pip install pycryptodome
"""
from json import dumps, loads
from Crypto import Random
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from datetime import datetime
import argparse

KEY = bytes([0xfb, 0xe9, 0x1b, 0x34, 0x60, 0xff, 0xe2, 0xa1, 0xfa, 0xe3, 0xd0, 0xf9, 0x8d, 0xa6, 0x25, 0x7f])
BS = 16


def pad(s):
    padding_length = BS - len(s) % BS
    padding = bytes([padding_length] * padding_length)
    return s + padding

def unpad(s):
    return s[:-s[-1]]


def create_license(expires, company, seats=None, repos=None, url=None, trial=True, pr=True):
    date = expires
    datetime.strptime(date, '%Y-%m-%d')
    users = seats
    if users:
        users = int(users)
    if repos:
        repos = int(repos)
    res = {
        'company': company,
        'expires': f'{date} 00:00:00',
        'url': url,
        'trial': trial,
        'users': users,
        'repos': repos,
        'pr_billing': pr
    }
    iv = Random.new().read(AES.block_size)
    des = AES.new(KEY, AES.MODE_CBC, iv)
    cipher_text = b64encode(iv + des.encrypt(pad(dumps(res).encode('utf-8')))).decode('utf-8')
    print(f'''{cipher_text}

License expires on {date}

---- Internal purposes only ----
{res}
''')


def decode_license(license):
    license = b64decode(license)
    iv = license[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    print(loads(unpad(cipher.decrypt(license[16:]))))


def main(args=None):
    expires = None
    company = None
    seats = None
    repos = None
    license = None
    url = None
    trial = True

    parser = argparse.ArgumentParser(prog='codecov key gen', add_help=True,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(title='Commands')

    make = subparsers.add_parser('new')
    make.add_argument('--expires', action="store", required=True,
                      help="expires in YYYY-MM-DD")
    make.add_argument('--trial', action="store_true",
                      default=False, help="set to true if trial is needed")
    make.add_argument('--pr', action="store_true",
                      default=False, help="set to true if this license requires PR Author Billing")
    make.add_argument('--company', action="store", required=True, help="Company name")
    make.add_argument('--url', action="store", help="(Optional) Company url endpoint")
    make.add_argument('--users', action="store", dest="seats", nargs="?",
                      default=None, help="(Optional) Number of seats")
    make.add_argument('--repos', action="store", dest="repos", nargs="?",
                      default=None, help="(Optional) Number of repos")

    check = subparsers.add_parser('check')
    check.add_argument('--license', nargs=1, required=True)

    pref = parser.parse_args(args)

    if getattr(pref, 'license', None):
        decode_license(pref.license[0])
    else:
        create_license(pref.expires, pref.company, seats=pref.seats,
                       repos=pref.repos, url=pref.url, trial=pref.trial, pr=pref.pr)


if __name__ == "__main__":
    main()