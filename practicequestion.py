import random
import pyinputplus as pyin 

subject = pyin.inputMenu(['Chem', 'Math', 'Add Math', 'Physics', 'Econ'], prompt="Choose what subject you want to do. \n", numbered=True)

dict ={'Physics': ['Lenses', 'SHC'],  'Math': ['Simple and Compound Interest', 'Bearings', 'Functions', 'Matrices'], 'Add Math': ['tbc'], 'Chem': ['Mole Concept', 'no'] }

def elasticity(num_q):
    for i in range(num_q):
        qd_1 = random.randint(1, 10000)
        qd_2 = random.randint(1, 10000)
        p_1 = random.randint(1, 10000) 
        p_2 = random.randint(1, 10000) 
        ans = (qd_2 -qd_1)/(p_2-p_1)
        user_ans = pyin.inputNum("enter the answer")
        if user_ans == ans:
            print('You got it!')
        else:
            print('Here\'s the explanation')
            input()
            print(f'The formula for elasticity is change in quantity demanded over change in price \n The change in quantity deamanded is {qd_2}-{qd_1}, and the change in pric ewould be {p_2}-{p_1}. \n When you divide those, you get {ans}')
            
    
    

if subject == "Chem":
    print(f"You have chosen {subject}")
    topic =pyin.inputMenu(dict[subject], prompt="Choose your topic. \n", numbered=True)
    

elif subject == "Add Math":
    print(f"You have chosen {subject}")
    topic =pyin.inputMenu(dict[subject], prompt="Choose your topic. \n", numbered=True)

elif subject == "Math":
    print(f"You have chosen {subject}")
    topic =pyin.inputMenu(dict[subject], prompt="Choose your topic. \n", numbered=True)

elif subject == "Physics":
    print(f"You have chosen {subject}") 
    topic =pyin.inputMenu(dict[subject], prompt="Choose your topic. \n", numbered=True)

    
elif subject == "Econ":
    print(f"You have chosen {subject}") 
    num_q = pyin.inputInt('How many questions do you want to do? ') 
    elasticity(num_q)
    
 

