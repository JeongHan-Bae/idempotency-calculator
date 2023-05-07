def faro_in(n: int):
    if n % 2:
        return None
    return list(i // 2 + (1 - i % 2) * n // 2 for i in range(2, n + 2))


def faro_out(n: int):
    if n % 2:
        return None
    return list(i // 2 + (i % 2) * n // 2 for i in range(2, n + 2))


def monge_in(n: int):
    if n % 2:
        return list(range(n, -1, -2)) + list(range(2, n + 1, 2))
    return list(range(n - 1, 0, -2)) + list(range(2, n + 1, 2))


def monge_out(n: int):
    if n % 2:
        return list(range(n - 1, 0, -2)) + list(range(1, n + 1, 2))
    return list(range(n, 0, -2)) + list(range(1, n + 1, 2))


def is_melange(melange_list: list):
    j = 1
    while j < len(melange_list) + 1:
        if bool(melange_list.count(j) - 1):
            return False
        j += 1
    return True


def melange(info: list, melange_list: list):
    if is_melange(melange_list) and len(info) == len(melange_list):
        return list(info[i - 1] for i in melange_list)
    return None


def idempotence(info: list, melange_list: list):
    nbr_m = 0
    info_m = info
    while True:
        nbr_m += 1
        info_m = melange(info_m, melange_list)
        if info_m == info:
            return nbr_m
