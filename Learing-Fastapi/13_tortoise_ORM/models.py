from tortoise.models import Model
from tortoise import fields


"""
学生选课系统的ORM模型
"""


class Student(Model):
    """
    学生模型
    与 Course 是多对多关系（通过StudentCourse）
    与 Department 是多对一关系
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50, description="学生姓名")
    student_id = fields.CharField(max_length=20, unique=True, description="学号")
    enrollment_date = fields.DateField(description="入学日期")
    # 多对一关系，一个学生属于一个院系，一个院系有多个学生
    department: fields.ForeignKeyRelation['Department'] = fields.ForeignKeyField(
        'models.Department',
        related_name='students',
        description='所属院系'
    )
    # 多对多关系，一个学生可以选择多门课，一门课可以有多个学生选
    courses : fields.ManyToManyRelation['Course'] = fields.ManyToManyField(
        "models.Course",
        through= 'student_course',
        related_name="students",
        description = "所选课程"
    )

class Department(Model):
    """
    院系模型
    与 学生 是一对多关系
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, unique=True, description="院系名称")
    code = fields.CharField(max_length=20, unique=True, description='院系代码')
    established_date = fields.DateField(description='成立日期')
    # 一对多关系， 一个院系有多个学生
    # 声明反向关系模型，通过 department.students 可以获取属于该院系的所有学生
    students: fields.ReverseRelation["Student"]
    ''' 如何使用：
    # 获取某个院系的所有学生
cs_dept = await Department.get(name="计算机科学系")
students = await cs_dept.students.all()  # 通过反向关系查询

for student in students:
    print(student.name)
    '''

    class Meta:  # 配置模型的数据库表信息
        tabel = 'departments'  # table：指定这个模型对应的数据库表名（如果不设置，默认用类名的小写形式）
        tabel_description = '院系信息表'  # table_description：表的描述信息（比如注释，方便数据库维护）


class Course(Model):
    """
    课程模型
    与Teacher是多对一关系
    与Student是多对多关系 (通过StudentCourse)
    """
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, description="课程名称")
    code = fields.CharField(max_length=20, unique=True, description='课程代码')
    credit = fields.IntField(description='学分')
    description = fields.TextField(null=True, description='课程描述') # 允许为空
    time = fields.DateField(description="课程时间")
