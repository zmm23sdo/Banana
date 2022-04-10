from Admin import login_admin, user, time, name
import random

Random =  str(random.randint(0,999))
Time = str(time.now())
Name = str(name.unicode()+name.unicode())

def test_create_user(page):
    username = "admin"
    password = "qwer@1234"
    login_admin.login(page, username, password)
    role_name = "Role" + Random
    role_des = "Create" + role_name + Time
    user.create_role(page, role_name, role_des)
    username_new = "mvtest"+ Random
    email_new = username_new + "@qa.com"
    name_new = Name
    password_new = "qwer`123"
    user.create_user(page, username=username_new, email=email_new, name=name_new, password=password_new)
    print(f'\nusername_new:{username_new},\nemail_new:{email_new},\nname_new:{name_new},\npassword_new:{password_new}')
