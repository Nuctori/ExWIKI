from sqlalchemy import Column, String, Integer
import time
from models import *
from models.user import User

Base = Models.Base
engine = Models.engine
Session = Models.Session


# 定义User对象:
class Page(Base):

    __tablename__ = 'pages'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=False)
    title = Column(String(48), nullable=False)
    content = Column(String(32), nullable=False)
    create_time = Column(String(16), nullable=False)
    last_time = Column(String(16), nullable=False)
    forum = Column(String(256))

    @classmethod
    def publish(cls, form):
        userid = form.get('userid', '')
        title = form.get('title', '')
        content = form.get('content', '')
        forum = form.get('forum', '')
        ct = time.strftime("%y-%m-%d", time.localtime(time.time()))
        lt = ct
        reg = cls(userid=userid,
                  title=title,
                  content=content,
                  create_time=ct,
                  last_time=lt,
                  forum=forum,
                  )
        s = Session()
        s.add(reg)
        s.commit()
        s.close()

    @classmethod
    def get_all(cls):
        s = Session()
        return s.query(cls).all()

    @classmethod
    def get_byid(cls, pageid):
        s = Session()
        return s.query(cls).filter_by(id=pageid).first()
        

    @classmethod
    def get_byforum(cls, forum):
        s = Session()
        return s.query(cls).filter_by(forum=forum).all()

    @classmethod
    def get_bytitle(cls, title):
        s = Session()
        return s.query(cls).filter_by(title=title).first()

    @classmethod
    def update_bytitle(cls, title,content):
        s = Session()
        page = s.query(cls).filter_by(title=title).first()
        page.content = content
        s.commit()

    @classmethod
    def del_bytitle(cls, title):
        s = Session()
        page = s.query(cls).filter_by(title=title).first()
        s.delete(page)
        s.commit()



    @classmethod
    def user(cls, userid):
        u = User.get(userid=userid)
        return u





    @classmethod
    def setinfo(cls, ):
        ...
if __name__ == '__main__':
    # Page.publish(
    #        dict(author='author',
    #             title='title',
    #             content='content',
    #             )
    # )
    #Models.init()
    a = Page.get_byforum("魔界漫游指南")
    print(a.title)

