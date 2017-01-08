def expandData(data, length):
    while len(data) < length:
        data += "0" + ''.join("0" if n == "1" else "1" for n in data[::-1])
    return data[:length]

def contractChecksum(checksum):
    while not len(checksum) & 1:
        checksum = ''.join("1" if x == y else "0" for x, y in zip(checksum[0::2], checksum[1::2]))
    return checksum

print (contractChecksum(expandData("11101000110010100", 272)))
print (contractChecksum(expandData("11101000110010100", 35651584)))



def checksum(s):
  checksum = ''
  for x, y in zip(s[0::2], s[1::2]):
    if x == y:
      checksum += '1'
    else:
      checksum += '0'
  return checksum

# w = '1010101101110111100010110010101100000101011101010101010101010100111010100111110000101011100010010100001011101110001010101001101010001'


# def makelong(s):
#   if len(s) < 2000000:
#     return makelong(s+s)
#   else:
#     return s


# r = makelong(w)
# print (len(r))

# rc = checksum(r)
# print (len(rc))


# import re

# data = '10010000000110000'
# length = 35651584

# def reversed_string(a_string):
#    return a_string + "0" + a_string[::-1].replace('0','X').replace('1','0').replace('X','1')

# def checksum(str):
#    arr = re.findall('..', str)
#    data = ""
#    for val in arr:
#        if val[0] == val[1]: data += "1"
#        else: data += "0"
#    return data

# while(len(data) <= length):
#    data = reversed_string(data)

# data = data[:length]

# while(True):
#    data = checksum(data)
#    if (len(data) % 2 != 0):
#        break

# print ("[Done] %s" % data)