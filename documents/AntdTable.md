**columns：** *list*型，必填，无默认值

　　用于*配置表格字段信息*的必要参数，元素为单个或多个字典，每个字典对应一个独立字段的相关信息，每个字典的**键值对**有：

- title：必填，*string*型，用于设置该字段对应列显示的字段名

- dataIndex：必填，*string*型，相当于此字段的id，需在所有字段中保持唯一性

- width：可选，*int*或*string*型，用于设置该字段对应列的显示宽度，其中：

  - 当传入*int*型时，代表像素宽度，如`200`即代表200px

  - 当传入*string*型时，接受合法的`css`宽度值，如`'20%'`、`100px`、`'10rem'`等

  - **注意！**，当表格内各个字段的宽度设定之和超出表格整体宽度，且未设置`maxWeight`开启水平方向滚动条时，原有设置的宽度值会与实际不符

- align：可选，*string*型，设置列文字对齐方式，可选项有`'left'`（左对齐）、`'center'`（居中）、`'right'`（右对齐）

- editable：可选，*bool*型，设置对应列单元格数据是否支持*编辑*，默认为`False`即不可编辑

- fixed：可选，*string*型，用于设置对应列的冻结固定倚靠方式，可选项有`'left'`（靠左）、`'right'`（靠右）

- renderOptions：可选，*dict*型，用于设置对应列所有单元格的*再渲染模式*，其中：

  - renderType：*string*型，用于设置以何种方式进行*再渲染*，可选项有`'link'`（超链接）、`'ellipsis'`（超长内容省略模式）、`'mini-line'`（迷你折线图）、`'mini-bar'`（迷你柱状图）、`'mini-progress'`（迷你进度条）、`'mini-area'`（迷你面积图）、`'tags'`（标签模式）、`'button'`（按钮模式）、`'copyable'`（可复制模式）、`mini-ring-progress`（迷你环形进度条模式）、`'status-badge'`（状态徽标模式）、`'image'`（图片模式）、`'custom-format'`（自定义格式化模式）、`'ellipsis-copyable'`（可复制省略模式）、`'corner-mark'`（角标模式），其中*超链接模式*、各种*迷你图模式*、*标签模式*、*按钮模式*、*状态徽标模式*、*图片模式*、*角标模式*均需要数据输入的格式满足要求，具体要求见下文中`data`参数说明部分

  - renderLinkText：可选，*string*型，用于在`renderType`设置为`'link'`时，指定超链接显示的文字内容，默认为`'链接🔗'`

  - renderButtonPopConfirmProps：可选，*dict*型，用于在`renderType`设置为`'button'`，且需要以*点击按钮弹出气泡确认卡片进一步确认*的形式进行功能渲染时设置使用，可用的键有：

    - title：*str*型，用于设置气泡确认卡片的*标题内容*
- okText：*str*型，用于设置气泡确认卡片*确认按钮*的文字内容
    - cancelText：*str*型，用于设置气泡确认卡片*取消按钮*的文字内容
- tooltipCustomContent：可选，*string*型，用于在`renderType`设置为`'mini-line'`、`'mini-area'`或`'mini-bar'`时，传入字符串形式的`javascript`箭头函数来自定义每个`tooltip`的内容及样式，具体使用参考本页对应示例

**data：** *list*型，必填，无默认值

　　用于配合`columns`参数，定义每一行数据记录，元素为单个或多个字典，每个字典内的键值对都对应当前行记录下指定字段的值（其中键值对`key`用于为每行数据赋值*唯一*的id信息，若未传入，会默认补上从0开始依次递增1的序列作为id），譬如下面的例子：

```py
data = [
    {
        'key': '1',
        '字段1': 1,
        '字段2': 2,
        '字段3': 3
    },
    {
        'key': '2',
        '字段1': 1,
        '字段2': 2,
        '字段3': 3
    }
]
```

