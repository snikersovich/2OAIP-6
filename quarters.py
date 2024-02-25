def quarters(*args):
    res = {'I': 0, 'II': 0, 'III': 0, 'IV': 0, }
    for x, y in args:
        if not x or not y:
            continue
        elif x > 0 and y > 0:
            res['I'] = res.get('I') + 1
        elif x < 0 and y > 0:
            res['II'] = res.get('II') + 1
        elif x < 0 and y < 0:
            res['III'] = res.get('III') + 1
        elif x > 0 and y < 0:
            res['IV'] = res.get('IV') + 1
    return res

data = [(1, 1), (-1, 2), (-3, -1)]
for k, v in sorted(quarters(*data).items()):
    print(f'{k}:\t{v}')
