from datetime import date
from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import current_user, login_required
from .models import User, ShitPost, Comment
from .forms import ShitPostForm, CommentForm
from . import db


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    shit_form = ShitPostForm()
    posts = db.session.execute(db.select(ShitPost)).scalars().all().__reversed__()
    if request.method == 'POST':
        new_post = ShitPost(
            post=shit_form.post.data,
            user=current_user
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('views.home'))
    return render_template("index.html", shit_posts=posts, shit_form=shit_form)

@views.route('/profile/<string:username>')
@login_required
def profile(username):
    user = db.session.execute(db.select(User).where(User.username == username)).scalar()
    posts = db.session.execute(db.select(ShitPost).where(ShitPost.user_id == user.id)).scalars().all().__reversed__()
    return render_template("profile.html", user_posts=posts, user=username)
    
