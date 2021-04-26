import pyodbc
import pandas as pd
server_name = '85.142.157.73,8628'
db_name = 'Dekanat2021'
User = 'saa'
password = '322322'

cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        f"Server={server_name};"
                        f"Database={db_name};"
                        f"uid={User};pwd={password}")
req = f"SELECT SprStudents.Fam, SprStudents.Name, SprStudents.Otch, Sessiya.dateS, SprMarks.mark, SprDisciplines.[Discipline Name] FROM Sessiya INNER JOIN SprStudents ON (Sessiya.StudentId = SprStudents.StudentId) INNER JOIN SprMarks ON Sessiya.id_mark = SprMarks.id_mark INNER JOIN SprDisciplines ON Sessiya.discipline_id = SprDisciplines.discipline_id"

