import csv


def cs(name, email, subject, message):
    with open('db.csv', mode="a") as database:
        sv_writer = csv.writer(database)
        JD = [name, email, subject, message]
        sv_writer.writerow(JD)


cs("rohit", "rohit@gmail.com", "test", "hello world")

print('Done')
