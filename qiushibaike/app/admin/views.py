from flask import render_template, session, redirect, url_for
from . import admin

@admin.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin/welcome.html')