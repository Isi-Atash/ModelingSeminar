# neptun1 neptun2

def init_bw():
    return 80

def decision(new, list_entry):
#    print '--', new, list_entry
    if new == 'gold':
#        print [1,[1 for x in list_entry]]
        return [1,[1 for x in list_entry]]
    else:
#        print [0,[1 for x in list_entry]]
        return [0,[1 for x in list_entry]]

