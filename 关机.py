with open("计划关机.bat","w",encoding="UTF-8") as f:
    long="shutdown -s -t "
    time=int(input("输入时间:"))
    time=str(time)
    long=f"{long}{time}"
    f.write(long)
    print(long)
    print("操作已完成...")
