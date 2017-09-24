

import xl_import


def ans_judge(usr_ans):
    """Judge the answer.If the answer is no legal, input again"""

    while usr_ans.lower() not in ['a', 'b', 'c', 'd']:
        usr_ans = raw_input("Your answer is not legal, please input again!\n")
    return usr_ans

def error_judge(correct_ans):
    """The game has 3 opptunities to reanswer the question"""

    global try_num
    pass_mark = None
    usr_ans = ans_judge(raw_input("Your answer write below (A/B/C/D)\n"))

    while pass_mark != 'pass':
        if usr_ans.lower() == correct_ans.lower():
            print "That's correct!\n"
            pass_mark = 'pass'
            return pass_mark
        else:
            if try_num == 0:
                print ("game over!")
                pass_mark = 'false'
                return pass_mark
            else:
                if try_num == 1:
                    usr_ans = ans_judge(raw_input("you have only one chance!\nPlease input again!\n"))
                    try_num -= 1
                    pass_mark = 'false'
                else:
                    print "you have ", try_num, "chances!"
                    usr_ans = ans_judge(raw_input("Please input again!\n"))
                    try_num -= 1

def print_correct_ans(question, answer):
    """if the answer is correct, print the whole sentence"""

    replace_answer = ""
    str_question = str(question)
    str_answer = str(answer)
    answer_pos1 = question.find(str_answer+':')
    answer_pos2 = question.find("\n", answer_pos1+1)

    for i in range(answer_pos1+2, answer_pos2):
        if str_question[i] != "\n":
            replace_answer = replace_answer + str_question[i]

    str_question_split = str_question.split("\n")[0]
    """find the blank and replace it with the correct answer"""
    print str_question_split.replace("___", replace_answer)

    return None

def quiz_main():
    """This is the main function of the quiz game"""

    difficulty = raw_input("Hi there!\n Please choose a difficulty for this game.\n Hard/Medium/Easy\n")
    while not ((difficulty.lower() == 'hard') or (difficulty.lower() == 'medium') or (difficulty.lower() == 'easy')):
        difficulty = raw_input("Please input again!\n")

    question_buf, answer_buf = xl_import.difficulty_choose(difficulty)
    correct_num = 0
    global try_num
    try_num = 3
    for i in range(len(question_buf)):
        print "-------------------------------------------------------"
        print "\n\nPlease read the quiz :\n" + question_buf[i]
        if error_judge(answer_buf[i]) == 'false':
            print ("\n\n\n\n-----------------------------------------")
            print "You answered ", correct_num, "question correctly!"
            break
        else:
            correct_num += 1
            print_correct_ans(question_buf[i], answer_buf[i])
        if correct_num == len(question_buf):
            print ("\n\n\n\n-----------------------------------------"  )
            print ("All correct! Congratulation, You have passed!")
    return None

quiz_main()
