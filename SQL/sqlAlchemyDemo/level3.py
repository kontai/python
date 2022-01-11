import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

##SQLAlchemy ORM

# 物件
# 進行連結
print('我在最外面')
conn = sa.create_engine('sqlite:///zoo.db')

# sqlAlchemy ORM
Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damage = sa.Column('damage', sa.Float)

    def __init__(self, critter, count, damage):
        self.critter = critter
        self.count = count
        self.damage = damage

    def __repr__(self):
        return "<Zoo({},{},{})>".format(self.critter, self.count, self.damage)


if __name__ == '__main__':
    print('我在main裡面')
    # 建立資料庫
    Base.metadata.create_all(conn)

    # 插入資料
    first = Zoo('duck', 10, 0.0)
    second = Zoo('bear', 2, 1000.0)
    third = Zoo('weasel', 1, 2000.0)

    #建立對話
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=conn)
    session = Session()

    session.commit()
    session.close()