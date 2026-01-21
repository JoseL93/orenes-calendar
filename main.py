#!/usr/bin/env python3
"""
Work Rotation Schedule Generator
Command-line tool to generate work schedules based on rotation patterns.
"""

import argparse
import sys
from datetime import datetime, timedelta
from schedule_generator import ScheduleGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate work rotation schedules')
    parser.add_argument('--start-date', type=str, default='2025-08-01',
                       help='Start date in YYYY-MM-DD format (default: 2025-08-01)')
    parser.add_argument('--days', type=int, default=90,
                       help='Number of days to generate (default: 90)')
    parser.add_argument('--output-dir', type=str, default='.',
                       help='Output directory for CSV files (default: current directory)')
    
    args = parser.parse_args()
    
    try:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d').date()
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD")
        sys.exit(1)
    
    if args.days <= 0:
        print("Error: Number of days must be positive")
        sys.exit(1)
    
    print(f"Generating work rotation schedule...")
    print(f"Start date: {start_date}")
    print(f"Duration: {args.days} days")
    print(f"Output directory: {args.output_dir}")
    print()
    
    generator = ScheduleGenerator(start_date)
    
    try:
        # Generate schedules
        general_schedule, individual_schedules = generator.generate_schedule(args.days)
        
        # Save to Excel file
        excel_file = generator.save_to_excel(general_schedule, individual_schedules, args.output_dir)
        
        print("Generación de calendario completada exitosamente!")
        print(f"\nArchivo Excel generado: {excel_file}")
        print("\nHojas incluidas:")
        print("📋 Lista General (Vista general detallada)")
        print("📅 Calendarios mensuales (Formato calendario)")
        print("👤 Cal. Ludy (Calendario individual)")
        print("👤 Cal. Sanye (Calendario individual)")  
        print("👤 Cal. Clari (Calendario individual)")
        print("📊 Lista Ludy (Datos detallados)")
        print("📊 Lista Sanye (Datos detallados)")
        print("📊 Lista Clari (Datos detallados)")
        print("\n🎨 Leyenda de colores:")
        print("🔵 Azul = Turno Mañana")
        print("🟠 Naranja = Turno Tarde") 
        print("🟢 Verde = Descanso")
        
        print("\nResumen del Calendario (primeros 7 días):")
        print("-" * 80)
        spanish_weekdays = {
            'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
            'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
        }
        
        for day_schedule in general_schedule[:7]:
            print(f"{day_schedule['Fecha']} ({day_schedule['Día']}): ", end="")
            
            working = []
            resting = []
            for employee, data in day_schedule.items():
                if employee not in ['Fecha', 'Día']:  # Skip date fields
                    if data['status'] == 'Trabajando':
                        working.append(f"{employee} ({data['shift']})")
                    else:
                        resting.append(f"{employee} (Descanso)")
            
            all_status = working + resting
            print(" | ".join(all_status))
        
    except Exception as e:
        print(f"Error generating schedule: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
