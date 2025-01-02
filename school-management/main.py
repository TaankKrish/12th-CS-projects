import mysql.connector

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="krish",
    password="toor",
    database="school_management"
)

cursor = db.cursor()

# Create student table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    grade VARCHAR(10)
)
""")

# Made a function to add student
def add_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade: ")
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(query, values)
    db.commit()
    print("Student added successfully!")

# Made a function to view student
def view_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    if results:
        print("Student Records:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Grade: {row[3]}")
    else:
        print("No records found.")

# Made a function to update student
def update_student():
    student_id = int(input("Enter student ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    grade = input("Enter new grade: ")
    query = "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s"
    values = (name, age, grade, student_id)
    cursor.execute(query, values)
    db.commit()
    print("Student record updated successfully!")

# Made a function to delete student
def delete_student():
    student_id = int(input("Enter student ID to delete: "))
    query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(query, values)
    db.commit()
    print("Student record deleted successfully!")

# Here is the main function, where all the work is done
def main():
    while True:
        print("\n=== School Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Called the main function here
main()