- 某些再渲染模式下，`data`字段特殊输入格式要求说明
  
  - link模式
    
    超链接模式下，接受的数据输入格式为*dict*型，可用键有：
    
    - href：*str*型，用于设置*链接url地址*
    - target：*str*型，用于设置*跳转行为target属性*，默认为`'_blank'`
    - disabled：*bool*型，设置是否*禁用链接*，默认为`False`
    - content：*str*型，用于单独设置当前记录单元格要显示的超链接文字内容
    
  - mini-line模式
    
    迷你折线图模式下，接受的数据输入格式为*list*型，传入按顺序的折线各点的y值
  
  - mini-bar模式
    
    同迷你折线图模式输入格式，传入按顺序的各柱体高度值
  
  - mini-progress模式
    
    迷你进度条模式下，接受的数据输入格式为*float*型，且值应当在0~1之间，代表百分比进度
  
  - mini-ring-progress模式
  
    迷你环形进度条模式下，接受的数据输入格式为*float*型，且值应当在0~1之间，代表百分比进度
  
  - mini-area模式
    
    同迷你折线图模式输入格式，传入按顺序的面积图上折线各点的y值
  
  - tags模式
    
    标签模式下，接受的数据输入格式为*list*型，可传入若干个由*dict*定义的单个标签信息，其中可用的键有：
    
    - tag：*str*型，用于设置对应标签的*文字内容*
  
  - color：*str*型，用于设置对应*标签的色彩*，详见`AntdTag`的`color`参数说明
  
  - button模式
    
    按钮模式下，接受的数据输入格式为*dict*或*list*型，当输入为*dict*时，代表单按钮模式，可用的键有：
    
    - content：*str*型，用于设置按钮中的*文字内容*
  
  - type：*str*型，同`AntdButton`中的`type`参数
  
  - danger：*bool*型，同`AntdButton`中的`danger`参数
  
  - disabled：*bool*型，同`AntdButton`中的`disabled`参数
  
  - style：*dict*型，同`AntdButton`的`style`参数
    
    亦可输入由多个*dict*组成的列表，来渲染*多个按钮*，以实现更为复杂的功能
    
  - status-badge模式
  
    状态徽标模式下，接受的数据输入格式为*dict*，可用的键有：
  
    - status：*str*型，用于*指定徽标的模式*，可选的有`'success'`、` 'processing'`、` 'default'`、` 'error'`及`'warning'`
    - text：*str*型，用于*设置状态徽标的后置文字内容*
  
  - image模式
  
    图片模式下，接受的数据输入格式为*dict*，可用的键有：
  
    - src：*str*型，用于*设置图片资源的地址*
    - height：*str*或*int*型，用于*设置图片的高度*
    - preview：*bool*型，用于*设置是允许交互式预览图片*，默认为`True`
    
  - corner-mark模式
  
    角标模式下，接受的数据输入格式为*dict*型，可用的键有：
  
    - placement：*str*型，用于设置角标的方位，可选的有`'top-left'`、`'top-right'`、`'bottom-left'`和`'bottom-right'`
    - color：*str*型，默认为`'rgb(24, 144, 255)'`，用于设置角标的颜色
    - content：*str*型，用于设置单元格内容
    - offsetX：*int*型，用于调整角标水平方向像素偏移量
    - offsetY：*int*型，用于调整角标竖直方向像素偏移量
    - hide：*bool*型，默认为`False`，用于设置是否隐藏当前单元格的角标

**miniChartAnimation：** *bool*型，默认为`false`

　　用于*设置是否为表格中的几种迷你图模式单元格开启初始渲染动画效果*

**miniChartHeight：** *int*型，默认为`30`

　　用于*手动设置表格中所有迷你图模式单元格中迷你图的像素高度*

**summaryRowContents：** *list*型

　　用于*为表格最下方添加额外的总结栏*，其中列表的每个元素为*dict*型，可选的键有：

- content：*str*型，用于设置*当前对应总结栏内的文字内容*

- colSpan：*str*型，用于设置*当前总结栏占据的字段位置数量*，从而实现“合并单元格”的效果

- align：*str*型，用于设置*总结栏文字内容的对齐方式*，可选的有`'left'`、`'right'`和`'center'`

