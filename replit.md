# Work Rotation Schedule Generator

## Overview

This is a comprehensive Python application that generates work rotation schedules for a team of employees in Excel format, available both as a command-line tool and web application. The system manages complex rotation patterns where employees alternate between working and resting periods, with different cycle lengths and shift assignments (Morning/Afternoon). The application tracks individual employee states and ensures proper coverage by validating that exactly 2 employees are working while 1 is resting at any given time. The output is a comprehensive Excel workbook with color-coded schedules for easy visualization.

## Recent Changes (August 2025)

✅ **Web Application Implementation**: Created Flask-based web interface for easy month/year selection and calendar generation
✅ **Enhanced Calendar Format**: Updated monthly calendars with separate colored cells for each employee  
✅ **Spanish Interface**: Complete Spanish language implementation throughout web interface
✅ **Color-Coded System**: Implemented blue (morning), orange (afternoon), green (rest) color scheme
✅ **Multiple Calendar Views**: Added individual employee calendars alongside general monthly views
✅ **Continuity System**: Fixed month-to-month continuity maintaining rotation sequence from August 2025 reference point
✅ **Docker Implementation**: Added complete Docker support with Dockerfile, docker-compose.yml, and deployment documentation
✅ **Preview Display Fix**: Corrected preview to show dates and Spanish weekdays properly

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Design Pattern
The application follows an object-oriented design with clear separation of concerns:

- **Employee Class**: Encapsulates individual employee state including rotation cycles, current position in cycle, shift assignments, and rest periods
- **ScheduleGenerator Class**: Orchestrates schedule generation logic, manages multiple employees, and handles validation
- **Command-Line Interface**: Provides user-friendly access to schedule generation with configurable parameters

### Rotation System Architecture
The system implements a complex rotation pattern with:
- **4-stage rotation cycles**: Each with different work/rest day combinations [(3,2), (3,2), (4,1), (4,2)]
- **Shift alternation**: Employees rotate between Morning and Afternoon shifts
- **State tracking**: Maintains current cycle index, day within cycle, and rest status for each employee
- **Validation logic**: Ensures exactly 2 employees work while 1 rests daily

### Data Flow
1. Initialize employees with predefined starting states (Ludy, Isaac, Genesis)
2. Generate daily schedules by advancing each employee's state
3. Validate daily coverage requirements (exactly 2 working, 1 resting)
4. Export results to Excel format with professional formatting and multiple worksheets

### Output Architecture
The system generates a comprehensive Excel workbook with multiple worksheets:
- **General schedule**: Daily overview showing all employee statuses with color-coded cells
- **Individual schedules**: Separate worksheets for each employee with detailed rotation tracking
- **Excel formatting**: Professional styling with borders, colors, and auto-sized columns
- **Color coding**: Morning shifts (light blue), Afternoon shifts (light yellow), Rest days (light gray)

## External Dependencies

### Core Python Libraries
- **datetime**: Date manipulation and calculations for schedule generation
- **csv**: Legacy CSV export functionality (still available)
- **argparse**: Command-line argument parsing
- **typing**: Type hints for better code maintainability

### Third-Party Dependencies
- **openpyxl**: Excel file generation with advanced formatting, styling, and multiple worksheets

### File System Dependencies
- **Excel file output**: Generates professional Excel workbook in specified output directory
- **Command-line execution**: Designed to run as standalone script with configurable parameters

The application is self-contained with minimal external dependencies, requiring only the openpyxl library for Excel functionality.