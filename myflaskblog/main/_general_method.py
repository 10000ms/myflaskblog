# -*- coding: utf-8 -*-
"""
    myflaskblog.main._generalMethod
    ~~~~~~~~~

    通用功能模块.

    :copyright: (c) 2018 by Victor Lai.
    :license: BSD, see LICENSE for more details.
"""
from myflaskblog.models import Article
from myflaskblog.models import User
from myflaskblog.models import Comment
from flask import render_template
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from myflaskblog import db


def page_mode(all_item_len, page_item_len, page=None, each_page_item=10):
    if all_item_len > each_page_item:
        if page_item_len < each_page_item:
            need_pagination = 1
        elif page and int(page)*each_page_item == all_item_len:
            need_pagination = 1
        else:
            need_pagination = 2
    else:
        need_pagination = 0
    return need_pagination


def search(search_model, search_name, pagination_url, template, pagination_page, page):
    if search_model == 'Article':
        search_item = Article.query.filter(Article.title.ilike('%' + search_name + '%'))
    elif search_model == 'User':
        search_item = User.query.filter(User.is_admin != 1, User.username.ilike('%' + search_name + '%'))
    elif search_model == 'Comment':
        search_item = Comment.query.filter(Comment.title.ilike('%' + search_name + '%'))
    pagination = search_item.paginate(pagination_page, per_page=10, error_out=True)
    pagination_items = pagination.items
    need_pagination = page_mode(
        len(search_item.all()),
        len(pagination_items),
        page
    )
    return render_template(
        template,
        items=pagination_items,
        pagination=pagination,
        need_pagination=need_pagination,
        pagination_url=pagination_url
    )


def check_token(token, function_module):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return False
    if function_module == 'confirm':
        fm_name = 'c'
        if User.query.filter_by(id=data.get(fm_name)).first():
            check_user = User.query.filter_by(id=data.get(fm_name)).first()
            if not check_user.confirmed:
                check_user.confirmed = True
                db.session.commit()
                return data.get(fm_name)
            else:
                return False
        else:
            return False
    elif function_module == 'resetpassword':
        fm_name = 'rp'
        if User.query.filter_by(id=data.get(fm_name)).first():
            return data.get(fm_name)
        else:
            return False
