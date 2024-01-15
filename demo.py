import pandas as pd

# 读取Excel文件
excel_file = '202401.xls'  # 替换为你的Excel文件路径
df = pd.read_excel(excel_file)

# 创建一个新的ExcelWriter对象，以在新文件中写入数据
writer = pd.ExcelWriter('new_202401.xls', engine='openpyxl')  # 替换为你想要的新文件名

# 根据序号将数据分组
groups = df.groupby('序号')

# 将每个分组的数据写入新的Excel文件中的单独工作表
for name, group in groups:
    group.to_excel(writer, sheet_name=f'{name}', index=False)

# 保存Excel文件
writer._save()
