username = input("Username :")
password = input("Password :")
if username == "Kirito" and password == "Tepza007" :
    print("Welcome to Isekai Shop")
    print("We have :")
    potion = int(input("Potion 20 TZ :"))
    price_I = 20 * potion
    sword = int(input("Sword 400 TZ :"))
    price_II = 400 * sword
    skill = int(input("Star Burst Stream(Skill) 2000 TZ :"))
    price_III = 2000 * skill
    total = price_I + price_II + price_III
    member = input("Do you have Tepza member card :")
    if member == "Yes" :
        print("Tatal price :", (total - (total * 10 / 100)), "TZ")
        print("Thank you")
    elif member == "No" :
        print("Total price :", (total / 1), "TZ")
        print("Thank you")
else :
    print("Username or password is incorrect")
