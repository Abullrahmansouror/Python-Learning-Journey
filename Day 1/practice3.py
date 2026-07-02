## Here I'm asking the users for her/his name using variable (name), this variable will store in the program.
name = input("What's your name ? ")

## Here I'm add this to remove the whitespace after and besfore string.
name = name.strip()

## Here I'm make the user name be capitalize.
name = name.capitalize()

## This make the user name be 
name = name.title()

## Remove the whitespace after and besfore string + Capitalize first word + Capitalize the first and second
name = name.strip().capitalize().title()

## Here I'm print the name user enter it.
print("Hello ! " + name)