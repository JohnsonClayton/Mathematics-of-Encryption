#! /bin/python3
'''
encryption_master.py

Clayton Johnson, Chris Vandermeer, Caden Anderson

The Mathematics of Encryption
Dr. Reitenbach

'''

import argparse
import math
import sys

def matrify(string=''):
	# Converts a given string to a 4xn-matrix padded with zeros
	conversion_string = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	converted_matrix = [[],[],[],[]]

	# How large the matrix will be
	MAX_ROWS = 4
	MAX_COLS = math.ceil(len(string)/MAX_ROWS)

	row = 0
	cols = 0	

	for ch in string:
		# Set current position in matrix equal to the index of the character
		if ch in conversion_string:
			converted_matrix[row].append(conversion_string.index(ch))
		else:
			converted_matrix[row].append(0)
		
		# Update position in the matrix
		row = (row + 1) % MAX_ROWS
		if row == 0:
			cols+=1
	while row != 0:
		converted_matrix[row].append(0)
		row = (row + 1) % MAX_ROWS

	#print('Converted matrix: {}'.format(converted_matrix))
	return converted_matrix

def unmatrify(matrix=[]):
	# Converts a 4xn-matrix to a string representation
	converted_string = ''
	MAX_ROWS = 4
	if matrix:
		row = 0
		cols = 0
		conversion_string = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

		while cols < len(matrix[0]):
			element = matrix[row][cols]
			if element < len(conversion_string):
				converted_string += conversion_string[element]
			row = (row + 1) % MAX_ROWS
			if row == 0:
				cols+=1
			
	return converted_string	

def mod_matrix(matrix=[], mod=0):
	# Applies modular arithmetic to each element in the provided matrix
	modular_matrix = matrix
	if mod is not 0:
		for row in range(len(modular_matrix)):
			for col in range(len(modular_matrix[row])):
				modular_matrix[row][col] = modular_matrix[row][col] % mod
				
	return modular_matrix

def matrix_multiply(left=[], right=[]):
	# Matrix Multiplies two matrices
	new_matrix = []
	if left and right:
		# if cols of left doesn't match up with rows of right, then we can't do it
		if len(left[0]) is len(right):
			# Create the new matrix -> same rows as left, same cols as right
			row_vector = []
			for columns in range(len(right[0])):
				# Add this many columns to the row_vector
				row_vector.append(0)
			for rows in range(len(left)):
				# Add this many rows of the row_vector to the matrix
				new_matrix.append(row_vector)

			zip_b = zip(*right)
			zip_b = list(zip_b)

			# This was acquired by https://stackoverflow.com/questions/10508021/matrix-multiplication-in-pure-python 
			new_matrix = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in left]

			# Mod all values by 27
			test_matrix = mod_matrix(new_matrix, 27)			

			# Double check
			#print('Computed matrix multiplication {}'.format(test_matrix))
		else:
			print('matrix multiplication error: matrix size format incorrect')
	else:
		print('matrices not received!')
	return new_matrix

def encode(message=''):
	print('encoding {}'.format(message))

	# This is our A
	encryption_key = [[ 14, 12, 26, 15],
	       		  [  8,  0,  7,  8],
	      		  [  6, 13, 20,  7],
	       		  [  7, 18, 25,  8]]

	# This is our P
	message_matrix = matrify(message)

	# AP=C returns our encoded matrix
	encoded_message_matrix = matrix_multiply(encryption_key, message_matrix)
	encoded_message = unmatrify(encoded_message_matrix)
	print('Your message has been encoded: {}'.format(encoded_message))

def decode(message=''):
	print('decoding {}'.format(message))
	# This is our B
	decryption_key = [[  9, 19, 18, 26],
	       		  [ 24, 26, 25,  5],
	      		  [  2,  2,  3, 22],
	       		  [ 23,  3,  3,  2]]

	# This is our C
	message_matrix = matrify(message)

	# BC=P returns our original message
	decoded_message_matrix = matrix_multiply(decryption_key, message_matrix)
	decoded_message = unmatrify(decoded_message_matrix)
	print('Your message has been decoded: {}'.format(decoded_message))

if __name__=='__main__':
	# Usage: $ python encryption_master.py --[encode|decode] 'message' 
	parser = argparse.ArgumentParser()
	parser.add_argument('--encode', help='encode given \'message\'')
	parser.add_argument('--decode', help='decode given \'message\'')
	args = parser.parse_args()

	if args.encode or args.decode:
		if args.encode:
			encode(args.encode.upper())
		if args.decode:
			decode(args.decode.upper())
	else:
		parser.print_help(sys.stderr)
		sys.exit(1)
