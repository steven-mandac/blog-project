from datetime import date
from flask import Blueprint, render_template, request, redirect, flash
from flask_login import current_user
from .models import User, ShitPost, Comment
from .forms import ShitPostForm, CommentForm
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    shit_form = ShitPostForm()
    posts = db.session.execute(db.select(ShitPost)).scalars().all()
    if request.method == 'POST':
        new_post = ShitPost(
            post=shit_form.post.data,
            user=current_user
        )
        db.session.add(new_post)
        db.session.commit()
        flash("Shit posted!", category="success")
    return render_template("index.html", shit_posts=posts, shit_form=shit_form)

