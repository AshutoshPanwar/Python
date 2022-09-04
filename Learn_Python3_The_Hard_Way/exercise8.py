# Passing multiple values with format() also called f_string

# Simple string with 4 place holders
formatter = "{} {} {} {}"

# Passing values to string
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
"I Can",
"And",
"I Will",
"Make It!"
))
