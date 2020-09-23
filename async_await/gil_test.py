from gevent import monkey; monkey.patch_all()
import requests
import threading

def a():
    r = requests.get('http://httpstat.us/200?sleep=1000')
    print(r.content)

def b():
    a()
    a()
    print("Done")

def c():
    t1 = threading.Thread(target=a)
    t2 = threading.Thread(target=a)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")

if __name__ == "__main__":
    
    b()