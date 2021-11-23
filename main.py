import sys
import decoding, encoding

if len(sys.argv) == 3:
    name = sys.argv[2]
    rabota = sys.argv[1]
    if rabota == '-e':
        encoding.encode(name)
        print('got it')
    else:
        decoding.decode(name)
        print('got it -d')
        
    