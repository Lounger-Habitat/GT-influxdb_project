
def progress_bar(total_size):
    now_progress = 0
    while now_progress <= 100:
        new_size = yield
        new_progress = int(new_size/total_size*100)
        if new_progress > now_progress:
            print('\r[{0}{1}%]'.format(int(new_progress/2.0)*'>',new_progress),end='',flush=True)
            now_progress = new_progress