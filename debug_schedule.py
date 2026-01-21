#!/usr/bin/env python3
"""
Debug script to understand rotation logic issues.
"""

from datetime import date, timedelta
from employee import Employee
from schedule_generator import ScheduleGenerator

def debug_schedule():
    start_date = date(2024, 8, 1)
    
    # Create employees with initial conditions
    ludy = Employee.create_ludy()
    sanye = Employee.create_sanye()
    clari = Employee.create_clari()
    
    print("Initial conditions (August 1, 2024):")
    print(f"Ludy: {ludy.get_schedule_info()}")
    print(f"Sanye: {sanye.get_schedule_info()}")
    print(f"Clari: {clari.get_schedule_info()}")
    print()
    
    employees = {'Ludy': ludy, 'Sanye': sanye, 'Clari': clari}
    current_date = start_date
    
    # Simulate first 7 days to find the issue
    for day in range(7):
        print(f"Day {day + 1} - {current_date.strftime('%Y-%m-%d (%A)')}:")
        
        working_count = 0
        for name, employee in employees.items():
            status, shift = employee.get_status_for_day()
            print(f"  {name}: {status} {shift if status == 'Working' else ''}")
            if status == 'Working':
                working_count += 1
        
        print(f"  Working count: {working_count}")
        
        if working_count != 2:
            print(f"  ERROR: Expected 2 working, got {working_count}")
            break
        
        print()
        
        # Advance all employees to next day
        for employee in employees.values():
            employee.advance_day()
        
        current_date += timedelta(days=1)

if __name__ == "__main__":
    debug_schedule()