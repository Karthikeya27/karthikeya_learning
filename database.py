from sqlalchemy import create_engine,text
import os
from sqlalchemy.exc import SQLAlchemyError

connection_string = os.environ["database_connection"]


engine = create_engine(connection_string, echo=True)
"""
def test_data(person):
  with engine.connect() as connection:
    string = text("insert into Persons(PersonID, LastName, FirstName, Address, City) values(:PersonID, :LastName, :FirstName, :Address, :City)")
    
    connection.execute(statement= string,
                     parameters=dict(PersonID = person["PersonID"],
                      LastName = person["LastName"],
                      FirstName = person["FirstName"],
                      Address = person["Address"],
                      City = person["City"]))
"""

                                      
def load_jobs_from_db():
   with engine.connect() as connection:
    result = connection.execute(text("select * from jobs"))
    jobs=[]
    for row in result.all():
       jobs.append(row._mapping)
    return(jobs)


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text("SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


def add_data_into_db(job_id, application_details):
    with engine.connect() as conn:
        data = text("insert into application(id, name, email, education) values(:id, :name, :email, :education)")
        params = {
            "id": job_id,
            "name": application_details['name'],
            "email": application_details['email'],
            "education": application_details['education']
        }
        conn.execute(data, params)
        conn.commit()  # Ensure you commit the transaction.
        
  
               
              
                                          


  
