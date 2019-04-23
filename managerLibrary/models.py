from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from users.models import CustomUser


class Course(models.Model):
    FIRST_YEAR = "FIR"
    SECOND_YEAR = "SEC"
    THIRD_YEAR = "THI"
    FOURTH_YEAR = "FOU"
    FIFTH_YEAR = "FIF"
    SIXTH_YEAR = "SIX"
    NINETH_YEAR = "NIN"

    DIVISION_A = "A"
    DIVISON_B = "B"
    DIVISION_C = "C"
    DIVISION_D = "D"
    DIVISION_E = "E"

    MORNING_SHIFT = "MS"
    EVENING_SHIFT = "ES"
    NIGHT_SHIFT = "NS"

    YEAR_IN_SCHOOL_CHOICES = (
        (FIRST_YEAR, 'Primer Año'),
        (SECOND_YEAR, 'Segundo Año'),
        (THIRD_YEAR, 'Tercer Año'),
        (FOURTH_YEAR, 'Cuarto Año'),
        (FIFTH_YEAR, 'Quinto Año'),
        (SIXTH_YEAR, 'Sexto Año'),
        (NINETH_YEAR, 'Septimo Año'),
    )

    DIVISION_IN_SCHOOL_CHOICES = (
        (DIVISION_A, 'Division A'),
        (DIVISON_B, 'Division B'),
        (DIVISION_C, 'Division C'),
        (DIVISION_D, 'Division D'),
        (DIVISION_E, 'Division E'),
    )

    SHIFT_IN_SCHOOL_CHOICES = (
        (MORNING_SHIFT, 'Turno mañana'),
        (EVENING_SHIFT, 'Turno tarde'),
        (NIGHT_SHIFT, 'Turno noche'),
    )

    id_course = models.AutoField(primary_key=True)

    year = models.CharField(
        max_length=3,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
    )

    division = models.CharField(
        max_length=1,
        choices=DIVISION_IN_SCHOOL_CHOICES,
        default=DIVISION_A,
    )

    shift = models.CharField(
        max_length=2,
        choices=SHIFT_IN_SCHOOL_CHOICES,
        default=MORNING_SHIFT,
    )

    class Meta:
        unique_together = ("year", "division", "shift")

    def __str__(self):
        return "%s %s" % (self.year, self.division)


class Subject(models.Model):
    id_subject = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 254)

    def __str__(self):
        return self.name


class Principal(CustomUser):
    first_name = models.CharField(max_length = 50, null = False, blank = False)
    last_name = models.CharField(max_length = 50, null=False, blank=False)

    def __str__(self):
        return "Director: " + self.first_name + " " + self.last_name


class Preceptor(CustomUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return "Preceptor: " + self.first_name + " " + self.last_name


class Professor(CustomUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    subjects = models.ManyToManyField(
        Subject,
        null = True,
        related_name = "subjects")

    def __str__(self):
        return "Profesor: " +  self.first_name + " " + self.last_name


class Student(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(
        max_length = 50,
        blank = False,
        null = False)
    last_name = models.CharField(
        max_length = 50,
        blank = False,
        null = False)
    birthday = models.DateTimeField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Category(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    id = models.AutoField(primary_key = True)
    student = models.ForeignKey(
        Student,
        on_delete = models.CASCADE,
        related_name = "comments")
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name = "comments")
    categories = models.ManyToManyField(
        Category,
        null = True,
        blank = True,
        related_name = "categories")
    description = models.TextField()
    date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return str(self.id)


class Phone(models.Model):
    id = models.AutoField(primary_key = True)
    number = models.CharField(max_length=50, blank = False, null = False)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "phone")

    def __str__(self):
        return self.number

class CourseHistory(models.Model):
    id = models.AutoField(primary_key = True)
    id_course = models.ForeignKey(Course, null = True, on_delete = models.SET_NULL)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name = "courseHistory")

    def __str__(self):
        return str(self.id)

class AcademicHistory(models.Model):
    id = models.AutoField(primary_key = True)
    id_course = models.ForeignKey(Course, null = True, on_delete = models.SET_NULL)
    subject = models.ForeignKey(Subject, null = True, on_delete = models.SET_NULL)
    cycle = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Grades(models.Model):
    GRADE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
    )

    id = models.AutoField(primary_key=True)
    professor = models.ForeignKey(
        Professor,
        null = True,
        on_delete = models.SET_NULL)
    student = models.ForeignKey(
        Student,
        null = True,
        on_delete = models.SET_NULL)
    subject = models.ForeignKey(
        Subject,
        null = True,
        on_delete = models.SET_NULL)
    grade = models.CharField(
        max_length = 2,
        choices = GRADE_CHOICES,
        default = "0",
    )

    def __str__(self):
        return self.grade

class Presence(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(default = timezone.now())
    student = models.OneToOneField(
        Student,
        null = True,
        on_delete = models.SET_NULL)
    preceptor = models.OneToOneField(
        Preceptor,
        null = True,
        on_delete = models.SET_NULL)
    presence = models.NullBooleanField()

    def __str__(self):
        return "%s %s %s" % (self.date, self.student, self.presence)