dane = "['col1', 'col2', 'col3', ['cola', 'colb']]"
input_list=dane[1:-1]
list = []
list_creator_string = input_list

print("Start: "+ list_creator_string)

end = False
while end == False:
    if list_creator_string[0] != "[":
        new_item = list_creator_string[0:(list_creator_string.find(","))].replace("'","").strip()
        list_creator_string = list_creator_string[(list_creator_string.find(",")+1):].strip()
        list.append(new_item)
        if len(list_creator_string)>0:
            end = False
        else:
            end = True
    else:
        new_item = list_creator_string[0:(list_creator_string.find("]")+1)].strip()
        list_creator_string = list_creator_string[(list_creator_string.find("]") + 1):].strip()
        list.append(new_item)
        if len(list_creator_string) > 0:
            end = False
        else:
            end = True

#przed rysowaniem zliczyc najwieksza szerokosc jaka bedzie i kazdą kolumnę tak ustawić
#getting max width
list_length = len(list)
counter = 0
length_max = 0
while counter < list_length:
    if len(list[counter])>length_max:
        length_max = len(list[counter])
    counter = counter+1


list_length = len(list)
counter = 0
first_line = ""
second_line = ""
third_line = ""

while counter < list_length:

    first_line = first_line + "+" + "-"*(length_max+2)
    second_line = second_line + "|" + " " + list[counter].ljust(length_max) + " "
    third_line = third_line + "+" + "-" *(length_max+2)
    counter = counter+1

first_line = first_line+"+"
second_line= second_line+"|"
third_line = third_line+"+"
print(first_line)
print(second_line)
print(third_line)

exit()
print(length)
print("+")




print(list[0])
print(list[1])
print(list[2])
print(list[3])
print("Koniec")
exit()
while list_in_list_check == True:



    if list_creator_string.find("[")>0:

        new_list_start_position = list_creator_string.find("[")-2
        new_list_end_position = list_creator_string.find("]")



        print(list_creator_string[0:new_list_start_position].split("', "))
        exit()

        list_in_list_check = True
    else:
        list_in_list_check = False

