from flask import Blueprint, render_template, url_for, request, session

admin_controller = Blueprint("admin_controller", __name__, template_folder="templates")

@admin_controller.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        posts = ''
        for elem in request.form:
            posts += elem + '=>' + request.form[elem]+'<br> '
        return posts
    else:
        return render_template("views/admin/login.html")
