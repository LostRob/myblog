from django.db import models

class Category(models.Model):
    """分类"""
    name = models.CharField(max_length=100)
    # 为了更好的查看模型数据，可以模型类添加__str__魔法方法
    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Blog(models.Model):
    """文章"""
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True,null=True)
    modified_time = models.DateTimeField(auto_now=True,null=True)
    excerpt = models.CharField(max_length=200, blank=True)  # 文章摘要，可为空
    category = models.ForeignKey(Category, on_delete=True,blank=True)  # ForeignKey表示1对多（多个post对应1个category）
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)  # 阅读量
    # orderalg = models.PositiveIntegerField(default=0)  # 加权分数
    author = models.ForeignKey('login.User',on_delete=None,default=1)

    def __str__(self):
        return self.title

    # 增加阅读量
    def add_views(self):
        self.views += 1
        self.save()