print("hello world")
student_registration = 1484
student_craftmanship = True
course_name = "Python Programming"
print(course_name)
print(student_registration)
email_message = """ Hi,
this is Hillary from HR Department. 
you are hereby ordered to desist your behavior of eating from the cafeteria.
There is no more food for you."""

# len() : used to count the number of characters in a string#
print(len(email_message))

# Learn to access a specific character; use square brackets #
print(course_name[5])
print(email_message[-1])

# slice strings # character at the end index is not included #
print(course_name[0:5])
print(email_message[0:])

# mixup len(), slice strings#
print(len(course_name[0:8]))

# Escape sequence; backslash{\} is used for this#
# Other Escape sequences : #, \', \\, \n, \"
course_description = "Python is a \"simple\" programming language mostly used for backend development."
print(course_description)

# Formatted strings
first = "Hillary"
last = "Koech"
full = f"{first} {last}"
print(full)

# built in functions

print(full.lower())
print(course_description.upper())
print(course_description.title())
print(email_message.strip().title())
print("H" in email_message)
print("swift" not in email_message)
