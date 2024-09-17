import pandas as pd
#task 1
print("---------task 1---------")

student_data={
    'Name':['Areeba','Hifza'],
    'Age':[20,19],
    'Semester':[5,5],
    'GPA':[3.9,4]
}

data_writing=pd.DataFrame(student_data)
data_writing.to_csv('students_data.csv',index=False)
read_data=pd.read_csv('students_data.csv')
print(read_data)

# for excel 
data_writing=pd.DataFrame(student_data)
data_writing.to_excel('students_data.xlsx',index=False)
read_data=pd.read_excel('students_data.xlsx')
print(read_data)

#task 2
# Reading from multiple sheets to confirm

print("---------task 2---------")

sheets = pd.read_excel('lab_5_practice.xlsx', sheet_name=None)



print("\nReading from 'Sheet1':")
print(sheets['Sheet1'].head())

print("\nReading from 'Sheet2':")
print(sheets['Sheet2'].head())


#task 3
# restricting duplicates 
import pandas as pd

print("---------task 3---------")

# Initialize the schedule dictionary
schedule = {
    'Course': [''],
    'Monday': [''],
    'Tuesday': [''],
    'Wednesday': [''],
    'Thursday': [''],
    'Friday': [''],
    'Saturday': ['Holiday'],
    'Sunday': ['Holiday']
}

# Dictionary to track occupied periods for each day
occupied_periods = {
    'Monday': set(),
    'Tuesday': set(),
    'Wednesday': set(),
    'Thursday': set(),
    'Friday': set()
}

# Collect input for the course


# List of weekdays
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Main loop to enter periods for different courses
while True:
    course = input("Enter your Course: ")
    schedule['Course'] = [course]
    # Loop through each day to assign periods
    for day in days_of_week:
        while True:  # Inner loop to handle period assignment for each day
            period_number = int(input(f"Enter your period number for {day} (e.g., '1' for Period #1): "))

            # Check if the period is already occupied on that day
            if period_number==0:
                occupied_periods[day].add(period_number)
                schedule[day] = [f"Period #{period_number}"]  
                break  # Exit the loop when a valid input is provided
            elif period_number in occupied_periods[day]:
                print(f"Period #{period_number} is already occupied on {day}. Please choose a different period.")
            else:
                # Mark the period as occupied and update the schedule
                occupied_periods[day].add(period_number)
                schedule[day] = [f"Period #{period_number}"]  # Assign the period to the respective day
                break  # Exit the loop when a valid input is provided

    # Ask user if they want to continue adding to the schedule
    run = int(input("Do you want to continue adding to the schedule? (1/0): "))

    if run == 0:
        break  # Exit the outer loop and stop the program

# Display the updated schedule
print(schedule)

# Save the schedule to a CSV file
data_writing2 = pd.DataFrame(schedule)
data_writing2.to_csv('schedule.csv', index=False)

# Read the CSV file back to verify the content
read_data2 = pd.read_csv('schedule.csv')
print(read_data2)


# task 4
# reading excel 
print("---------task 4---------")

df = pd.read_excel('students_data.xlsx', sheet_name='Sheet1',usecols=['marks'])

filtered_data = df[df['marks'] >85 ]
print(filtered_data)

#task 5 
print("---------task 5---------")


# Load the student data from the Excel file
data = pd.read_excel('students_grade.xlsx')

# Function to calculate GPA for each student
def calculate_gpa(df):
    # Group by each student
    gpa_data = {}
    for student, student_data in df.groupby('Student'):
        # Calculate weighted score sum and total credits
        total_weighted_score = (student_data['Score'] * student_data['Credits']).sum()
        total_credits = student_data['Credits'].sum()
        
        # Calculate GPA as weighted average
        gpa = total_weighted_score / total_credits
        gpa_data[student] = gpa
    return gpa_data

# Calculate GPA for each student
gpa_result = calculate_gpa(data)

# Display the GPA for each student
for student, gpa in gpa_result.items():
    print(f"Student: {student}, GPA: {gpa:.2f}")

# If you want to write the GPA results back to Excel:
gpa_df = pd.DataFrame(list(gpa_result.items()), columns=['Student', 'GPA'])
gpa_df.to_excel('student_gpa.xlsx', index=False)



