from flask import Blueprint, render_template
'''
加载日历控件模板文件
'''

cal = Blueprint('cal', __name__)
@cal.route('/calendar')
def calendar():
    return render_template('calendar/index.html')

@cal.route('/day.html')
def tmpls_day():
    return render_template('calendar/tmpls/day.html')
@cal.route('/events-list.html')
def tmpls_events_list():
    return render_template('calendar/tmpls/events-list.html')
@cal.route('/modal.html')
def tmpls_modal():
    return render_template('calendar/tmpls/modal.html')
@cal.route('/month.html')
def tmpls_month():
    return render_template('calendar/tmpls/month.html')
@cal.route('/month-day.html')
def tmpls_month_day():
    return render_template('calendar/tmpls/month-day.html')
@cal.route('/week.html')
def tmpls_week():
    return render_template('calendar/tmpls/week.html')
@cal.route('/week-days.html')
def tmpls_week_days():
    return render_template('calendar/tmpls/week-days.html')
@cal.route('/year.html')
def tmpls_year():
    return render_template('calendar/tmpls/year.html')
@cal.route('/year-month.html')
def tmpls_year_month():
    return render_template('calendar/tmpls/year-month.html')