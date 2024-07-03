import random
import csv
import methodsfuncs


def main():
    '''
    input_file = "checking.csv"
    output_file = "outputfil.csv"
    methodsfuncs.add_score_column(input_file, output_file)
    '''
    filename="outputfil.csv"

    print("Welcome to the Coraldex!\n")
    while True:
        print("Please select an option:")
        print("1. Based on my tank what should I get?")
        print("2. Coral Recommendation (general-beginner).")
        print("3. Coral Recommendation (general-intermediate).")
        print("4. Coral Recommendation (general-advanced).")
        print("5. Find a coral.")
        print("6. Add a coral.")
        print("7. Non-Photosynthetics")
        print("8. Softies")
        print("9. LPS")
        print("10. SPS")
        print("11. Random Coral!")
        print("12. Exit\n")
        userchoice=input("Enter your choice: ")
        if userchoice=="1":
            methodsfuncs.recommendspec(filename)
        elif userchoice=="2":
            methodsfuncs.recommendgenbeginner(filename)
        elif userchoice=="3":
            methodsfuncs.recommendgenintermediate(filename)
        elif userchoice=="4":
            methodsfuncs.recommendgenadvanced(filename)
        elif userchoice=="5":
            methodsfuncs.findcoral(filename)
        elif userchoice=="6":
            methodsfuncs.addcoral(filename)
        elif userchoice=="7":
            methodsfuncs.nonphotosynthetics(filename)
        elif userchoice=="8":
            methodsfuncs.softies(filename)
        elif userchoice=="9":
            methodsfuncs.lps(filename)
        elif userchoice=="10":
            methodsfuncs.sps()
        elif userchoice=="11":
            methodsfuncs.randomcoralgen(filename)
        elif userchoice=="12":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
