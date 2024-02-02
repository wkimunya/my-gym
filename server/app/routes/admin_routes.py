# app/routes/admin_routes.py

from flask import Blueprint, jsonify
from app.models.admin import Admin
from app.models.member import Member

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/admin/members/<int:member_id>', methods=['GET'])
def get_member_data(member_id):
    admin = Admin.query.first()  # Fetch the admin (you might have multiple admins)
    
    # Verify that the admin has access to the requested member's data
    member = Member.query.get_or_404(member_id)

    # You can fetch other related data, e.g., workout plans
    workout_plans = member.workout_plans

    # Convert the data to JSON and return
    return jsonify({
        'id': member.id,
        'name': member.name,
        'email': member.email,
        'workout_plans': [{'id': plan.id, 'time': plan.time, 'day': plan.day} for plan in workout_plans],
        # Add other member details as needed
    })
