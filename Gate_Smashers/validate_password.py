# program to validate the password based on the following conditions:
# 6 characters atleast and 30 characters maximum
# should start with an uppercase alphabet
# it can can contain numbers
# It can contain characters !,@,#,$,%,^,&,_,*,.
# it should not have characters /, =, ', " and spaces

pwd = input("Enter Password: ")
valid = False

if 6 <= len(pwd) <= 30:
    if 'A' <= pwd[0] <= 'Z':
        if not ('/' in pwd or '=' in pwd or "'" in pwd or '\"' in pwd or ' ' in pwd):
            valid = True
print(valid)
