import requests # here we request the pwned website and get the response from the website , means running a website without actually having it
import hashlib # here we are able to do the sha1 hashing
def request_api_data(querry_character): # request the api
    url = 'https://api.pwnedpasswords.com/range/' + querry_character  # this api has a list of all the passwords which are leaked
    res = requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching : {res.status_code} , check the api and try again')
    return res
def get_password_leaks_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines()) # we get a tuple of the hashed password(except the first five alphabets) and the number of times the password has been hacked
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0

def pwned_api_check(password):  # here our password will be in plain format , not the hashed version . we will check if the password exists in the API response or not
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # now we will send the sha1password to the api
    first5_characters,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(first5_characters)
    return get_password_leaks_count(response,tail)

def taking_the_values():
    list1=[""] # write your password in between the double quotes
    for password in list1:
        count=pwned_api_check(password)
        if count:
            print(f'{password} has been hacked {count} times.... you should probably change your password')
        else:
            print(f'{password} was not found. carry on!')
    return 'done!'
taking_the_values()











