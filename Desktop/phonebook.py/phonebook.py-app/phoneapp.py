contact_dic ={
1:("Alex",5678),
"Max":45324532,
"Peter":43252532,
}
def find(name):
    name =name.title()
    return contact_dic.get(name,f"{name} is not in the phonebook")
def add(name ,number):
    name = name.title()
    if (name in contact_dic.keys()):
       if input(f"Are you sure you want to update {name} y/n").lower() == "y": 
           contact_dic[name] = number
           return f"Insterted name {name} with number {number} successfully"
       else: 
           if input("Would you like to add something to the end of name") == "y":
               contact_dic[name+input("What would you like to add")] = number
           return f"{name} was not updated"
    else:
        contact_dic[name] = number
        return f"Updated name {name} with number {number} successfully"
def delete(name):
    del contact_dic[name.title()]
    return  name not in contact_dic.keys()
def user_Options(option):
    option = option.title()
    options_map ={
    "Insert":1,
    "1":1,
    "I":1,
    "int":1,
    "Delete":2,
    "Del":2
    }
    return options_map.get(option,f"{option} is not one of the authorized option")