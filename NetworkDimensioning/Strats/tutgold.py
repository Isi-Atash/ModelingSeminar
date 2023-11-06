# neptun1 neptun2

def init_bw():
    return 150

def decision(new, list_entry):
#    print '--', new, list_entry
    bw={'bronze': 1, 'silver': 3, 'gold': 10}
    if new != 'gold':
        br=len([x for x in list_entry if x[0]=='bronze'])
        go=len([x for x in list_entry if x[0]=='bronze'])
        si=len([x for x in list_entry if x[0]=='silver'])
        bwn=sum([bw[x[0]] for x in list_entry])
        if bwn > init_bw()-bw['gold']: 
            return [0,[1 for x in list_entry]]
    return [1,[1 for x in list_entry]]

