from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from datetime import datetime, date, timedelta

Base = declarative_base()

class Results(Base):
    __tablename__ = 'multicoin_exchange'

    id = Column(Integer, primary_key=True, nullable=True)
    start_amount = Column(Float, nullable=True)
    from_symbol = Column(String(255), nullable=True)
    to_symbol = Column(String(255), nullable=True)
    rate = Column(Float, nullable=True)
    amount = Column(Float, nullable=True)
    percentage_gain = Column(Float, nullable=True)
    for_symbol= Column(String(255), nullable=True)
    date_time = Column(DateTime, nullable=False)
    from_rate = Column(Float, nullable=True)
    to_rate = Column(Float, nullable=True)
    from_exchange = Column(String(255), nullable=True)
    to_exchange = Column(String(255), nullable=True)


    def __init__(self, id=0, start_amount=None, from_symbol=None,to_symbol=None,rate=None,amount=None,percentage_gain=None,
                 for_symbol=None,date_time=None, from_rate=None, to_rate=None, from_exchange=None, to_exchange=None):
      self.id = id
      self.start_amount = start_amount
      self.from_symbol = from_symbol
      self.to_symbol = to_symbol
      self.rate = rate
      self.amount = amount
      self.percentage_gain = percentage_gain
      self.for_symbol = for_symbol
      self.date_time = date_time
      self.from_rate = from_rate
      self.to_rate = to_rate
      self.from_exchange = from_exchange
      self.to_exchange = to_exchange

    def __repr__(self):
      return '<Results {},{}>'.format(self.from_symbol, self.from_exchange)

connect_string = 'mysql+pymysql://root:mentrandr@localhost/asperegrine' # OK

engine = create_engine(connect_string)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# ######
# 2019-12-12 20:42:24.707105
# Starting with 100 in BLOC
# BLOC to USDT at 0.0013986 = 0.13986 on okex3 for BLOC/USDT
# USDT to BLOC at 1867.289719626169 = 261.15914018691603 on kucoin for BLOC/USDT

time_stamp = '2019-12-12 20:42:24.707105'

id = 8 #increment me! 7
start_amount = 100
from_symbol = 'BLOC'
to_symbol = 'USDT'
rate = 0.0013986
# rate = 0
amount = start_amount * rate
percentage_gain = 0
for_symbol = 'BLOC'
# date_time = '2019-12-12 20:42:24.707105'
date_time = datetime.now()
from_rate = 0 #don't need
to_rate = 0 #don't need
from_exchange = 'okex3'
to_exchange = 'kucoin'


r1 = Results(id, start_amount, from_symbol, to_symbol, rate, amount, percentage_gain, for_symbol, date_time,
             from_rate, to_rate, from_exchange, to_exchange)


try:
    session.add(r1)
    session.commit()
except:
    print('rollback')
    session.rollback()


alldata = session.query(Results).all()
for somedata in alldata:
    print(somedata)

