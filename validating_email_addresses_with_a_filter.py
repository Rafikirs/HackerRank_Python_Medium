# Exercise: Validating Email Addresses With A Filter
# URL: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
# Description: Validating an email address based on an expected format and specific digits

def fun(s):
    pattern = r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return re.match(pattern, s) is not None
