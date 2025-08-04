#!/usr/bin/env python3
"""
Test different starting positions to find a working combination.
"""

from datetime import date, timedelta
from employee import Employee

def test_combination(ludy_cycle, ludy_day, isaac_cycle, isaac_day, genesis_cycle, genesis_day):
    """Test a specific combination of starting positions."""
    
    # Create employees with specific starting positions
    ludy = Employee("Ludy", ludy_cycle, ludy_day, "Morning", 
                   is_resting=(ludy_day > Employee.ROTATION_PATTERN[ludy_cycle][0]))
    isaac = Employee("Isaac", isaac_cycle, isaac_day, "Afternoon", 
                    is_resting=(isaac_day > Employee.ROTATION_PATTERN[isaac_cycle][0]))
    genesis = Employee("Genesis", genesis_cycle, genesis_day, "Morning", 
                      is_resting=(genesis_day > Employee.ROTATION_PATTERN[genesis_cycle][0]))
    
    employees = {'Ludy': ludy, 'Isaac': isaac, 'Genesis': genesis}
    
    # Test first 10 days
    valid_days = 0
    for day in range(10):
        working_count = sum(1 for emp in employees.values() 
                          if emp.get_status_for_day()[0] == 'Working')
        
        if working_count == 2:
            valid_days += 1
        else:
            break
            
        # Advance all employees
        for emp in employees.values():
            emp.advance_day()
    
    return valid_days

def find_working_combination():
    """Find a working starting combination."""
    
    print("Searching for valid starting combinations...")
    
    # Test different combinations
    for ludy_cycle in range(4):
        for ludy_day in range(1, sum(Employee.ROTATION_PATTERN[ludy_cycle]) + 1):
            for isaac_cycle in range(4):
                for isaac_day in range(1, sum(Employee.ROTATION_PATTERN[isaac_cycle]) + 1):
                    for genesis_cycle in range(4):
                        for genesis_day in range(1, sum(Employee.ROTATION_PATTERN[genesis_cycle]) + 1):
                            
                            valid_days = test_combination(ludy_cycle, ludy_day, 
                                                        isaac_cycle, isaac_day, 
                                                        genesis_cycle, genesis_day)
                            
                            if valid_days >= 10:
                                print(f"Found working combination (10+ valid days):")
                                print(f"  Ludy: cycle {ludy_cycle}, day {ludy_day}")
                                print(f"  Isaac: cycle {isaac_cycle}, day {isaac_day}")
                                print(f"  Genesis: cycle {genesis_cycle}, day {genesis_day}")
                                return ludy_cycle, ludy_day, isaac_cycle, isaac_day, genesis_cycle, genesis_day
    
    print("No working combination found.")
    return None

if __name__ == "__main__":
    result = find_working_combination()
    if result:
        print("\nTesting the found combination:")
        ludy_cycle, ludy_day, isaac_cycle, isaac_day, genesis_cycle, genesis_day = result
        
        # Test and show the first few days
        ludy = Employee("Ludy", ludy_cycle, ludy_day, "Morning", 
                       is_resting=(ludy_day > Employee.ROTATION_PATTERN[ludy_cycle][0]))
        isaac = Employee("Isaac", isaac_cycle, isaac_day, "Afternoon", 
                        is_resting=(isaac_day > Employee.ROTATION_PATTERN[isaac_cycle][0]))
        genesis = Employee("Genesis", genesis_cycle, genesis_day, "Morning", 
                          is_resting=(genesis_day > Employee.ROTATION_PATTERN[genesis_cycle][0]))
        
        employees = {'Ludy': ludy, 'Isaac': isaac, 'Genesis': genesis}
        current_date = date(2024, 8, 1)
        
        for day in range(7):
            print(f"\nDay {day + 1} - {current_date.strftime('%Y-%m-%d')}:")
            working_count = 0
            for name, emp in employees.items():
                status, shift = emp.get_status_for_day()
                print(f"  {name}: {status} {shift if status == 'Working' else ''}")
                if status == 'Working':
                    working_count += 1
            print(f"  Working count: {working_count}")
            
            for emp in employees.values():
                emp.advance_day()
            current_date += timedelta(days=1)