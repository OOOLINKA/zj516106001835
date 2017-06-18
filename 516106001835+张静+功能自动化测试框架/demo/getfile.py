
class GetFile:
	def getAnswer(self, filePath):
		answers = []
		with open(filePath, 'r') as fr:
			# flag = True
			
			for line in fr:
				if line[-1] == '\n':
					line = line[:-1]
				line = line[1:-1]
				if line.strip() != "": 
					line = line.strip().replace(' ','')
					data = map(int, line.split(','))
					answers.append(data)
					# print(data)
		answers = sorted(answers, key=lambda a: (len(a), a))
		return answers
	
