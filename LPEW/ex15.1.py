print "Type the filename"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

txt_position = txt_again.tell()
print txt_position

txt_lines = txt_again.readline()
print txt_lines

txt_again.close()
