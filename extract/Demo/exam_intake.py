classes_held = int(input("Classes Held: "))
class_attended = int(input("Classes Attended: "))
class_percentage = round((class_attended/classes_held) * 100)

if class_percentage >= 75:
    print("Percentage of Class attended: ",class_percentage, "Eligible for Exams.")

else:
    print("Percentage of Class attended: ", class_percentage, "Not Eligible.")