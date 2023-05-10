"""
编写学员实体类，对应属性包含：学号、姓名、性别。
编写学员名单管理类，实现删除学员方法、查询学员方法。
学员实体类添加一个私有属性成绩，要求实现对应的 getter 和 setter。
实现更新学员、添加学员操作。
添加学员时，把学员信息写入文件中；查看学员时，读取文件中学员的信息。
自定义异常类：添加学员传入参数不合理时抛出自定义异常。
创建一个venv 环境，实现环境隔离。
"""
import json
import os.path
from dataclasses import dataclass, field
from typing import List


@dataclass
class Student:
    """
    自己根据题目要求实现
    """
    id: int
    name: str
    gender: str
    __score: int = field(default=60)

    @property
    def set_score(self):
        score = self.__score
        return score

    @set_score.setter
    def set_score(self, num):
        if type(num) == int:
            self.__score = num
        else:
            print("输入正确成绩")


class SaveException(Exception):
    def __init__(self, msg):
        print(f"这是一个异常：{msg}")


class StudentList:
    def __init__(self, student_list: List[Student]):
        self.s_list = student_list

    def get(self, student_id: int):
        """
        根据 student_id 查询信息
        """
        for student in self.s_list:
            if student_id == student.id:
                print(student.__dict__)
                break
        else:
            print("查无此人")

    def delete(self, student_id: int):
        """
        根据 student_id 删除信息
        """
        for item in self.s_list:
            if student_id == item.id:
                self.s_list.remove(item)
                list_new = [item.__dict__ for item in self.s_list]
                print(f"已删除同学{item.__dict__}\n剩余信息{list_new}")
                break
        else:
            print("请输入正确学生id")

    def update(self, student: Student):
        id_list = []
        for item in self.s_list:
            s_id = item.id
            id_list.append(s_id)
            # id_list = [item.id for item in self.s_list]
            if student.id not in id_list:
                msg = "未找到可更新的学员信息，建议使用save方式"
            else:
                item.__dict__.update(student.__dict__)
                msg = f"更新内容{student.__dict__}\n更新后整体结果{[item.__dict__ for item in self.s_list]}"
                break
        print(msg)

    def save(self, student: Student):
        try:
            if type(student.id) != int or student.id == 0:
                raise SaveException("id不合法")
            elif type(student.gender) != str or student.id == '':
                raise SaveException("gender不合法")
            elif type(student.name) != str or student.name == '':
                raise SaveException("name不合法")
        except SaveException as e:
            print("请确保学生信息格式正确: " + str(e))
        else:
            id_list = [item.id for item in self.s_list]
            if student.id not in id_list:
                info_list = []
                if os.path.exists(".\save_data.json"):
                    size = os.path.getsize(".\save_data.json")
                    if size == 0:
                        info_list.append(student.__dict__)
                        with open(".\save_data.json", 'w', encoding="utf-8") as f:
                            json.dump(info_list, f, ensure_ascii=False)
                    else:
                        with open(".\save_data.json", "r+", encoding="utf-8") as f:
                            data = json.load(f)
                            save_id_list = [item['id'] for item in data]
                            if student.id not in save_id_list:
                                data.append(student.__dict__)
                                f.seek(0)
                                f.truncate(0)
                                json.dump(data, f, ensure_ascii=False)
                                print("新增学员信息已保存到文件: save_data.json")
                            else:
                                print(f"保存文件里已存在该学生信息id：{student.id}")
                else:
                    with open(".\save_data.json", 'w', encoding='utf-8') as f:
                        json.dump(info_list.append(student.__dict__), f, ensure_ascii=False)
            else:
                print("初始化学员信息里，已经存在该学生")

    def get_info_by_file(self, student_id: int):
        """
        根据 student_id 读取save文件查询信息
        """
        with open("./save_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            for item in data:
                if item['id'] == student_id:
                    msg = f"学生信息：{item}"
                    break
                else:
                    msg = "读取文件查无此人"
            print(msg)


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1, "Mary", "girl", 90)
    s2 = Student(2, "Jack", "boy", 85)
    s3 = Student(3, "Selina", "girl")
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])

    # 实现update
    s_info = Student(1, "Henry", "boy", 75)
    s_list.update(s_info)

    # 实现delete
    s_list.delete(2)

    # 实现save
    s_info1 = Student(1, "小黑", "boy", 100)
    s_list.save(s_info1)

    # 实现get()方法
    s_list.get(6)
    # 读取json文件 get学员信息
    s_list.get_info_by_file(8)

