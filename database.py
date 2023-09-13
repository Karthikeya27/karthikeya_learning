from sqlalchemy import create_engine,text
connection_string = "mysql+mysqlconnector://yhf3lqjz3d3x4j9qt5c0:pscale_pw_FMKMuGsjJ4OF0uwvQ03QuP4MQkE2ztuqGPvAIVvtWB6@aws.connect.psdb.cloud:3306/kittusdatabase"


engine = create_engine(connection_string, echo=True)

def load_jobs_from_db():
   with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
       jobs.append(row._mapping)
    return(jobs)









  