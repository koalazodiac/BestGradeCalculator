menu = """
Welcome to the "Best Grade Plan" Calculator
1. Enter Student Name and ID
2. Calculate the final letter grade based on both plans and determine the best plan
3. Exit
Enter your selected option: """

LABO_MAX = 10 # Max lab grade
PROJ_MAX = 15 #Max project grade
TEST_MAX = 100 #Max midterm test grade
EXAM_MAX = 100 #Max final exam grade

#Test weight
LAB_TOTAL = 15 #Total Lab weight for both plans
LAB = LAB_TOTAL/3 #Lab weight for both plans
PROJECT = 15 #Project weight for both plans
PLAN_A_TEST = 30 #Plan A midterm test weight
PLAN_A_EXAM = 40 #Plan A exam weight
PLAN_B_TEST = 20 #Plan B midterm test weight
PLAN_B_EXAM = 50 #Plan B exam weight

#Pre-set variable to verify if option 1 is completed
info_entered = False

#Pre-set variable to begin the while loop and is not processed
option = 1
while option != 3:
    #User inputs new option and is processed
    option = int(input(menu))
    if option == 1:
        info_entered = True 
        first_name = input("Please enter first name: ")
        #Conditions
        if (first_name[0].islower()) or (not first_name.isalpha()) or (not first_name[1:].islower()):
            #Reset verification
            info_entered = False
            print("Error! Please enter a valid first name.")
            #Return to menu
            continue
        
        #Similar to first name
        last_name = input("Please enter last name: ")
        if (last_name[0].islower()) or (not last_name.isalpha()) or (not last_name[1:].islower()):
            info_entered = False
            print("Error! Please enter a valid last name.")
            continue
            
        ID = input("Please enter student ID: ")
        if len(ID) != 7 or ID.isdigit() == False:
            info_entered = False
            print("Error! Please enter a valid student ID.")
            continue
        

    # option 2 code  
    elif option == 2:
        
        #Verification for completion of option 1
        if not info_entered:
            print("must enter name and ID in option 1 first")
            continue
        
        #User input grades into new variables that will be used in calculation
        Lab1_Grade = int(input("Enter lab1 grade: "))
        if Lab1_Grade > LABO_MAX:
            #Error verification
            print("Error! Please enter a lab grade <=", LABO_MAX)
            continue
        Lab2_Grade = int(input("Enter lab2 grade: "))
        if Lab2_Grade > LABO_MAX:
            print("Error! Please enter a lab grade <=", LABO_MAX)
            continue
        Lab3_Grade = int(input("Enter lab3 grade: "))
        if Lab3_Grade > LABO_MAX:
            print("Error! Please enter a lab grade <=", LABO_MAX)
            continue
        Pro_Grade = int(input("Enter project grade: "))
        if Pro_Grade > PROJ_MAX:
            print("Error! Please enter a project grade <=", PROJ_MAX)
            continue
        Test_Grade = int(input("Enter test grade: "))
        if Test_Grade > TEST_MAX:
            print("Error! Please enter a test grade <=", TEST_MAX)
            continue
        Exam_Grade = int(input("Enter exam grade: "))
        if Exam_Grade > EXAM_MAX:
            print("Error! Please enter an exam grade <=", EXAM_MAX)
            continue
        
        #Calculation Plan A
        a1_planA = (Lab1_Grade / LABO_MAX)*LAB
        a2_planA = (Lab2_Grade / LABO_MAX)*LAB
        a3_planA = (Lab3_Grade / LABO_MAX)*LAB
        b_planA = (Pro_Grade / PROJ_MAX)*PROJECT
        c_planA = (Test_Grade / TEST_MAX)*PLAN_A_TEST
        d_planA = (Exam_Grade / EXAM_MAX)*PLAN_A_EXAM
        PlanA = a1_planA+a2_planA+a3_planA+b_planA+c_planA+d_planA
        
        #Calculation Plan B
        a1_planB = (Lab1_Grade / LABO_MAX)*LAB
        a2_planB = (Lab2_Grade / LABO_MAX)*LAB
        a3_planB = (Lab3_Grade / LABO_MAX)*LAB
        b_planB = (Pro_Grade / PROJ_MAX)*PROJECT
        c_planB = (Test_Grade / TEST_MAX)*PLAN_B_TEST
        d_planB = (Exam_Grade / EXAM_MAX)*PLAN_B_EXAM
        PlanB = a1_planB+a2_planB+a3_planB+b_planB+c_planB+d_planB
        
           
        #if loop to verify the best grading-scheme
        if PlanA > PlanB:
            print("The best grading-scheme is Plan A, grade achieved:")
            
            #Calculation for Plan A letter grade
            #Letter_grade is a new variable for displaying letter grade in print()
            if PlanA >= 95:
                Letter_grade = "A"
            elif PlanA>= 90:
                Letter_grade = "A-"
            elif PlanA>= 84:
                Letter_grade = "B"
            elif PlanA>=75:
                Letter_grade = "B-"
            elif PlanA>=70:
                Letter_grade = "C"
            elif PlanA>= 60:
                Letter_grade = "D"
            else:
                Letter_grade = "F"
            
            print(last_name, ",", first_name, "ID:", ID, "Final Grade:", PlanA, "%", "Letter Grade:", Letter_grade)
        elif PlanA < PlanB:
            
            print("The best grading-scheme is Plan B, grade achieved:")
            
            #Calculation for Plan B letter grade
            if PlanB >= 95:
                Letter_grade = "A"
            elif PlanB>= 90:
                Letter_grade = "A-"
            elif PlanB>= 84:
                Letter_grade = "B"
            elif PlanB>=75:
                Letter_grade = "B-"
            elif PlanB>=70:
                Letter_grade = "C"
            elif PlanB>= 60:
                Letter_grade = "D"
            else:
                Letter_grade = "F"
            print(last_name+", "+first_name, "ID: "+ID, "Final Grade:", PlanB, "%", "Letter Grade:", Letter_grade)
        else:
            print("Both Plan A and Plan B are the best grading-scheme, grade achieved:")
            if PlanA >= 95:
                Letter_grade = "A"
            elif PlanA>= 90:
                Letter_grade = "A-"
            elif PlanA>= 84:
                Letter_grade = "B"
            elif PlanA>=75:
                Letter_grade = "B-"
            elif PlanA>=70:
                Letter_grade = "C"
            elif PlanA>= 60:
                Letter_grade = "D"
            else:
                Letter_grade = "F"
            
            print(last_name, ",", first_name, "ID:", ID, "Final Grade:", PlanA, "%", "Letter Grade:", Letter_grade)
            
    # option 3 code  
    elif option == 3:
        print("Exiting...")
    
    #Error code for any inputted option thats other than 1-3
    else:
        print("Invalid option. Please choose a valid option.")
