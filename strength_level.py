# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:06:50 2019

终止循环
存储文件
读取文件
定义工具class

@author: yuan
"""
class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0
    
    
    def process_password(self):
        if len(self.password) >= 8:
             self.strength_level += 1
        else:
             print('密码长度要大于8位')
          #是否含有数字
        if self.check_number_exist():
             self.strength_level += 1
        else:
             print('密码要含有数字')
           #是否含有字母  
            
# =============================================================================
#         if self.check_letter_exist():
#             self.strength_level += 1
#         else:
#              print('密码要含有字母')
#              
# =============================================================================
        if self.check_islower_exist():
            self.strength_level += 1
        else:
            print('密码需要有小写字母')
        
        if self.check_isupper_exist():
            self.strength_level += 1
        else:
            print('密码需要有大写字母')
             
    def check_number_exist(self):
    
        has_number = False
        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        has_letter = False
        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter 
    
    def check_islower_exist(self):
        has_lower = False
        for c in self.password:
            if c.islower():
                has_lower = True
                break
        return has_lower 
    def check_isupper_exist(self):
        has_upper = False
        for c in self.password:
            if c.isupper():
                has_upper = True
                break
        return has_upper
    
class FileTool:
    def __init__(self, filepath):
        self.filepath = filepath
    def write_to_file(self, line):
        f = open(self, line)
        f.write(line)
        f.close()
        
        

def main():
    

     try_times = 5
     
     while try_times > 0:
     
         password = input('请输入密码：')
        
         password_tool = PasswordTool(password)
         password_tool.process_password()
             
# =============================================================================
#          f = open('password.txt', 'w')
#          f.write('密码：{}, 强度：{}\n'.format(password, password_tool.strength_level))
#          f.close()
# =============================================================================
         f = open('password2.0.txt', 'a')
         f.write('密码：{}, 强度：{}\n'.format(password, password_tool.strength_level))
         f.close()
          
         if password_tool.strength_level == 4:
             print('密码强度合格')           
             break
         else:
             print('建议修改密码')
             try_times -= 1
         
         print()
             
     if try_times <= 0:
         print('密码输入错误次数超过5次，请稍后重试')
       
    
if __name__ == '__main__':
    main()
