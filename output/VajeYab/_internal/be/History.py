from idlelib.history import History

from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base
from be.Setting import Setting
from sqlalchemy import create_engine, Column, Integer, String, NVARCHAR

conn=Setting().GetConnectionString()
# print(conn)
engine = create_engine(conn)
# engine = create_engine('mssql+pyodbc://./vajeYab?driver=ODBC+Driver+17+for+SQL+Server')
Base = declarative_base()

class History(Base):
    __tablename__="History"
    hs_id=Column(Integer,primary_key=True)
    hs_Title=Column(NVARCHAR)
    # hs_En=Column(NVARCHAR)
    hs_Text=Column(NVARCHAR)

    def __init__(self,hs_Title="",hs_Text=""):
        self.hs_Title=hs_Title
        # self.hs_En=hs_En
        self.hs_Text=hs_Text


try:
    Base.metadata.create_all(engine)

    # شما باید اول نمونه بگیرید بعد بیاید نرم افزار رواجرا کنید جدول ها هم ساخته میشه

except Exception as e:
     print(" اتصال ندارید" )

