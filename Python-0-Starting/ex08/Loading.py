def print_bar(iteration, total, barlen=64):
    progress = iteration/total
    bar_progess = 0.0
    print(f"{int(progress * 100)}%|", end='[')
    for i in range(1, barlen):
        bar_progess = i/barlen
        if i == barlen-1:
             print('>', end='')
        elif bar_progess < progress:
            print('=', end='')
        else:
            print(' ', end='')
    print(f"]| {iteration}/{total}")

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, item in enumerate(lst, 0):
        i += 1
        print_bar(i, total, 128)
        yield item