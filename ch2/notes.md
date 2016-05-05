# ch2 Collaborative Filtering

update: 2016-5-5

---
**新技能Get**

	- sort\sorted
	- +=
	- dict
	- lambada
	- map

---

##1. for循环中‘+=’的用法

'+='是常用的缩写法，比如：

	i = i +5	等价于:	i += 5	

以Manhattan算法为例：

	def manhattan(rating1, rating2):
		distance = 0
		commeRating = False	#用于识别rating1、rating2是否有相同项

		for key in rating1:
			if key in rating2:
				distance += abs(rating1[key]-rating2[key])
				commeRating = True	#如果有一个相同项，就将标志字段置为True
			else:
				continue

		if commeRating:
			return distance
		else:
			return -1	#表示没有共同项

如果将:

>distance += abs(rating1[key]-rating2[key])

替换为：

>distance = abs(rating1[key]-rating2[key])
>
>distance += distance

则输出结果会错误，且不是一个定值！

原因是：
> distance = abs(rating1[key]-rating2[key])
> 是赋值语句，使用它会**直接抹掉distance之前存储的值**。
> distance += disatance则会将新的distance得值做加法。

>而我们需要的，是将新计算的abs(rating1[key]-rating2[key])值和distance原值相加。

##2. Map和匿名函数lambda

>感谢知乎@涛吴的解答。原文链接：https://www.zhihu.com/question/20125256/answer/14058285

### 2.1 Map

>map() 函数，它可以将一个函数映射到一个可枚举类型上面。

案例:

	map(f, a)	#将函数 f 依次套用在 a 的每一个元素上面

现在用 lambda 表达式来替换 f，就变成：

	map( lambda x : x + 1, [1, 2, 3] )

会不会觉得现在很一目了然了？尤其是类比

	a = [1, 2, 3]
	r = []
	for each in a:
    	r.append(each+1)

### 2.2 匿名函数lambda
> 简单来说，编程中提到的 lambda 表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。

案例：

	lambda x: x*x

等价于：

	def sq(x):
    	return x * x

>进一步讲，**匿名函数本质上就是一个函数，它所抽象出来的东西是一组运算。**这是什么意思呢？类比
>
	a = [1, 2, 3]
和

>
	f = lambda x : x + 1
你会发现，等号右边的东西完全可以脱离等号左边的东西而存在，等号左边的名字只是右边之实体的标识符。如果你能习惯 [1, 2, 3] 单独存在，那么 lambda x : x + 1 也能单独存在其实也就不难理解了，它的意义就是给「某个数加一」这一运算本身。


练习题：
	t = [('a', 3), ('b',2), ('c',1)]

	print(t)
	print(sorted(t, key = lambda tTuple: tTuple[1], reverse = False))	#正序排列
