from country import *
from recipe import *
from add_country import *
from add_food import *

def show_menu():
    print('π Welcome~ μ¬νμ λ λλ³ΌκΉμ? β')
    print('1. λλΌ κ²μ ')
    print('2. λλΌ μμ κ²μ')
    print('3. λλΌ μΆκ°')
    print('4. μμ λ©λ΄ μΆκ°')
    print('5. μ’λ£')

def main():
    show_menu()

    space_list = Country()
    recipe_list = Recipe()
    add_country_list = Add_country()
    add_food_list = Add_food()

    while True:
        choose_num = input('λ©λ΄λ₯Ό μ νν΄μ£ΌμΈμ: ')
        if choose_num == '1':
            space_list.show_space()
        elif choose_num == '2':
            recipe_list.show_recipe()
        elif choose_num == '3':
            add_country_list.add_country()
        elif choose_num == '4':
            add_food_list.add_food()
        elif choose_num == '5':
            break

if __name__ == "__main__":
    main()