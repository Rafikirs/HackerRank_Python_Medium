def fun(s):
    pattern = r'^[\w-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$'
    return re.match(pattern, s) is not None
