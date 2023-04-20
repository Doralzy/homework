# 编写学员实体类，对应属性包含：学号、姓名、性别。
# 编写学员名单管理类，实现删除学员方法、查询学员方法。

class Student:
    def __init__(self, sid, name, gender):
        self.sid = sid
        self.name = name
        self.gender = gender

    def msg(self):
        # li = []
        dc = {
            "id": self.sid,
            "name": self.name,
            "gender": self.gender
        }
        # li.append(dc)
        return dc


class StudentList:
    def __init__(self, student_list):
        self.s_list = student_list
        print(self.s_list)

    def get(self, student_id):
        """
        根据 student_id 查询信息
        """
        li = self.s_list
        for i in range(0, len(li)):
            data = li[i]
            # print(type(data))
            sid = data.get('id')
            if sid == student_id:
                content = li[i]
                break
            else:
                content = "查无此人"
        return print(content)
        # return content  # 为什么不能打印结果


    def delete(self, student_id):
        """
        根据 student_id 删除信息
        """
        li = self.s_list
        new_list = []
        id_list = []
        for i in range(0, len(li)):
            sid = li[i]['id']
            id_list.append(sid)
        if student_id in id_list:
            for i in range(0, len(li)):
                sid = li[i]['id']
                if sid == student_id:
                    del_info = li[i]
                    continue
                else:
                    new_list.append(li[i])
            return print(f"删除信息:{str(del_info)}; 最终信息:{str(new_list)}")
        else:
            return print("无此信息")





if __name__ == '__main__':
    # 入参自己定义
    s1 = Student(1, "小明", "男")
    s2 = Student(2, "小红", "女")
    s3 = Student(3, "小芳", "女")
    info_s1 = Student.msg(s1)
    print(info_s1)
    # 初始化一个成员名单
    s_list = StudentList([Student.msg(s1), Student.msg(s2), Student.msg(s3)])
    # 实现get()方法
    s_list.get(2)
    # 实现delete
    s_list.delete(2)