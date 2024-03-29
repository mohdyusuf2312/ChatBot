import re
import long_res as long
logo = '''
  ______                                            ____         ______                
 .~      ~. |         |       .'.       `````|````` |    ~.     .~      ~.  `````|````` 
|           |_________|     .''```.          |      |____.'_   |          |      |      
|           |         |   .'       `.        |      |       ~. |          |      |      
 `.______.' |         | .'           `.      |      |_______.'  `.______.'       |      
                                                                                        
'''
def msg_prob(user_msg, recognised_word, single_res = False, required_words = []):
    msg_certainty = 0
    has_required_words = True

    for word in user_msg:
        if word in recognised_word:
            msg_certainty +=1
        
    percentage = float(msg_certainty)/float(len(recognised_word))

    for word in required_words:
        if word not in user_msg:
            has_required_words = False
            break

    if has_required_words or single_res:
        return int(percentage*100)
    else:
        return 0
    
def check_msg(msg):
    high_prob_list = {}
    def res(bot_res, list_of_words, single_res = False, required_words = []):
        nonlocal high_prob_list
        high_prob_list[bot_res] = msg_prob(msg, list_of_words,single_res, required_words)
    
    #res__________________________________________________________________________________
    res('Hello!',['hello','hi','hiii','yup','hey','heyo'],single_res = True)
    res('I\'m doing fine, and you?', ['how','are','are','you','doing'],required_words = ['how','you'])
    res('Thank you!', ['i','love','chat','bot'],required_words=['chat','bot'])
    res(long.R_EATING, ['What','you','eat'], required_words=['you','eat'])

    best_match = max(high_prob_list, key = high_prob_list.get)
    # print(high_prob_list)
    # return best_match
    if high_prob_list[best_match] < 1:
        return long.unknown()
    else:
        return best_match

def get_res(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    res = check_msg(split_msg)
    return res


while True:
    print("Chatbot : " + get_res(input("You : ")))