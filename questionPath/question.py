
class question:

	index = 0
	text = "this is the text of the question"
	responseType = 0 # type of response expected, 0 for written, 1 for multiple choice
	possibleAnswer = [] #array of strings
	followUpBy = [] #array of integers for the questions that can follow this 
	relevancy = 100 #the current relevancy assignment for this question
	intent = [] #array of strings that specifies what this question asks for
	similarTo = [] #array of integer for the questions that is similar to this
	specificity=[] #an integer that indicate how specific or pointed the question is. Should general go from less specific to more specific questions
	needUserInput = 0 #does this question need an user input to fill in the blanks

	# def makeQuestion(questionarray): #the input to this function needs to be a dictionary variable of 1 row of the data
	# 	followUpBy = questionarray['followUpBy']
	# 	possible_responses = questionarray['Possible Answer']
	# 	if len(possible_responses) == 0:
	# 		response_type = 0
	# 	else:
	# 		response_type = 1
	# 	similarTo = questionarray['similarTo']
	# 	text = questionarray['Question']

	# def runtest(array):
	# 	print(array['followUpBy'])

	#def __init__(self, questiontext,)






	
