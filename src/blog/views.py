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


class PostView(MethodView):
    def get(self, id):
        note = Note.select().where(Note.id == id)
        print(note)
        return render_template(
            'detail_post.html',
            context={
                'note': note[0]
            }
        )


bp.add_url_rule(
    '/',
    view_func=BlogView.as_view(
        name='blog_page',
    ),
)

bp.add_url_rule(
    '/post/<int:id>',
    view_func=PostView.as_view(
        name='post_page',
    ),
)
