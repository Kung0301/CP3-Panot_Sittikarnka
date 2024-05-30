def login() :
    username = input("Username :")
    password = input("Password :")
    if username == "Kirito" and password == "Tepza007":
        return show_menu()
    else :
        return login()
def show_menu() :
    print("Welcome")
    print("1) Vat Calculator")
    print("2) Price Calculator")
    return menu_select()
def menu_select() :
    userselected = int(input(">>"))
    if userselected == 2 :
        return price_cal()
def vat_cal(total_price) :
    vat = 7
    result = total_price+(total_price*vat/100)
    return result
def price_cal() :
    price_1 = int(input("First product price :"))
    price_2 = int(input("Second product price :"))
    return vat_cal(price_1+price_2)

print(login())