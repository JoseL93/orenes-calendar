from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
import tempfile
from datetime import datetime, date
import calendar
from schedule_generator import ScheduleGenerator

app = Flask(__name__)
app.secret_key = 'calendario_trabajo_secret_key'

@app.route('/')
def index():
    # Get current year and month for defaults
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    # Generate year options (current year - 2 to current year + 5)
    year_options = list(range(current_year - 2, current_year + 6))
    
    # Month names in Spanish
    months = [
        (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
        (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
        (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
    ]
    
    return render_template('index.html', 
                         year_options=year_options,
                         months=months,
                         current_year=current_year,
                         current_month=current_month)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get form data
        selected_month = int(request.form['month'])
        selected_year = int(request.form['year'])
        
        # Validate inputs
        if selected_year < 2020 or selected_year > 2030:
            flash('Por favor selecciona un año entre 2020 y 2030', 'error')
            return redirect(url_for('index'))
        
        if selected_month < 1 or selected_month > 12:
            flash('Por favor selecciona un mes válido', 'error')
            return redirect(url_for('index'))
        
        # Calculate start date (1st day of selected month)
        start_date = date(selected_year, selected_month, 1)
        
        # Calculate number of days in the month
        days_in_month = calendar.monthrange(selected_year, selected_month)[1]
        
        # Create temporary directory for output
        temp_dir = tempfile.mkdtemp()
        
        # Initialize schedule generator
        generator = ScheduleGenerator(start_date)
        
        # Generate schedules
        general_schedule, individual_schedules = generator.generate_schedule(days_in_month)
        
        # Save to Excel file
        excel_file = generator.save_to_excel(general_schedule, individual_schedules, temp_dir)
        
        # Generate month name in Spanish for the filename
        month_names = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        
        month_name = month_names[selected_month]
        download_filename = f"calendario_{month_name}_{selected_year}.xlsx"
        
        return send_file(excel_file, 
                        as_attachment=True, 
                        download_name=download_filename,
                        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    
    except Exception as e:
        flash(f'Error al generar el calendario: {str(e)}', 'error')
        return redirect(url_for('index'))

@app.route('/preview')
def preview():
    try:
        # Get parameters from URL
        selected_month = int(request.args.get('month', datetime.now().month))
        selected_year = int(request.args.get('year', datetime.now().year))
        
        # Calculate start date
        start_date = date(selected_year, selected_month, 1)
        days_in_month = calendar.monthrange(selected_year, selected_month)[1]
        
        # Generate a preview (first 7 days)
        generator = ScheduleGenerator(start_date)
        general_schedule, _ = generator.generate_schedule(min(7, days_in_month))
        
        # Month name in Spanish
        month_names = {
            1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
            5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
            9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
        }
        
        month_name = month_names[selected_month]
        
        return render_template('preview.html',
                             schedule=general_schedule,
                             month_name=month_name,
                             year=selected_year,
                             selected_month=selected_month,
                             selected_year=selected_year)
    
    except Exception as e:
        flash(f'Error al generar la vista previa: {str(e)}', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)