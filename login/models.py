from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    #CharField:字符串类型，必须接受max_length参数，默认表单标签是inputtext
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    #EmailField:邮箱类型，默认max_length最大长度254位，可以使用DJango内置的EmailValidator进行邮箱地址合法性验证。
    email = models.EmailField(unique=True)
    #choices:用于页面上的选择框标签，需要先提供一个二维的二元元组，第一个元素表示存在数据库内真实的值，第二个表示页面上显示的具体内容
    sex = models.CharField(max_length=32, choices=gender, default="男")
    #DateTimeField:日期时间类型。Python的datetime.datetime的实例。与DateField相比就是多了小时、分和秒的显示，其它都一样。
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"

