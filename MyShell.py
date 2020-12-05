import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","fpr.settings")

import django
django.setup()

from fpr_db.models import Student
from fpr_db.models import Camp

# select * from student
students = Student.objects.all()

#for s in students:
#   print("Student ID:", student.id, "Student:", student)

## select camp where id = 2
#c = Camp.objects.get(id=2)
#print(c.text)
#print(c.lname)


# select student where camp = 1
#students = c.student.set_all()
#for c in students:
    #print(student)


camps = Camp.objects.all()
for c in camps:
    print(c.id)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)