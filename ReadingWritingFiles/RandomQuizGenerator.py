#! python3
#RandomQuizGenerator.py : Creates quizzes with questions and answers in random order, along with the answer key

'''
    Here is what the program does:

        Creates 35 different quizzes.
        Creates 50 multiple-choice questions for each quiz, in random order.
        Provides the correct answer and three random wrong answers for each question, in random order.
        Writes the quizzes to 35 text files.
        Writes the answer keys to 35 text files.

    This means the code will need to do the following:

        Store the provinces and their capitals in a dictionary.
        Call open(), write(), and close() for the quiz and answer key text files.
        Use random.shuffle() to randomize the order of the questions and multiple-choice options.
'''

# 1. Store the quiz data in a dictionary(provinces:capitals)
capitals = {'Beijing':'Beijing', 'Shanghai':'Shanghai', 'Tianjin':'Tianjin', 'Chongqing':'Chongqing', 'Heilongjiang':'Haerbing',
    'Jilin':'Changchun', 'Liaoning':'Changchun', 'Neimenggu':'Huhehaote', 'Hebei':'Shijiazhuang', 'Xinjiang':'Wulumuqi', 
    'Gansu':'Lanzhou', 'Qinghai':'Xining', 'Shaanxi':'Xi\'an', 'Ningxia':'Yinchuan', 'Henan':'Zhengzhou', 'Shandong':'Jinan',
    'Shanxi':'Taiyuan', 'Anhui':'Hefei', 'Hubei':'Wuhan', 'Hunan':'Changsha', 'Jiangsu':'Nanjing', 'Sichuan':'Chengdu', 
    'Guizhou':'Guiyang', 'Yunnan':'Kunming', 'Guangxi':'Nanning', 'Xizang':'Lasa', 'Zhejiang':'Hangzhou', 'Jiangxi':'Nanchang',
    'Guangdong':'Guangzhou', 'Fujian':'Fuzhou', 'Taiwan':'Taibei', 'Hainan':'Haikou', 'Hongkong':'Hongkong', 'Aomen':'Aomen'
    }

# 2. Create the quiz file and shuffle the question order
import random, os

qpath = os.path.join(os.getcwd(), 'Quiz')
if os.path.isdir(qpath) == False:
    os.makedirs(qpath)
os.chdir(qpath)

for quizNum in range(35):
    # Create quiz and answer file

    quizFile = open('CapitalsQuiz%s.txt' % (quizNum+1), 'w')
    answerFile = open('CapitalQuiz_Answers%s.txt' % (quizNum+1), 'w')

    #Write the header for the quiz
    quizFile.write('Name:\t\tDate:\n\n')
    quizFile.write((' '*25)+'Provinces and Capitals Quiz (Form %s)' % (quizNum+1) + '\n\n')

    #Shuffle the order
    provinces = list(capitals.keys())
    random.shuffle(provinces)

    # 3. Create answer options
    for questionNum in range(34):
        # Get right and Wrong answers
        correctAnswer = capitals[provinces[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # random.sample(list, num): selecting num random values from list.
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # 4. Write content to the quiz and answer
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, provinces[questionNum]))
        for i in range(4):
            quizFile.write('\t%s. %s\t' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerFile.write('%s. %s\n' % (questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))
        
    quizFile.close()
    answerFile.close()
