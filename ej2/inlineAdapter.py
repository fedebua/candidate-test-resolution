import re


class inlineAdapter():
	def __init__(self,inputPath):
		self.inputPath = inputPath
		self.outputVerilogPath = inputPath

	def modifyFile(self):
		file = open(self.inputPath,"r")
		text = file.read()
		file.close()
		#searchValue = re.search(r'initial begin\n((    \S*\[\S*\] = \S*;\n)*)  end\n',text)
		searchValue = re.findall(r'(?s)(?<=initial begin\n).*?(?=end\n)',text)

		registerName = []
		registerParts = re.findall(r'reg \[(.*)\] (\S*) \[(.*)\];\n',text)
		for registerPart in registerParts:
			registerName.append(registerPart[1])
		#memory = searchValue.split()
		i = 0
		for searchData in searchValue:
			#data = re.findall(r'\S*\[\S*\] = \S*;\n',memory)
			bits = []
			numericSystem = []
			values = []
			data = searchData.split('\n')[0 : -1]
			for d in data:
				bits.append(int(re.search(r'(?<== ).*?(?=\')',d).group())) #Search for the number between the space and the ' 
				numericVal = re.search(r"'\S",d).group()[1]
				numericSystem.append(numericVal)
				searchString = r"(?<="+numericVal+r")(.*?)(?=\;)" #Search between numeric type (h, b, etc.) and ; for the value
				values.append(re.search(searchString,d).group())
			
			#####################################################################
			#registerPart = re.search(r'\] (\S*) \[',text).group()
			#registerPart = re.search(r'reg \[(.*)\] (\S*) \[(.*)\];\n',text).group()
			#registerName = re.search(r'\] (\S*) \[',registerPart).group().replace(" ","").replace("[","").replace("]","")
			outputMemPath = registerName[i] + str(bits[0]) + "_" + str(numericSystem[0]) + "_" + "dump.mem"

			output = open(outputMemPath,"w")
			for value in values:
				output.write("%s\n" % value)
			output.close()
			print("Archivo creado: " + outputMemPath)
			readFromDump = "$readmemh("+outputMemPath+", "+registerName[i]+");\n"
			startIndex = text.find('initial begin\n')
			lastIndex = text.find('end\n',startIndex) + len("end")
			#startIndex, lastIndex = searchValue.span()
			text = text[0 : startIndex] + readFromDump + text[lastIndex : :] #Crops the searchValue part and adds the readmem part
			#print(newText)
			i = i+1

		verilogOutputFile = open(self.outputVerilogPath,"w")
		verilogOutputFile.write(text)
		verilogOutputFile.close()
		print("Archivo creado: " + self.outputVerilogPath)


	