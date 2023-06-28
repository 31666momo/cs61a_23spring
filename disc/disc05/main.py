def tree(label, branches=[]):
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

def find_path(t, x):
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path


def sum_tree(t):
    total = 0
    for b in branches(t):
        total = total + sum_tree(b)
    return label(t) + total

