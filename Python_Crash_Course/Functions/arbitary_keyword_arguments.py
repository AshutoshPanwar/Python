# (**) tell python to create an empty dictionary

def build_profile(first, last, **user_info):
    """Build a dictionary confaining everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='price', field='phy')
print(user_profile)