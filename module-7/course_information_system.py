'''
Hailey King-Winterton
CSC 500 - Principles of Programming
Critical thinking - M7

Course information system:
    Input: course number
    Output: room number, instructor, meeting time 

Pseudocode:
    START
        Create room number dictionary
        Create instructor dictionary
        Create meeting time dictionary

        Function: get course number
            Prompt user to enter course number
            Remove extra spaces
            Convert course number to uppercase
            Return course number

        Function: retrieve course information
            Look up room number using course number
            Look up instructor using course number
            Look up meeting time using course number
            Return course information

        Function: display course information
            Display course number
            Display room number
            Display instructor
            Display meeting time

        Main function
            Create course dictionaries

            WHILE program is running
                TRY
                    Get course number from user

                    IF course number equals "EXIT"
                        Display closing message
                        Stop loop

                    Retrieve course information
                    Display course information

                EXCEPT value error
                    Display message that a course number is required

                EXCEPT key error
                    Display message that course was not found

        Run main function
    END
'''

# course dictionaries: rooms, instructors, and meeting times
def create_course_data():
    course_rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    course_instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    course_times = {
        "CSC101": "8:00 AM",
        "CSC102": "9:00 AM",
        "CSC103": "10:00 AM",
        "NET110": "11:00 AM",
        "COM241": "1:00 PM"
    }

    return course_rooms, course_instructors, course_times


# prompt for course number
def get_course_number():
    course_number = input("Enter a course number (ie: CSC101) or enter 'exit': ").strip().upper()

    if course_number == "":
        raise ValueError("Course number must be entered. Please try again.")

    return course_number


# retrieves matching values from all three dictionaries
def get_course_information(
        course_number,
        course_rooms,
        course_instructors,
        course_times):

    room_number = course_rooms[course_number]
    instructor = course_instructors[course_number]
    meeting_time = course_times[course_number]

    return room_number, instructor, meeting_time


# displays retrieved course information
def display_course_information(
        course_number,
        room_number,
        instructor,
        meeting_time):

    print("\nCourse Information")
    print("-------------------------")
    print(f"Course Number: {course_number}")
    print(f"Room Number: {room_number}")
    print(f"Instructor: {instructor}")
    print(f"Meeting Time: {meeting_time}")


# main flow of program
def main():
    course_rooms, course_instructors, course_times = create_course_data()

    while True:

        # exception handling for invalid input
        try:
            course_number = get_course_number()

            if course_number == "EXIT":
                print("\nCourse Information System closed.")
                break

            room_number, instructor, meeting_time = get_course_information(
                course_number,
                course_rooms,
                course_instructors,
                course_times
            )

            display_course_information(
                course_number,
                room_number,
                instructor,
                meeting_time
            )

        except ValueError as error:
            print(f"\nError: {error}")

        except KeyError:
            print(
                f"\nSorry, course {course_number} was not found. "
                "Please enter a valid course number."
            )

        print()


if __name__ == "__main__":
    main()