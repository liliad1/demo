import xadmin
from .models import *
from xadmin.views.website import LoginView
from xadmin.views import CommAdminView


class GlobalSetting(CommAdminView):
    # 左上角及浏览器标题
    site_title = '学生信息管理系统'
    # 页脚版权信息
    site_footer = 'Copyright © 2018 宝宝巴士'
    menu_style = 'accordion'


class LoginViewAdmin(LoginView):
    title = '学生信息管理系统'


class GradeAdmin(object):
    list_display = ('grade_name',)


class ClassAdmin(object):
    list_display = ('class_name',)


class SubjectsAdmin(object):
    list_display = ('name', 'score',)


class TeachersAdmin(object):
    list_display = ('name',)


class StudentsAdmin(object):
    list_display = ('name', 'sex', 'age', 'address',)
    style_fields = {'subjects': 'checkbox-inline', }
    search_fields = ('name', 'class_name__class_name', 'subjects__name',)
    list_filter = ('sex',)
    ordering = ('age', 'name',)


xadmin.site.register(CommAdminView, GlobalSetting)
xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(Grade, GradeAdmin)
xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(Subjects, SubjectsAdmin)
xadmin.site.register(Teachers, TeachersAdmin)
xadmin.site.register(Students, StudentsAdmin)
