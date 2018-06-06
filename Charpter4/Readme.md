##Python对象
- 4.1  
用对象模型储存数据，任何类型的值都是一个对象  
    - 对象的3个特性：    
        - 身份: 对任意对象可使用`id()`确认，可以认为是内存地址
        - 类型：对象的类型决定此对象可以保存什么类型的值。`type()`
        - 值：对象表示的数据项    
- 4.2   
标准类型
- 4.3   
其他内建类型
- 4.4   
内部类型
- 4.5   
标准类型操作符 
    - 值的比较  
    - 身份的比较 `is, is not`用来测试两个变量是否指向同一个对象   
    `a = 1
    b=1 id(a)=id(b)`    
    `a = 1.0
    b = 1.0 
    id(a) != id (b)`
此处有关缓存 python3未实验
    - 布尔型
- 4.6 
标准类型内建函数    
    
| 函数 | 功能|    
| -----|---|    
| cmp(obj1,obj2) |根据比较结果返回整型i i<0 obj1<obj2 |
| repr(obj)|返回一个对象的字符串表示|
| str(obj)|返回一个对象可读性好的字符串表示|
|type(obj)|得到一个对象的类型 返回相应的TPYE对象|
- 4.7       


    if isinstance(num, (int, float, complex)):      
        print("a number of type: {}".format(type(num)))     
        print("a number of type: {}".format(type(num).\__name__))
    
   
 
    
 
 
    
- 4.8 类型比较的3种方法
    - 通过types模块的类成员来判断，     
    其实所有python中的类型都是这个types模块中类型的实例。  
    import types   
    `type(x) is types.IntType` # 判断是否int 类型  
    `type(x) is types.InstanceType`  #是否是自定义的实例对象，
    isinstance函数不支持比较这个  
    python3中：  
    `type(x) is int`
    

  
| python2 |	python3 |  
|  --- | --- |
|types.UnicodeType|	str|
|types.StringType |	bytes|
|types.DictType|	dict|
|types.IntType	|int|
|types.LongType|	int|
|types.ListType|	list|
|types.NoneType|	type(None|
|types.BooleanType	|bool|
|types.BufferType	|memoryview|
|types.ClassType	|type|
|types.ComplexType	|complex|
|types.EllipsisType|	type(Ellipsis)|
|types.FloatType|	float|
|types.ObjectType|	object|
|types.NotImplementedType	|type(NotImplemented)|
|types.SliceType	|slice|
|types.TupleType	|tuple|
|types.TypeType	|type|
|types.XRangeType	|range|



- 通过已知类型比较，因为python中所有相同类型的对象他们所引用的类型都是同一个，所以可以通过如下的方式对比：  
    `type(x) == type('a')` 此种方法是值的比较，需要多求一次值。
- 使用内建函数isinstence(obj, type)  
`isinstance(obj, (int, str, list))` 
    
-  工厂函数 int() type() list()等 他们看起来是函数实际是类
-标准类型的分类方式
    - 储存模型  
    能存多少，是否能存不同类型的对象  
    数值，字符串  
    列表，元组，字典  
    - 更新模型  
    可变：列表、字典    
    不可变：数字、字符串、元组（新赋值则旧的数字和字符被丢弃，产生新的对象，既ID不同）  
    - 访问模型  
        - 直接访问： 数字
        - 顺序访问（切片）：列表，元组，字符串。
        - 映射访问： 字典。
        
 练习未做完
 -