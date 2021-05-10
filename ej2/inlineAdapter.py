import re


class inlineAdapter():
	def __init__(self,inputPath,outputMemPath,outputVerilogPath):
		self.inputPath = inputPath
		self.outputMemPath = outputMemPath
		self.outputVerilogPath = outputVerilogPath

	def modifyFile(self):
		file = open(self.inputPath,"r")
		text = file.read()
		searchValue = re.search(r'initial begin\n((    \S*\[\S*\] = \S*;\n)*)  end\n',text)
		memory = searchValue.group()
		###########################################################################
		data = re.findall(r'\S*\[\S*\] = \S*;\n',memory)
		bits = []
		numericSystem = []
		values = []
		values = []
		for d in data:
			bits.append(int(re.search(r' \d',d).group())) #Search for the number between the space and the ' 
			numericVal = re.search(r"'\S",d).group()[1]
			numericSystem.append(numericVal)
			searchString = r"(?<="+numericVal+r")(.*?)(?=\;)" #Search between numeric type (h, b, etc.) and ; for the value
			values.append(re.search(searchString,d).group())
			
		output = open(self.outputMemPath,"w")
		for value in values:
			output.write("%s\n" % value)

		output.close()

		#####################################################################
		registerPart = re.search(r'] (\S*) \[',text).group()
		registerName = re.search(r' (\S*) ',registerPart).group().replace(" ","")
		readFromDump = "$readmemh("+self.outputMemPath+", "+registerName+");\n"

		startIndex, lastIndex = searchValue.span()
		newText = text[0 : startIndex] + readFromDump + text[lastIndex : :] #Crops the searchValue part and adds the readmem part
		#print(newText)
		file.close()

		verilogOutputFile = open(self.outputVerilogPath,"w")
		verilogOutputFile.write(newText)
		verilogOutputFile.close()


	