
import re

word_list = ['basic_sphere', 'con_cnc_out_gen', 
'define_test', 'define_null', 
'con_btw_geo_parts', 'define_align_direction', 
'define_temp', 'define_var', 'fracture_laths']

word_list = ['basic_sphere', 'con_cnc__out_gen']




def splitWordList(text=None):
	word_vars = []
	for word in text:
		pattern = re.compile(r'([_])')
		word_split =  re.split(pattern,word)
		chunk = ""
		word_chunks = []
		for x in word_split:
			chunk+=x
			word_chunks.append(chunk)
		word_vars += word_chunks
	print word_vars

splitWordList(word_list)


