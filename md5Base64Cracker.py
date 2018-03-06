#coding:utf-8
#Author:LSA
#Description:Crack md5{d_base64} encryption
#Data:20180306
#Version:v1.0



import md5
import optparse



base64Table = {'+': 62, '/': 63, '1': 53, '0': 52, '3': 55, '2': 54, '5': 57, '4': 56, '7': 59, '6': 58, '9': 61, '8': 60, 'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, 'I': 8, 'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, 'O': 14, 'N': 13, 'Q': 16, 'P': 15, 'S': 18, 'R': 17, 'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24, 'X': 23, 'Z': 25, 'a': 26, 'c': 28, 'b': 27, 'e': 30, 'd': 29, 'g': 32, 'f': 31, 'i': 34, 'h': 33, 'k': 36, 'j': 35, 'm': 38, 'l': 37, 'o': 40, 'n': 39, 'q': 42, 'p': 41, 's': 44, 'r': 43, 'u': 46, 't': 45, 'w': 48, 'v': 47, 'y': 50, 'x': 49, 'z': 51}
base64Table1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h', 34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'}





def crackMd5Base64(cipher):
	cipher = cipher.split('=')[0]
	binString = ''
	binToInt = []
	IntToHex = []
	md5 = []

	for c in cipher:
		number = base64Table[c]
		binNumber = bin(number).split('0b')[-1]
		if len(binNumber) < 6:
			binNumber = '0' * (6-len(binNumber)) + binNumber
		binString = binString + binNumber
	binGroup = [binString[b:b+8] for b in xrange(0,len(binString),8)]
	#print binGroup
	binToInt = [int(binGroup[bg],2) for bg in xrange(0,len(binGroup)-1)]
	#print binToInt
	IntToHex = [hex(binToInt[bti]) for bti in xrange(0,len(binToInt))]
	#print IntToHex
	md5 = [IntToHex[m].replace('0x','') for m in xrange(0,len(IntToHex))]
	for mm in xrange(0,len(md5)):
		if len(md5[mm])!=2:
			md5[mm] = '0' + md5[mm]
	#print md5
	md5string = ''.join(md5)
	print md5string


def encryptMd5Base64(plaintext):
	md5string = ''
	md5Hex = []
	hexToInt = []
	m = md5.new()
	m.update(plaintext.encode(encoding='utf-8'))
	md5string = m.hexdigest()
	#print md5string
	md5Hex = [md5string[ms:ms+2] for ms in xrange(0,len(md5string),2)]
	#print md5Hex
	hexToInt = [int('0x'+md5Hex[mh],16) for mh in xrange(0,len(md5Hex))]
	#print hexToInt
	intToBin = [bin(hexToInt[hti]).replace('0b','') for hti in xrange(0,len(hexToInt))]
	#print intToBin
	for itb in xrange(0,len(intToBin)):
		if len(intToBin[itb]) < 8:
			intToBin[itb] = '0' * (8-len(intToBin[itb])) + intToBin[itb]
	#print intToBin
	binString = ''.join(intToBin) + '0000000000000000'
	#print binString
	asciiBin = [binString[bs:bs+6] for bs in xrange(0,len(binString),6)]
	#print asciiBin
	binToInt = [int(asciiBin[ab],2) for ab in xrange(0,len(asciiBin))]
	#print binToInt
	intToBase64 = [base64Table1[binToInt[itb64]] for itb64 in xrange(0,len(binToInt)-2)]
	#print intToBase64
	md5Base64 = ''.join(intToBase64) + '=='
	print md5Base64
		
		



def main():
	parser = optparse.OptionParser('python %prog '+\
                 '-h <manual>',version="%prog v1.0")
	
        parser.add_option('-d', dest='decrypt', type='string',\
                 help='decrypt the cipher')
        parser.add_option('-e', dest='encrypt', type='string', help='encrypt the plaintext')
	

        (options, args) = parser.parse_args()
         
        cipher = options.decrypt
        plaintext = options.encrypt
	
	if cipher:
		crackMd5Base64(cipher)
	if plaintext:
		encryptMd5Base64(plaintext)
		

	
	




if __name__ == '__main__':
	main()