#!/usr/bin/env python3
"""
Debug script for 2025 schedule.
"""

from datetime import date
from employee import Employee

def debug_2025():
    start_date = date(2025, 8, 1)
    
    # Create employees with initial conditions
    ludy = Employee.create_ludy()
    sanye = Employee.create_sanye()
    clari = Employee.create_clari()
    
    print("Initial conditions (August 1, 2025):")
    print(f"Ludy: {ludy.get_schedule_info()}")
    print(f"Sanye: {sanye.get_schedule_info()}")
    print(f"Clari: {clari.get_schedule_info()}")
    print()
    
    employees = {'Ludy': ludy, 'Sanye': sanye, 'Clari': clari}
    current_date = start_date
    
    # Check first 5 days to understand the issue
    for day in range(5):
        print(f"Day {day + 1} - {current_date.strftime('%Y-%m-%d (%A)')}:")
        
        working_count = 0
        for name, employee in employees.items():
            status, shift = employee.get_status_for_day()
            print(f"  {name}: {status} {shift if status == 'Trabajando' else ''}")
            if status == 'Trabajando':
                working_count += 1
        
        print(f"  Working count: {working_count}")
        print()
        
        # Advance all employees to next day
        for employee in employees.values():
            employee.advance_day()
        
        current_date += timedelta(days=1)

if __name__ == "__main__":
    from datetime import timedelta
    debug_2025()