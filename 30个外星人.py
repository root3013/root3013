# 定义一个外星人字典，包含颜色和分数
alien = {"color": "green", "point": "5"}
# 创建一个空列表，用于存储外星人
aliens = []
# 初始化计数器变量
i = 1
# 循环30次，向列表中添加外星人
for alien_num in range(0, 30):
    # 每次循环创建一个新的字典对象并添加到列表中
    aliens.append({"color": alien["color"], "point": alien["point"]})
# 遍历所有外星人并打印它们的属性
for alien in aliens[0:]:
    print(f"No.{i} alien {alien}")
    i += 1
# 打印外星人的总数
print(f"total: {len(aliens)} aliens")
# 修改前5个外星人的属性
for alien in aliens[0:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["point"] = "10"
# 再次遍历所有外星人并打印它们的属性
for alien in aliens[0:]:
    print(alien)
