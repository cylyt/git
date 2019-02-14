# 主程序

1. pygame.init() 初始化
2. screen=pygame.display.set_mode((width,height)) 设置屏幕窗口
3. pygame.display.set_caption("**") 窗口标题
4. 退出程序
5. pygame.display.flip() 刷新屏幕

```bash
for event in pygame.event.get():
    if event.type==pygame.QUIT:
        sys.exit()
```