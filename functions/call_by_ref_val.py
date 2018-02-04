def update(input_list):
    input_list.append(4)

def update_modify(input_list):
    input_list = ["ram", "shyam"]


outer_list = [1, 2, 3, 4]
update(outer_list)

print outer_list    #It will print updated list

update_modify(outer_list)

print outer_list    #It will print previous list

