from flask import Blueprint, render_template, request, flash
from com.plugins import csrf
bp_user = Blueprint('user', __name__)
# 剔除csrf保护
csrf.exempt(bp_user)
@bp_user.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        remark = request.form['remark']
        print('Add -> Email is : ', email)
        print('Add -> Remark : ', remark)
        flash('User added successfully!!!')
    return render_template('sys/user/edit.html', title='添加用户')
@bp_user.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        email = request.form['email']
        remark = request.form['remark']
        print('Edit -> Email is : ', email)
        print('Edit -> Remark : ', remark)
        flash('User edited successfully!!!')
    return render_template('sys/user/edit.html', title='编辑用户', email='guoqian.cheng@hyundai-di.com', remark='Remark from background')