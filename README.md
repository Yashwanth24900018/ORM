# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

<img width="1001" height="557" alt="image" src="https://github.com/user-attachments/assets/82957a3d-575d-4445-961b-5498dd82ddf9" />




## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

## admin.py:

    from django.contrib import admin
    from . models import car
    admin.site.register(car)
    class carAdmin(admin.ModelAdmin):
      list_display = ('car_id','brand','model''year','price')
## models.py:
    from django.db import models
      class car(models.Model):
        car_id = models.IntegerField(primary_key=True)
        brand = models.CharField(max_length=20)
        model = models.CharField(max_length=20)
        year = models.DateField()
        price = models.IntegerField()

## OUTPUT

<img width="1918" height="1048" alt="Screenshot 2025-09-21 204212" src="https://github.com/user-attachments/assets/61fb3c21-0cba-4907-8b77-6ac74962f11d" />




## RESULT
Thus the program for creating a database using ORM hass been executed successfully
