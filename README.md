# daily-fortune

## 每日当季鸡汤

这个的初衷是写一些短句子放到可制定字符的程序界面里提供一些乐子。使用方法举个例子：

从文本库里随机选择一条短句 -> 输入进script -> 在界面上显示成功

一个前置条件是，目标程序界面需要支持scripting。

文本是我随便写的，关于文本的随机选择我有以下想法：

 - 随机模式
 - 当季模式。一些句子可以带上跟日子相关的tag，比如“周五”，“周末”，“春季”，
   每天根据当天符合的tag来挑选，没有tag的不选
 - 随机+当季。以上两种模式的混合，可以加不同的比重。

## 使用举例

### polybar+eww

```
# let yuck trigger a script that contains the following
fortune=`daily_fortune random`
eww="eww -c $HOME/.config/eww/mybar"
$eww update fortune="$fortune"
```

![img](daily_fortune/imgs/fortune.png)
