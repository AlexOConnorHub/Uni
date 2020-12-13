import csv, os, time, datetime, json, re

public = 'public/'
private = 'private/'

class chatObject:
    def __init__(self, sender: str, message: str, time: int = int(time.mktime(datetime.datetime.utcnow().timetuple())*1000)):
        self.sender  = sender
        self.message = message
        self.time    = time
        self.id      = hash(self)

    def __str__(self):
        return f'{self.sender} said {self.message} at {self.time}'

    def __repr__(self):
        return f'chatObject({self.sender}, {self.message}, {self.time})'

    def __hash__(self):
        return hash(f'{self.sender}{self.message}{self.time}')

    def getId(self):
        return self.id

    def getChat(self):
        return {
            "sender":self.sender,
            "message":self.message,
            "time":self.time,
            "id":self.id
        }

def checkLogin(login: dict) -> bool:
    '''
    Master Login code
    '''
    user = getUserLogin(login['uname'])
    if user == None:
        return user
    else:
        return (checkPass(login['pass'], user['hash']))

def validUser(currentUsers, toValidate):
    """ 
    >>> validUser( { 'test': 'trueCookie' }, { 'uname' : 'test', 'cookie' : 'trueCookie' })
    True
    >>> validUser( { 'test': 'trueCookie' }, { 'uname' : 'test', 'cookie' : 'falseCookie' })
    False
    >>> validUser( { 'test': 'falseCookie', 'testUser' : 'trueCookie' }, { 'uname' : 'testUser', 'cookie' : 'trueCookie' })
    True
    """
    return currentUsers[toValidate['uname']] == toValidate['cookie']

def giveCookie() -> str:
    """
    >>> type(giveCookie())
    <class 'str'>
    >>> type(giveCookie())
    <class 'str'>
    >>> type(giveCookie())
    <class 'str'>
    """
    return str(hash(os.urandom(60)))

def getUserLogin(name: str) -> dict:
    with open(private + 'pass.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if (row['name'] == name):
                return row
    return None

def  makeLogin(uname, pass1, pass2) -> str:
    '''
    Makes login
    '''
    login = { 'uname': uname ,'pass' : pass1 }
    if (login['pass'] == pass2):
        if (getUserLogin(login['uname']) != None):
            return False
        with open(private + 'pass.csv', 'a') as file:
            file.write(','.join([login['uname'],hashword(login['pass'])]) + '\n')
        return '/'
    return '/html/chat/signup.html'

import hashlib
import binascii

def checkPass(userPassword: str, verifiedPassword: str) -> bool:
    '''
    Checks the userPassword against the verifiedPassword
    Pass user, then verified
    >>> checkPass('password', '679177222e940525d48c3243a8c4306f8c2aaa8a1a7755aaaf313b3d1519f18194a9380ff362537674b32fed9020aa334ad1fbd9e10e217eeaaf71bf403b91b3bef48cf34f0bd623e024f9ac1a39ab8b37e8ea7825b63bce249de89c3cd52ab3')
    True
    >>> checkPass('passphrase', '679177222e940525d48c3243a8c4306f8c2aaa8a1a7755aaaf313b3d1519f181ac162bb5132ac5778ec4777e657d6045a5c4bb622c3d4048cef02eaef542b1da515315b0ad4f19f19b2d191037df89c1ad461390a0e64afe94b8cf91196fced9')
    True
    >>> checkPass('fakePassword', 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
    False
    '''
    return hashword(userPassword, verifiedPassword[:64].encode('ascii')) == verifiedPassword

def hashword(password: str, salt: str = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')) -> str:
    '''
    Makes the password hash
    Pass user password to make new pass
    Pass salt to get same salt
    >>> len(hashword('password'))
    192
    >>> len(hashword('passphrase'))
    192
    >>> hashword('passphrase', '679177222e940525d48c3243a8c4306f8c2aaa8a1a7755aaaf313b3d1519f181'.encode('ascii'))
    '679177222e940525d48c3243a8c4306f8c2aaa8a1a7755aaaf313b3d1519f181ac162bb5132ac5778ec4777e657d6045a5c4bb622c3d4048cef02eaef542b1da515315b0ad4f19f19b2d191037df89c1ad461390a0e64afe94b8cf91196fced9'
    '''
    pwdhash = binascii.hexlify(hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000))
    return (salt + pwdhash).decode('ascii')

import fileinput

def replacePassphrase(uname, oldPass, newPass1, newPass2):
    print(uname, oldPass, newPass1, newPass2)
    if not ((newPass1 == newPass2) and (checkLogin({ 'uname': uname, 'pass': oldPass }))):
        return False
    for line in fileinput.FileInput(private + "pass.csv", inplace=True):
        if line[:len(uname)] == uname:
            print(uname + ',' + hashword(newPass1) + '\n', end='')
        else:
            print(line, end='')
    return True

# On load, make banned words list
fileIO = open(private + 'profane.bad', 'r')
profane = json.loads( open(private + 'profane.bad', 'r').read())
fileIO.close()

def isClean(message):
    """ 
    >>> isClean('clean message')
    True
    >>> isClean("Can't say torture")
    False
    >>> isClean('Can I say ToRTure???')
    False
    """
    global profane
    for word in re.sub('[-_/.~,?!@#]', ' ', message).split(' '):
        if word.lower() in profane:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()