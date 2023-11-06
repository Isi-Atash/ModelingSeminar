# neptun1 neptun2

def init_bw():
    return 100

def decision(new, list_entry):
#    print '--', new, list_entry
    bw={'bronze': 1, 'silver': 3, 'gold': 10}
    if new == 'gold':
        b=sum([bw[x[0]] for x in list_entry])
        if b+10>init_bw():
            br=len([x for x in list_entry if x[0]=='bronze'])
            si=len([x for x in list_entry if x[0]=='silver'])
            if b+10-br<=init_bw():
                return [1,[0 if x[0]=='bronze' else 0 for x in list_entry]]
    return [1,[1 for x in list_entry]]