**summaryRowFixed：** *bool*型，默认为`False`

　　设置*是否为总结栏开启固定效果*，从而配合`maxHeight`表头固定呈现出更好的数据展示效果

**rowSelectionType：** *str*型，默认为`None`

　　当需要*开启行选择*功能时设置使用，默认不开启，可选的参数有`'checkbox'`（多选模式）与`'radio'`（单选模式）

**selectedRowKeys：** *list*型

　　对应*已被选择行key值列表*，可用于自主控制表格中的已选择行

**selectedRows：** *list*型

　　对应*已被选择行数据字段字典列表*

**rowSelectionWidth：** *int*或*string*型，默认为`'32px'`

　　用于设置*行选择控件列的宽度*

**sticky：** *bool*或*dict*型，默认为`False`

 　　用于设置*是否开启粘性表头功能*，当传入*dict*型参数时，可设置以下键值对参数：

- **offsetHeader：** *int*型，用于*设置粘性表头距离顶端的像素距离*

**titlePopoverInfo：** *dict*型

　　用于以指定字段名为键，为其表头添加悬浮气泡卡片，可用于为指定字段添加说明信息，其中参数字典可用键有：

- title：*str*型，设置气泡卡片*标题内容*

- content：*str*型，设置气泡卡片*文字说明内容*

　　示例：

```py
titlePopoverInfo = {
    '字段1': {
        'title': '字段1说明',
        'content': '这是字段1的具体含义说明'
    }
}
```

**mode：** *string*型，默认为`'client-side'`

　　用于设置组件的整体*数据渲染方式*，`'client-side'`对应*前端渲染模式*，此模式下数据在初始化时一次性传入前端，涉及到的*翻页*、*排序*及*筛选*功能均在前端自动完成，适合数据量较小（譬如小于10000行时）的情况；`'server-side'`对应*服务器端渲染模式*，此模式下*翻页*、*排序*及*筛选*功能均需由后端回调函数进行控制，前端任意时刻只会存放*翻页*、*排序*及*筛选*共同作用下对应的单页数据，极大程度上节省了内存和网络传输资源，适合数据量较大的情况，具体使用方式参考本页相应示例

**sortOptions：** *dict*型，可选

　　用于对指定若干列设置*排序*功能，可设定以下键值对参数：

- multiple：*bool*或*str*型，用于设置是否开启组合排序模式，默认为`False`即不开启，当设置为`'auto'`时，组合排序的优先级将自动根据用户点击字段排序的顺序而定，先点击进行排序的字段具有更高的优先级

- sortDataIndexes：*list*型，用于传入需要添加排序功能的若干字段`dataIndex`组成的列表，注意，当`multiple`设置为`True`时，`sortDataIndexes`传入的列表`dataIndex`顺序即代表了组合排序模式下的*排序优先级*

**filterOptions：** *dict*型，可选

　　用于对指定若干列设置*筛选*功能，与**sortOptions**不同的是，**filterOptions**中的键应为所要设置筛选功能的*字段名*，值则为字典，可设定以下键值对参数：

- filterMode：*string*型，用于设置筛选器模式，可选的有`'checkbox'`（勾选模式）和`'keyword'`（关键词搜索模式），默认为`'checkbox'`
- filterCustomItems：*list*型，当filterMode为`'checkbox'`时生效，用于自定义设置选择框中可供勾选的选项，默认不设置此参数时，会自动计算出对应字段的所有唯一值
- filterMultiple：*bool*型，当filterMode为`'checkbox'`时生效，用于设置是否开启多选模式，默认为`True`
- filterSearch：*bool*型，当filterMode为`'checkbox'`时生效，用于设置是否开启搜索框，默认为`False`

**containerId：** *string*型

　　用于在*局部滚动条*模式下，以传入对应*id*的方式为表格绑定合适的参考容器，从而修正滑动滚轮时悬浮层不跟随的问题，具体使用场景参考本页示例*妥善使用containerId参数*

**pagination：** *dict*型，可选

