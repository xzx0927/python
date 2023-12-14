import xlrd
import xlwt

# wb = xlwt.Workbook()
# sh = wb.add_sheet("text")  # 创建一个表sheet1的名字是text
# sh.write(0, 0, 'abc')  # x在第0行0列写入abc
# sh.col(0).width = 256 * 20  # 设置0列的宽度
#
# style = xlwt.XFStyle()  # 创建样式
# font = xlwt.Font()
# font.bold = True  # 加粗
# font.name = "微软雅黑"  # 设置字体样式为微软雅黑
# font.colour_index = 20  # 设置颜色
#
# al = xlwt.Alignment  # 对齐方式
# al.vert = 0x01  # 居中对齐
# al.horz = 0x02  # 水平方向对齐
# style.font = font  # 使用font类型
# style.Alignment = al  # 使用al类型
# sh.write(2, 2, "12345", style)#在2行2列写入12345并使用style

# sh.write_merge(行,合并行数,列,合并列数)#合并单元格

# wb.save('text.xls')  # 创建表文件是text.xls

#读
du=xlrd.open_workbook("text.xls")#打开表格文件
d=du.sheet_by_index(0)#读取文件第一张表
print(d.row_values(2))#打印第2行数据
print(d.col_values(0))#打印第0列数据
print(d.row(0)[0].value)#第0行0列
print(d.col(1)[2].value)#第1行2列
print(d.cell(1,2).value)#第1行第二列