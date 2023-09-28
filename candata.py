input_file_name = "ChassisCAN1.dbc"
output_file_name= "CANoutput"

# Read the input text file and filter lines containing "BO_"
lines_with_BO = []
with open(input_file_name, 'r') as input_file:
    for line in input_file:
        if line.startswith('BO_'):
            words = line.split()
            lineToAdd = [words[1]," " ,words[2], "\n"]
            lines_with_BO.append(''.join(lineToAdd))
# Write the filtered lines to another text file
with open(output_file_name, 'w') as output_file:
    for line in lines_with_BO:
        output_file.write(line)