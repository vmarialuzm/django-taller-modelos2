from django.db import models

# Vamos a crear 4 modelos
# 1. Person
# 2. Student
# 3. Teacher
# 4. ClassRoom

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    born_date = models.DateField()


    class Meta:
        abstract = True

#---------------------------------------------------

class Teacher(Person):
    salary = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0)

    class Meta:
        db_table = "teachers"

class TeacherProxy(Teacher):
    class Meta:
        proxy = True

    def get_bonnus(self):
        return self.salary + self.rating * 100

#---------------------------------------------------

class ClassRoom(models.Model):
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True, default=None)
    name = models.CharField(max_length=2)
    start_time = models.TimeField()

    def __str__(self):
        return self.name + "-" + str(self.start_time)

    class Meta:
        db_table = "classrooms"

#---------------------------------------------------

class Student(Person):
    classroom_id = models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    grade_lab = models.FloatField(default=0.0)
    grade_exam = models.FloatField(default=0.0)
    grade_final = models.FloatField(default=0.0)

    class Meta:
        db_table = "students"


class StudentProxy(Student):
    class Meta:
        ordering = ["-id"]
        proxy = True

    def average(self):
      return self.grade_exam * 0.1 + self.grade_lab * 0.6 + self.grade_final * 0.3


#------------------------Tarea---------------------------

class Evaluacion(models.Model):
    hora_fecha = models.DateTimeField()
    curso = models.CharField(max_length=30)
    evaluador = models.CharField(max_length=50)

    class Meta:
        abstract = True

#---------------------------------------------------

class ExamenFinal(Evaluacion):
    duracion_exam = models.IntegerField()
    num_preguntas = models.IntegerField()
    puntaje_total = models.IntegerField()

    def __str__(self):
        return self.num_preguntas / self.puntaje_total

    class Meta:
        db_table = "examen_final"

#---------------------------------------------------

class Proyecto(Evaluacion):
    tema_proyecto = models.CharField(max_length=100)
    num_grupos = models.IntegerField()

    class Meta:
        db_table = "proyecto"

class ProyectoProxy(Proyecto):
    class Meta:
        ordering = ["tema_proyecto"]
        proxy = True
        
    







    
    