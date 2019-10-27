def create_list_from_string(list_creator_string, created_list, item_length, inlist_run):
    #function to create list from this string
    print("Start: create_list_from_string")
    max_item_length = item_length
    print("list_creator_string")
    print(list_creator_string)
    if inlist_run==True:
        list_creator_string = list_creator_string[1:-1]
        max_item_length=len(list_creator_string)

    new_list_item = ""
    end = False
    while end == False:
        print("end:")
        print(end)
        print("list_creator_string[0]")

        if len(list_creator_string)==0:
            end=True
            break

        print(list_creator_string[0])
        if list_creator_string[0] != "[":
            new_list_item = list_creator_string[0:(list_creator_string.find(","))].replace("'", "").strip()
            created_list.append(new_list_item)
            if len(new_list_item)>max_item_length:
                max_item_length=len(new_list_item)

            print("Added new list item:")
            print(new_list_item)
            if list_creator_string.find(",")>0:
                print("Still going (end=False")
                list_creator_string = list_creator_string[(list_creator_string.find(",") + 1):].strip()
                end = False
            else:
                print("Stop going (end=True)")
                list_creator_string=""
                end = True
        else:
            new_list=[]
            new_created_string, new_created_list, new_max_item_length = create_list_from_string(list_creator_string,new_list,max_item_length,True)
            created_list.append(new_created_list)
            list_creator_string=new_created_string
            if new_max_item_length>max_item_length:
                max_item_length=new_max_item_length
            # new_list_item = list_creator_string[0:(list_creator_string.find("]") + 1)].strip()
            # list_creator_string = list_creator_string[(list_creator_string.find("]") + 1):].strip()
            # created_list.append(new_list_item)
            # if len(list_creator_string) > 0:
            #     end = False
            # else:
            #     end = True
    print("End: create_list_from_string")
    return list_creator_string, created_list, max_item_length

def drawing(list, length_max, indrawing):
    list_length = len(list)
    first_line=""
    second_line=""
    third_line=""
    new_first_line=""
    new_second_line=""
    new_third_line=""
    first_line_addon = 0
    third_line_addon = 0
    counter = 0
    while counter < list_length:
        if len(list[counter][0])>1:
            new_first_line, new_second_line, new_third_line, new_first_line_addon, new_third_line_addon = drawing(list[counter], length_max, True)
            first_line = first_line + "+" + "-"*(length_max+2)
            first_line_addon = first_line_addon+1
            second_line = first_line.replace("+","|").replace("-"," ").strip()+" +"+"-"*(length_max-2)+"+"+" |"+"\n"+second_line + "|" + " " + new_second_line + "|"
            third_line = first_line.replace("+","|").replace("-"," ").strip()+" +"+"-"*(length_max-2)+"+"+" |"+"\n"+third_line + "+" + "-" *(length_max+2)
            third_line_addon=third_line_addon+1
        else:
            first_line = first_line + "+" + "-"*(length_max+2)
            if indrawing==False:
                second_line = second_line + "|" + " " + list[counter].ljust(length_max) + " "
            else:
                second_line = second_line + "|" + " " + list[counter] + " "
            third_line = third_line + "+" + "-" *(length_max+2)
        counter = counter+1
    if indrawing==False:
        print(first_line+"+")

    return first_line, second_line, third_line, first_line_addon, third_line_addon

print("Witaj. Przygotowałem dwa przykładowe zestawy danych z których możesz wybrać wykonanie programu.")
dane1 = "['col1', 'col2', 'col3']"
dane2 = "['col1', 'col2', 'col3', ['col4', 'col5', 'col6']]"
choice_list = list(range(1,4))
user_choice = ''
user_choice_digit_or_not = False
while user_choice_digit_or_not==False:
    print("Wybierz jedną z trzech opcji wciskając 1, 2 lub 3: ")
    print("-   1 - wykonanie programu z listą: "+dane1)
    print("-   2 - wykonanie programu z listą: "+dane2)
    print("-   3 - wprowadź listę samemu.")
    user_choice = input("Twój wybór: ")
    user_choice_digit_or_not=user_choice.isdigit()
    if user_choice_digit_or_not==False or (user_choice_digit_or_not==True and int(user_choice) not in choice_list):
        print("Wprowadzono błędą wartość: '"+user_choice+"'")
        print("By spróbować ponownie wciśnij: T/t")
        print("By zakończyć program wciśnij inny klawisz niż: T/t")
        if(input("Kontynuować? ").upper()=="T"):
            print("Wybrałeś by kontynuować. Zaczynamy ponownie...")
            user_choice_digit_or_not=False
        else:
            print("Nie chciałeś próbować ponownie. Koniec programu.")
            exit()

if int(user_choice)==1:
    dane=dane1
elif int(user_choice)==2:
    dane=dane2
else:
    print("Opcja chwilowo niedostępna.")
    exit()

input_list=dane[1:-1]
list=[]
final_string, final_list, final_max_length = create_list_from_string(input_list, list, 0, False)
print(list)

print("Start rysowania")
list_length = len(list)
print("Powstanie kolumn: " + str(list_length))

length_max = final_max_length

first_line, second_line, third_line, first_line_addon, third_line_addon = drawing(list, length_max, False)
second_line= second_line+" |"
third_line = third_line+"+"

print(second_line)
print(third_line)
