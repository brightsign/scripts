#!//usr/bin/python
import sys, os, hashlib


def hashfile(filepath):
    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        sha1.update(f.read())
    finally:
        f.close()
    return sha1.hexdigest()

def touch(fname, times=None):
    with file(fname, 'a'):
        os.utime(fname, times)



def usage():
    print "usage: %s <file> [action]" %(sys.argv[0])
    print "       action:  print or touch - defaults to print if not specified"
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        usage()

    file = sys.argv[1]
    sha1= hashfile(file)
    action    = "print"
    
    if len(sys.argv) > 2:
        action   = sys.argv[2]
    else:
        action   = "print"

    if action in ['touch','Touch','TOUCH']:
        sha1file=file+".sha1."+sha1
        touch(sha1file)
        print sha1file
    elif action in ['print','Print','PRINT']:
        print sha1
    else:
        usage()


if __name__ == "__main__":
    main()
