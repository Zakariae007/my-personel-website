from models import Experience
from database import connect_db

result_set = connect_db()
Experiences = result_set.Experiences