　　用于配置表格自带的*翻页*组件的相关功能，在*服务器端渲染*模式下用于返回最近一次翻页操作后的对应参数信息，其中涉及到的键值对有：

- position：*string*型，用于设置分页部件的*位置*，可选项有`'topLeft'`（左上）、`'topCenter'`（上方居中）、`'topRight'`（右上）、`'bottomLeft'`（左下）、`'bottomCenter'`（下方居中）、`'bottomRight'`（右下），默认为`bottomRight`

- pageSize：*int*型，用于设置初始状态下每页显示的纪录行数，默认为`10`条

- current：*int*型，用于设置初始状态下停留在的*页码*，默认为`1`

- showSizeChanger：*bool*型，用于设置*是否渲染页码尺寸切换器*，当`total`大于50时会自动设置为`True`

- pageSizeOptions：*list*型，用于设置*单页尺寸*切换选项中的可选项

- showQuickJumper：*bool*型，用于设置是否渲染*快速页码跳转*控件

- showTotalPrefix：*string*型，用于设置*总记录显示*内容，记录数值之前的文字内容，默认为`"共 "`

- showTotalSuffix：*string*型，用于设置*总记录显示*内容，记录数值之后的文字内容，默认为`" 条记录"`

- hideOnSinglePage：*bool*型，用于设置是否在数据记录行数少于pageSize时隐藏分页组件，默认为`False`

**bordered：** *bool*型，可选，默认为`False`

　　用于设置是否为单元格四周渲染网格线

**maxWidth：** *int*型，可选

　　用于设置表格的最大像素高度，当本页所有记录行长度超出此上显时会以*冻结表头*滑轮滑动的方式进行浏览

**maxHeight：** *int*型，可选

　　用于设置表格的最大像素高度，当本页所有记录行长度超出此上显时会以*冻结表头*滑轮滑动的方式进行浏览

**sorter：** *dict*型

　　用于在回调中捕获最近一次排序操作后，返回对应的字段及排序方式等参数信息，主要用于在*服务器端渲染*模式下实现排序操作

**filter：** *dict*型

　　用于在回调中捕获最近一次筛选操作后，返回对应的字段及筛选条件等参数信息，主要用于在*服务器端渲染*模式下实现筛选操作

**currentData：** *list*型

　　用于在回调中捕获最近一次修改之后整张表对应的`data`格式列表，由*排序*与*编辑*操作触发更新

**recentlyChangedRow：** *dict*型

　　用于在回调中捕获最近一次进行单元格内容修改之后，对应的行记录字典，由*编辑*操作触发更新

**recentlyButtonClickedRow：** *dict*型

　　对应**按钮模式**下，*最近一次被点击的按钮所在行数据记录字典*

**nClicksButton：** *int*型

　　 当表格中存在**按钮模式**字段时，用于记录所有按钮的*累计被点击次数*，适合用作监听按钮点击事件

**clickedContent：** *str*型

　　对应**按钮模式**下，*最近一次被点击的按钮对应的文字内容*，可用于在单个单元格渲染多按钮时区分具体被点击的按钮

**enableHoverListen：** *bool*型，默认为`False`

　　用于设置*是否开启表头/数据行鼠标移入事件监听*，此功能开启后可能会影响**按钮模式**等其他涉及到鼠标事件的功能，请慎用！

**recentlyMouseEnterColumn：** *str*型

　　当设置`enableHoverListen=True`后，用于记录最近一次鼠标移入的表头对应`dataIndex`信息

**recentlyMouseEnterRow：** *str*型

　　当设置`enableHoverListen=True`后，用于记录最近一次鼠标移入的数据行对应`key`信息

**expandedRowKeyToContent：** `list[dict]`型

　　用于*为对应行定义行展开内容*，其中每个元素为字典，需包含下列键值对：

- key：*string*型，用于设置对应的行`key`值
- content：*组件*型，用于设置对应的行展开内容

**expandedRowWidth：** *int*或*string*型

　　用于设置*行展开控件字段列的宽度*

**expandRowByClick：** *bool*型，默认为`False`

　　用于设置*点击对应是否也可触发行展开操作*