users = {
    'fasih': '1234',
    'raghib': '2345',
    'fahad': '727'
}

posts = {
    'fasih': ['kill me'],
    'raghib': ['cool'],
    'fahad': ['hello world']
}

def authenticate_user(protected_method):
    def wrapper(username, password):
        if users[username] != password:
            raise Exception(f'Invalid username for {username}')
        return protected_method(username, password)
    return wrapper
            

@authenticate_user
def view_posts(username, password):
    for creator in posts:
        if username == creator:
            print(posts[creator])
            return
    raise Exception('User doesn\'t exist')

try:
    view_posts('fasih', '1234')
    view_posts('raghib', '2346')
    view_posts('fahad', '727')
except Exception as error:
    print(error)