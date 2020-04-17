import sys
try:
    float("aaabc123")
except:
    err=sys.exc_info()
    print(err[1])

