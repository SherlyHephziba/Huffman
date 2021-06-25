#!/usr/local/bin/python3
import sys
import argparse
import shutil
import ast

class node:
    def __init__(self, freq, symbol, left=None, right=None):

        self.freq = freq
 
        self.symbol = symbol
 
        self.left = left
 
        self.right = right
 
        self.huff = ''


def find_frequency_dict(text):
    frequency = {}
    for character in text:
        if not character in frequency:
            frequency[character] = 0
        frequency[character] += 1
    return frequency

def storeCode(node, code,val = ""):
    newVal = val + str(node.huff)
 
    if(node.left):
        storeCode(node.left, code, newVal)
    if(node.right):
        storeCode(node.right, code,newVal)
 
    if(not node.left and not node.right):
        code[node.symbol]= newVal

def get_encoded_text(text, code):
    encoded_text = ""
    for character in text:
        encoded_text += code[character]
    return encoded_text

def encode(input_file, output_file):
    print("encoding ", input_file, output_file)
    with open(input_file, 'r+') as file, open(output_file, 'w') as output:
        text = file.read()
        print(text)
        text = text.rstrip()

        frequency = find_frequency_dict(text)

        nodes = []
        code = {}

        for x in frequency:
            nodes.append(node(frequency[x],x))

        while len(nodes) > 1:
 
            nodes = sorted(nodes, key=lambda x: x.freq)
 
            # pick 2 smallest nodes
            left = nodes[0]
            right = nodes[1]
 
            left.huff = 0
            right.huff = 1
 
            newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
 
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
        
        storeCode(nodes[0],code)

        info = {}
        for z in code:
            info[code[z]] = z
        output.write(str(info)+'\n')

        etext = get_encoded_text(text, code)
        print(etext)

        output.write(etext)
  


def decode(input_file, output_file):
    print("decoding ", input_file, output_file)
    with open(input_file, 'r+') as file, open(output_file, 'w') as output:
        
        encode_info = file.readline()
        encoded_text = file.read()
        code = ast.literal_eval(encode_info)
        current_code = ""
        decoded_text = ""

        for bit in encoded_text:
		      	current_code += bit
		      	for z in code:
		      	    if(current_code==z):   
				            character = code[current_code]
				            decoded_text += character
				            current_code = ""
        print(decoded_text)
        output.write(decoded_text)


def get_options(args=sys.argv[1:]):
	parser = argparse.ArgumentParser(description="Huffman compression.")
	groups = parser.add_mutually_exclusive_group(required=True)
	groups.add_argument("-e", type=str, help="Encode files")
	groups.add_argument("-d", type=str, help="Decode files")
	parser.add_argument("-o", type=str, help="Write encoded/decoded file", required=True)
	options = parser.parse_args()
	return options


if __name__ == "__main__":
	options = get_options()
	if options.e is not None:
		encode(options.e, options.o)
	if options.d is not None:
		decode(options.d, options.o)
