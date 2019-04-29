import webbrowser
import time

total_breaks = 3
break_count = 0
while(break_count < total_breaks):
    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com/watch?v=zb_whk63zdE', new = 1)
    break_count += 1
