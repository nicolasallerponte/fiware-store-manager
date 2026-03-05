from flask import Blueprint, render_template, abort
from app.models import Employee
from flask_babel import _

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/employees')
def index():
    """List all employees"""
    employees = Employee.query.all()
    return render_template('employees/index.html', employees=employees)

@employees_bp.route('/employees/<string:employee_id>')
def detail(employee_id):
    """Employee detail view"""
    employee = Employee.query.get_or_404(employee_id)
    return render_template('employees/detail.html', employee=employee)
