from flask import Flask, render_template, request, redirect, url_for
from models.page import Page
from models.reply import Reply
import markdown



app = Flask(__name__)


@app.route('/')
def index():
    ms = Page.get_all()
    navs=[]
    for m in ms:
        if m.forum not in navs:
            navs.append(m.forum)
    return render_template('wiki/index.html', ms=ms,navs=navs, markdown=markdown,index=True)

@app.route('/app/editor/',methods=['POST','GET'])
@app.route('/app/editor/<forum>',methods=['POST','GET'])
def editor(forum=None):
    if request.method =='POST':
        if request.form.get('post')=="提交":
            if Page.get_bytitle(forum):
                Page.update_bytitle(forum,request.form.get('content'))
            else:
                form = request.form
                Page.publish(form)
        elif request.form.get('post')=="删除":
            Page.del_bytitle(forum)
        print(request.form)
        return redirect(url_for('forum',forum=request.form.get('title')))
    ms = Page.get_all()
    content = Page.get_bytitle(forum)
    navs=[]
    for m in ms:
        if m.forum not in navs:
            navs.append(m.forum)
    return render_template('wiki/topic.html', ms=ms,content=content,navs=navs)


        
        

@app.route('/forum/<forum>')
def forum(forum):
    ms = Page.get_byforum(forum)
    content = Page.get_bytitle(forum)
    navs=[]
    route='forum'
    for m in ms:
        navs.append(m.title) 
    return render_template('wiki/index.html', ms=ms,navs=navs,content=content, markdown=markdown,route=route)

@app.route('/editor/<forum>')
def editor_forum(forum):
    ms = Page.get_byforum(forum)
    content = Page.get_bytitle(forum)
    navs=[]
    route='editor_forum'
    for m in ms:
        navs.append(m.title) 
    return render_template('wiki/index.html', ms=ms,navs=navs,content=content,
    markdown=markdown,route=route)


'''
@app.route('/bbs')
def bbs():
    ms = Page.get_all()
    return render_template('bbs/index.html', ms=ms)

@app.route('/editor/posting', methods=['POST'])
def posting_page():
    form = request.form
    Page.publish(form)
    return redirect(url_for('index'))


@app.route('/page_posting', methods=['POST'])
def posting_commit():
    form = request.form
    Reply.comment(form, userid='1')
    return redirect(url_for('showpage', page_id=form.get('page_id')))


@app.route('/page/<int:page_id>')
def showpage(page_id):
    page = Page.get_byid(page_id)
    replys = Reply.get(page_id)
    return render_template('bbs/detail.html', id=id, page=page, replys=replys, markdown=markdown)
'''

if __name__ == '__main__':
    app.run(debug=True)
