"""
编写学员实体类，对应属性包含：学号、姓名、性别。
编写学员名单管理类，实现删除学员方法、查询学员方法。
学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
实现更新学员、添加学员操作。
作业内容
编写学员实体类，对应属性包含：学号、姓名、性别。
编写学员名单管理类，实现删除学员方法、查询学员方法。
学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
实现更新学员、添加学员操作。
"""
from dataclasses import dataclass, asdict, field
from typing import List


@dataclass
class Student:
    sid: int
    name: str
    gender: str
    __score: int = field(default=0)

    @property
    def score(self):
        return self.__score
    
    @score.setter    # 没走到
    def score(self, num):
        if type(num) == int:
            self.__score = num
        else:
            print("修改失败，请规范填写")

# asdict()是否可以放在这里实现一个自动返回字典的内容


class StudentList:
    def __init__(self, student_list: List[Student]):
        self.s_list = student_list

    def get(self, student_id: int):
        """
        根据 student_id 查询信息
        """
        for i in range(0, len(self.s_list)):
            sid = self.s_list[i]['sid']
            if sid == student_id:
                info = self.s_list[i]
                msg = f"查询到信息{info}"
                break
            else:
                msg = "无"
        return print(msg)

    def delete(self, student_id: int):
        """
        根据 student_id 删除信息
        """

        # new 修改原数据
        for i in range(0, len(self.s_list)):
            sid = self.s_list[i]['sid']
            if sid == student_id:
                del_info = self.s_list.pop(i)
                msg = f"已删除成功学院信息：{del_info}， 最终信息{self.s_list}"
                break
            else:
                msg = "请输入正确学员id"
        return print(msg)

    def update(self, student: Student):
        update_sid = student.get('sid')
        for i in range(len(self.s_list)):
            if update_sid == self.s_list[i]['sid']:
                self.s_list[i].update(student)
                msg = f"更新后内容{self.s_list}"
                break
            else:
                msg = "无可更新对象"
        return print(msg)

    def save(self, student: Student):
        new_id = student.get('sid')
        sid_list = [self.s_list[i]['sid'] for i in range(len(self.s_list))]
        if new_id not in sid_list:
            self.s_list.append(student)
            msg = f"已新增学员信息，新增后{self.s_list}"
        else:
            msg = "该学院的id已存在，建议使用更新方法"
        return print(msg)


if __name__ == '__main__':
    # 入参自己定义
    s1 = asdict(Student(1, "小明", "男"))
    s2 = asdict(Student(2, "小红", "女"))
    s3 = asdict(Student(3, "小芳", "女"))
    s4 = Student(99, "小学霸", "女", 120)
    print(s4.score)
    s4.score = "100"
    print("修改分数", s4.score)
    # s1 = (Student(1, "小明", "男", 100))
    # s2 = (Student(2, "小红", "女", -10))
    # s3 = (Student(3, "小芳", "女"))
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现save
    s4 = asdict(Student(6, "小红花", "女生", 100))
    s_list.save(s4)
    # 实现update
    s5 = asdict(Student(3, "小芳fff", "男男男", 85))
    s_list.update(s5)
    # 实现get()方法
    s_list.get(2)
    # 实现delete
    s_list.delete(2)