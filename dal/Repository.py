from sqlalchemy.orm import Session,sessionmaker
from  sqlalchemy import create_engine
from be.Setting import Setting

conn=Setting().GetConnectionString()
engine=create_engine(str(conn))
Session=sessionmaker(bind=engine)
session=Session()

class Repository():
    def Add(self,obj):
        try:
            session.add(obj)
            session.commit()
            return True
        except ConnectionError as  e:
            return False

    def Read(self,obj):
        return session.query(obj).all()

    def Update(self,obj,id):
        newObj=self.ReadById(obj,id)
        newObj=obj
        session.commit()

    def Delete(self,obj):
        try:
            session.delete(obj)
            session.commit()
            return True
        except:
            return False
    def ReadById(self,obj,id):
        return session.query(obj).filter(obj.hs_id==id).first()

