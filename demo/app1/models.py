from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    #属性text是一个CharField——由字符或文本组成的数据
    #需要存储少量的文本，如名称、标题或城市时
    text = models.CharField(max_length=200)
    #属性date_added是一个DateTimeField——记录日期和时间的数据
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关耨个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50]+"..."
