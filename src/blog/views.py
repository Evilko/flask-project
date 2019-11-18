from flask import Blueprint, render_template
from flask.views import MethodView
from src.blog.models import Note

bp = Blueprint('blog', __name__, template_folder='templates')


class BlogView(MethodView):
    def get(self):
        notes = Note.select()
        return render_template(
            'blog_page.html',
            context={
                'notes': notes
            }
        )


bp.add_url_rule(
    '/',
    view_func=BlogView.as_view(
        name='blog_page',
    ),
)
