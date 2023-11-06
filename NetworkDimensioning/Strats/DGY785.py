# DGY785
# python3

def init_bw():
    return 100

def decision(new, list_entry):
    # Always accept gold claims
    if new == 'gold':
        return [1, [1 for _ in list_entry]]

    bw_requirements = {'bronze': 1, 'silver': 3, 'gold': 10}
    used_bw = sum(bw_requirements[claim[0]] for claim in list_entry)
    available_bw = init_bw() - used_bw

    if new == 'silver' and available_bw >= bw_requirements['gold']:
        return [1, [1 for _ in list_entry]]

    return [0, [1 for _ in list_entry]]
