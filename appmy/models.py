from django.db import models
import re
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64, verbose_name= '사용자명')
    password = models.CharField(max_length=64, verbose_name= '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name= '등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'appmy_user'

def cleanText(input_username):
    text = re.sub('[!@#$%^&*()_+-=!/\<>,.{}?"]', '', input_username)
    return text

# if __name__ == "__main__":
#     login_username = 'roo@#!!@%$#^%#^#$&$#&$#^@#%><t?:"'
#     print(cleanText(login_username))