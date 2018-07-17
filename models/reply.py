import time
from sqlalchemy import Column, String, Integer
from models import Models
import bleach


allow_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em','i',
              'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p']
Base = Models.Base
engine = Models.engine
Session = Models.Session


class Reply(Base):
    __tablename__ = 'reply'
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, nullable=False)
    content = Column(String(32), nullable=False)
    create_time = Column(String(16), nullable=False)
    page_id = Column(Integer)

    @classmethod
    def get(cls, page_id):
        s = Session()
        return s.query(cls).filter_by(page_id=page_id).all()

    @classmethod
    def comment(cls, form, **kwargs):
        userid = kwargs.get('userid')
        content = form.get('content', '')
        content = bleach.clean(content,allow_tags)
        print(content)
        page_id = form.get('page_id', '')
        create_time = time.strftime("%y-%m-%d", time.localtime(time.time()))
        reg = cls(
            userid=userid,
            content=content,
            page_id=page_id,
            create_time=create_time,
        )
        s = Session()
        s.add(reg)
        s.commit()
        s.close()

    @classmethod
    def user(cls, userid):
        from user import User
        u = User.get(userid=userid)
        return u


if __name__ == '__main__':
    """

    Reply.comment(dict(
        userid=1,
        content='wocao2',
        page_id=1,
    ))
    """
    print(Reply.user(userid=1))



    #print(Reply.get(1).userid)

    #Models.init()


