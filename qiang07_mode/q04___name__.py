if __name__ == "__main__":  # 每个模块都有__name__属性, 当值等于__main__时, 表明模块在自身运行, 否则是被引入
    print("innner")
else:
    print("outer")