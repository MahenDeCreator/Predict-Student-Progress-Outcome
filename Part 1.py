# I declare that my work contains no examples of misconduct, such as plagiarism, or collision.
# Any code taken from other sources is referenced within my code solution.
# Student ID: W1912882
# Date- 12.12.22

student_progress_count_calculation = 0  # count_calculation = 0 before run the programme
student_module_trailer_count_calculation = 0
student_exclude_count_calculation = 0
student_d_module_count_calculation = 0
student_total_count_calculation = 0


def range_check_for_staff_version(your_input_1):  # function for check the range
    if your_input_1 <= 120 and your_input_1 >= 0 and your_input_1 % 20 == 0:
        boolean_save_1 = True

    else:
        print("range error")
        boolean_save_1 = False
        return boolean_save_1


def histogram_count_calculation():  # function for progression outcome
    print("Progress ", student_progress_count_calculation, ":  ", student_progress_count_calculation * "*")
    print("\n")

    print("Trailing ", student_module_trailer_count_calculation, ":  ", student_module_trailer_count_calculation * "*")
    print("\n")

    print("Retriever ", student_d_module_count_calculation, ": ",
          student_d_module_count_calculation * "*")  # student_d_module_count_calculation meant for student do not progress-module retriever count calculation
    print("\n")

    print("Excluded ", student_exclude_count_calculation, ":  ", student_exclude_count_calculation * "*")
    print("\n")
    print("\n")
    print(student_total_count_calculation, " outcomes in total.")




while True:
    boolean_save_2 = False
    while boolean_save_2 == False:

        boolean_range = False
        while boolean_range == False:
            try:
                student_pass_mark_for_staff_version = int(input("Please enter PASS credit :"))
                boolean_range = range_check_for_staff_version(student_pass_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                student_defer_mark_for_staff_version = int(input("Please enter DEFER credit :"))
                boolean_range = range_check_for_staff_version(student_defer_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False

        boolean_range = False
        while boolean_range == False:
            try:
                student_fail_mark_for_staff_version = int(input("Please enter FAIL credit:"))
                boolean_range = range_check_for_staff_version(student_fail_mark_for_staff_version)

            except ValueError:
                print("Integers required")
                boolean_range = False
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        total_mark_for_staff_version = student_pass_mark_for_staff_version + student_fail_mark_for_staff_version + student_defer_mark_for_staff_version
        if total_mark_for_staff_version == 120:  # Total calculated by the sum of 3 credit types
            boolean_save_2 = True
            print("\n")
        else:
            print("Total incorrect")
            print("_____________________________________________________________________")
            print("\n")
            boolean_save_2 = False

    if student_pass_mark_for_staff_version == 120:
        print("Progress")
        print("_____________________________________________________________________")
        print("\n")
        student_progress_count_calculation = student_progress_count_calculation + 1

    elif student_pass_mark_for_staff_version == 100:
        print("Progress–module trailer")
        print("_____________________________________________________________________")
        print("\n")
        student_module_trailer_count_calculation = student_module_trailer_count_calculation + 1

    elif student_fail_mark_for_staff_version >= 80:
        print("Exclude")
        print("_____________________________________________________________________")
        print("\n")
        student_exclude_count_calculation = student_exclude_count_calculation + 1

    else:
        print("Do not progress–module retriever")
        print("_____________________________________________________________________")
        student_d_module_count_calculation = student_d_module_count_calculation + 1

    student_total_count_calculation = student_d_module_count_calculation + student_exclude_count_calculation + student_module_trailer_count_calculation + student_progress_count_calculation
    input_command_for_exit = input(
        "Press 'q' to exit from the program. Press 'y' to check the progression outcome of another student  : ")
    if input_command_for_exit == "q":
        print("\n")
        break  # break used for stop the programme
    else:
        print("\n")
        continue

histogram_count_calculation()
