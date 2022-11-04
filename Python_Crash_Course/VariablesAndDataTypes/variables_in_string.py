first_name = 'ada'
last_name = 'luice'

# 1st put f-> format, outside quotes.
# 2nd put {} outside variable name
full_name = f"{first_name} {last_name}"     # One Way!
full_name = "{} {}".format(first_name,last_name)    # Another Way!

print(f"Hello, {full_name}!")