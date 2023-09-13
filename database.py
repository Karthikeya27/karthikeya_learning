from sqlalchemy import create_engine,text
import os
connection_string = os.environ["database_connection"]


engine = create_engine(connection_string, echo=True)

def load_jobs_from_db():
   with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
       jobs.append(row._mapping)
    return(jobs)









  