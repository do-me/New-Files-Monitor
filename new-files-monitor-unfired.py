import os,sys,glob,datetime,time

def get_count(s):
    return len(glob.glob(s))
    
def get_time():
    return datetime.datetime.now()

cursor_up = '\x1b[1A'
erase_line = '\x1b[2K'

def clear_console():
    print((cursor_up + erase_line)*6 +cursor_up)
    
def get_delta(wait=0, dir="", repeat=1, file_type="*"):
    """A simple live monitor to get a new files/s rate in a directory. Particularly useful when (chaotically) downloading from multiple threads. Repo: https://github.com/do-me/New-Files-Monitor. A perfect symbiosis with https://github.com/do-me/fast-instagram-scraper"""
    
    if dir != "":
        os.chdir(dir)
        
    i = 0
    while i < repeat:
     
        # first count
        count_0 = get_count(file_type)
        time_0 = get_time()

        # the longer you wait, the more accurate the rate
        time.sleep(wait)
        
        # second count
        count_1 = get_count(file_type)
        time_1 = get_time()
            
        # get delta seconds
        count_delta = count_1-count_0
        time_delta = (time_1-time_0).seconds
        
        try:
            current_rate = count_delta/time_delta
        except:
            current_rate = 0
        
        rate = " {:.2f} files/s\n {} files total\n {} start count\n {} end count\n {} seconds delta\n {} files delta".format(current_rate, count_1, time_0, time_1, time_delta, count_delta)
         
        # for first iteration don't clear console
        if i > 0:
            clear_console()
        print(rate)
        
        i += 1

if __name__ == '__main__':
    get_delta()