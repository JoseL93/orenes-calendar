"""
Employee class to track individual rotation states and schedule calculations.
"""

from datetime import date, timedelta
from typing import Tuple, List

class Employee:
    """
    Represents an employee with their rotation pattern and current state.
    """
    
    # Rotation pattern: work_days, rest_days
    ROTATION_PATTERN = [(3, 2), (3, 2), (4, 1), (4, 2)]
    
    def __init__(self, name: str, initial_cycle_index: int, initial_day_in_cycle: int, 
                 initial_shift: str, is_resting: bool = False):
        """
        Initialize employee with starting conditions.
        
        Args:
            name: Employee name
            initial_cycle_index: Index in rotation pattern (0-3)
            initial_day_in_cycle: Day within the current cycle (1-based)
            initial_shift: 'Morning' or 'Afternoon'
            is_resting: Whether employee is resting on start date
        """
        self.name = name
        self.current_cycle_index = initial_cycle_index
        self.current_day_in_cycle = initial_day_in_cycle
        self.current_shift = initial_shift
        self.is_resting = is_resting
        self.shift_cycle_count = 0  # Tracks shift alternation
        
    def get_current_cycle(self) -> Tuple[int, int]:
        """Get current work/rest cycle."""
        return self.ROTATION_PATTERN[self.current_cycle_index]
    
    def get_status_for_day(self) -> Tuple[str, str]:
        """
        Get status and shift for current day.
        
        Returns:
            Tuple of (status, shift) where status is 'Trabajando' or 'Descanso'
        """
        if self.is_resting:
            return 'Descanso', '-'
        else:
            return 'Trabajando', self.current_shift
    
    def advance_day(self):
        """Advance to next day and update rotation state."""
        work_days, rest_days = self.get_current_cycle()
        total_cycle_days = work_days + rest_days
        
        # Move to next day in cycle
        self.current_day_in_cycle += 1
        
        # Check if we've completed the current cycle
        if self.current_day_in_cycle > total_cycle_days:
            # Move to next rotation pattern
            self.current_cycle_index = (self.current_cycle_index + 1) % len(self.ROTATION_PATTERN)
            self.current_day_in_cycle = 1
            
            # Alternate shift for next work cycle based on cycle pattern:
            # 3-2 tarde, 3-2 mañana, 4-1 tarde, 4-2 mañana
            cycle_shifts = ['Tarde', 'Mañana', 'Tarde', 'Mañana']
            self.current_shift = cycle_shifts[self.current_cycle_index]
        
        # Update resting status based on current position in cycle
        work_days, rest_days = self.get_current_cycle()
        self.is_resting = self.current_day_in_cycle > work_days
    
    def get_schedule_info(self) -> dict:
        """Get detailed schedule information for current day."""
        status, shift = self.get_status_for_day()
        work_days, rest_days = self.get_current_cycle()
        
        return {
            'status': status,
            'shift': shift,
            'cycle': f"{work_days}-{rest_days}",
            'day_in_cycle': self.current_day_in_cycle,
            'cycle_index': self.current_cycle_index
        }
    
    @classmethod
    def create_ludy(cls):
        """
        Create Ludy with initial conditions:
        - August 1st is last day of 4-2 rotation (day 4 of work period)
        - Working morning shift
        """
        return cls("Ludy", 3, 4, "Mañana", is_resting=False)
    
    @classmethod
    def create_sanye(cls):
        """
        Create Sanye with initial conditions:
        - August 1st is second day of 4-1 rotation (day 2 of work period)  
        - Working afternoon shift
        """
        return cls("Sanye", 2, 2, "Tarde", is_resting=False)
    
    @classmethod
    def create_clari(cls):
        """
        Create Clari with initial conditions:
        - August 1st is in rest period, will start working August 2nd
        - Will start with morning shift
        """
        # Position Clari to start working on day 2 (August 2nd)
        # This creates proper staggering with other employees
        clari = cls("Clari", 0, 5, "Tarde", is_resting=True)  # In 3-2 cycle, last rest day
        return clari
