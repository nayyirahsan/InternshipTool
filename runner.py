import csv

internships = []
with open('Data_Salaries.csv', 'r', encoding='utf-8') as file:
    csv_file = csv.reader(file)
    next(csv_file)  
    for row in csv_file:
        internships.append(row)

while True:
    print("\nInternship Search\n")

    print("[1] Company Name")
    print("[2] Company Score")
    print("[3] Job Title")
    print("[4] Location")
    print("[5] Salary")
    choice = input("Select [1-5]: ")
    choice = int(choice) - 1
    print(" ")

    while choice > 4 or choice < 0:
        print("Please choose a number between 1 and 5")
        print("[1] Company Name")
        print("[2] Company Score")
        print("[3] Job Title")
        print("[4] Location")
        print("[5] Salary")
        choice = input("Select [1-5]: ")
        choice = int(choice) - 1
        print(" ")

    if choice == 0:
        val = input("Enter the name of the company you're interested in: ")
    elif choice == 1:
        min_score = float(input("Enter the minimum company score: "))
        max_score = float(input("Enter the maximum company score: "))
    elif choice == 2:
        val = input("Enter the name of the internship position you're interested in: ")
    elif choice == 3:
        val = input("Enter the location you're interested in: ")
    else:
        salary_type = input("Do you want to search for hourly or yearly salary? (Enter 'hourly' or 'yearly'): ").strip().lower()
        min_salary = input("Enter the minimum salary: ")
        max_salary = input("Enter the maximum salary: ")

    doesContain = []

    for row in internships:
        if choice == 1: 
            if row[1].strip() != '':  
                score = float(row[1])
                if min_score <= score <= max_score:
                    doesContain.append(row)

        elif choice == 4:  
            salary_str = row[4].strip()

            if salary_type == 'hourly' and 'Per Hour' in salary_str:
                salary_str = salary_str.replace('$', '').replace(',', '').replace('Per Hour', '').replace('\xa0', '').strip()
                if '(' in salary_str:
                    salary_str = salary_str.split('(')[0].strip()
                if salary_str == '':
                    continue  
                if '-' in salary_str:
                    salary_range = salary_str.split('-')
                    min_salary_intern = float(salary_range[0].strip())  
                    max_salary_intern = float(salary_range[1].strip())  
                else:
                    min_salary_intern = float(salary_str)  
                    max_salary_intern = min_salary_intern  

                if min_salary_intern >= float(min_salary) and max_salary_intern <= float(max_salary):
                    doesContain.append(row)

            if salary_type == 'yearly' and 'Per Hour' not in salary_str:
                salary_str = salary_str.replace('$', '').replace(',', '').replace('K', '').replace('\xa0', '').strip()
                if '(' in salary_str:
                    salary_str = salary_str.split('(')[0].strip()
                if salary_str == '':
                    continue  
                if '-' in salary_str:
                    salary_range = salary_str.split('-')
                    min_salary_intern = float(salary_range[0].strip()) 
                    max_salary_intern = float(salary_range[1].strip())  
                else:
                    min_salary_intern = float(salary_str)  
                    max_salary_intern = min_salary_intern  

                if min_salary_intern >= float(min_salary) and max_salary_intern <= float(max_salary):
                    doesContain.append(row)

        elif choice == 3:  
            if val.lower() in row[3].lower():  
                doesContain.append(row)

        elif val.lower() in row[choice].lower():  
            doesContain.append(row)

    if choice == 1 or choice == 3 or choice == 4:
        if len(doesContain) > 0:
            for result in doesContain:
                print(" ")
                print("Company:", result[0])
                print("Company Score:", result[1])
                print("Job Title:", result[2])
                print("Location:", result[3])
                print("Salary:", result[4])
            print(f"\nFound {len(doesContain)} internships matching your search.\n")
        else:
            print(" ")
            print("No internships matched your search criteria.")

    else:
        if len(doesContain) > 1:
            print(f"\nFound {len(doesContain)} internships matching your search.\n")
            cnt = 1
            for name in doesContain:
                print(f"[{cnt}] {name[choice]}")
                cnt += 1
            length = len(doesContain)
            print(" ")
            number = int(input(f"Select [1-{length}]: ")) - 1
            selected = doesContain[number]
        elif len(doesContain) == 1:
            selected = doesContain[0]
        else:
            print("No internships matched your search criteria.")
            selected = None

        if selected:
            print(" ")
            print("Company:", selected[0])
            print("Company Score:", selected[1])
            print("Job Title:", selected[2])
            print("Location:", selected[3])
            print("Salary:", selected[4])

    print("\nWould you like to search again?")
    search_again = input("Enter 'yes' to search again, or anything else to exit: ").strip().lower()

    if search_again != 'yes':
        print("\nThank you for using the Internship Search Program!")
        break
