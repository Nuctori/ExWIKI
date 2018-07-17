from sqlalchemy import Column, String, Integer
import time
from models import Models

Base = Models.Base
engine = Models.engine
Session = Models.Session


# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'users'
    __table_args__ = {"useexisting": True}
    # 表的结构:
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(32), nullable=False)
    QQnumber = Column(String(16))
    create_time = Column(String(16), nullable=False)
    last_time = Column(String(16), nullable=False)
    rights = Column(String(16), nullable=False)
    user_image = Column(String(1024))

    @classmethod
    def register(cls, form):
        un = form.get('username', '')
        pw = form.get('password', '')
        qq = form.get('QQnumber', '')
        ct = time.strftime("%y-%m-%d", time.localtime(time.time()))
        lt = ct
        rights = 'user'
        reg = cls(username=un,
                  password=pw,
                  QQnumber=qq,
                  create_time=ct,
                  last_time=lt,
                  rights=rights,
                  user_image='',
                  )
        s = Session()
        s.add(reg)
        s.commit()
        s.close()
        print('ok')

    @classmethod
    def get(cls, userid):
        s = Session()
        return s.query(cls).filter_by(id=userid).first()

    @classmethod
    def setinfo(cls):
        ...

"""
    def __repr__(self):
        #return '%s(%r)' % (self.__class__.__name__, self.name)

"""


if __name__ == '__main__':

    """
    User.register(dict(
        username='1234444',
        password='12345',
        QQnumber='110',

    ))
    """

    #Models.init()


