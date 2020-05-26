## 配置

pysa有两种类型的配置文件：

- taint.config：定义了Sources, Sinks, Features, Rules，json格式，全局只有一个
- *.pysa：使用taint.config文件中定义的Sources, Sinks, Features, Rules去标注代码的stub文件，可以有多个

这两类配置文件存放于.pyre_configuration文件中taint_models_path定义的目录下。
任何在这个目录下的.pysa文件都会被pysa解析。

### Sources

污染数据源，在taint.config文件中定义如下

```
sources: [
    {
        name: "Cookies",
        comment: "used to annotate cookie sources"
    },
]
```
