import csv

# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([10, 43, 1000])
#     writer.writerow([17, 46, 179])



with open("data.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for i in reader:
        print(i)