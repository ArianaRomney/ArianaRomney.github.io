#!/usr/bin/env python3'''
#Name: Ariana Romney
#Directory ID: 114801906
#Date: 2019-04-01
#Assignment: Homework 3
#'''
class Income():                        #this class will give you the income of an employee
    def __init__(self, pay, stipend):    #method that takes in two arguments and sets them to the member variables of the income class
        self.pay = pay
        self.stipend = stipend
    def yearly_income(self):            #method used to calculate the income of an employee for a year, in addition to a stipend that the employee gets every 3 months throughout a year
        return (self.pay * 12) + (self.stipend * 4)

class Employee():                     #this class will give you the information of an employee
    def __init__(self, name, age, pay, stipend):    #method that takes in four arguments and sets the two new arguments to the member variables of the employee class
        self.name = name
        self.age = age
        self.emp_income = Income(pay, stipend)     #new variable that takes two parameters in order to help with calculating salary

    def overall_salary(self):                #method that will calculate the overall salary
        return self.emp_income.yearly_income()

def main():
    person = Employee('Brian', 42, 5000, 2000)
    print(person.overall_salary())

if __name__ == '__main__':main()
