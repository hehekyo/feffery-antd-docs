from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc
import feffery_markdown_components as fmc

import callbacks.AntdSelect

docs_content = html.Div(
    [
        html.Div(
            [
                html.H2(
                    'AntdSelect(id, className, style, *args, **kwargs)',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5'
                    }
                ),

                fac.AntdBackTop(
                    containerId='docs-content',
                    duration=0.6
                ),

                html.Span(
                    '主要参数说明：',
                    id='主要参数说明',
                    style={
                        'borderLeft': '4px solid grey',
                        'padding': '3px 0 3px 10px',
                        'backgroundColor': '#f5f5f5',
                        'fontWeight': 'bold',
                        'fontSize': '1.2rem'
                    }
                ),

                fmc.FefferyMarkdown(
                    markdownStr=open('documents/AntdSelect.md', encoding='utf-8').read()
                ),

                html.Div(
                    html.Span(
                        '使用示例',
                        id='使用示例',
                        style={
                            'borderLeft': '4px solid grey',
                            'padding': '3px 0 3px 10px',
                            'backgroundColor': '#f5f5f5',
                            'fontWeight': 'bold',
                            'fontSize': '1.2rem'
                        }
                    ),
                    style={
                        'marginBottom': '10px'
                    }
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择国家：',
                            options=[
                                {'label': '中国', 'value': '中国'},
                                {'label': '美国', 'value': '美国'},
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国', 'disabled': True},
                                {'label': '加拿大', 'value': '加拿大'}
                            ],
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '基础的下拉选择',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择国家：',
    options=[
        {'label': '中国', 'value': '中国'},
        {'label': '美国', 'value': '美国'},
        {'label': '俄罗斯', 'value': '俄罗斯'},
        {'label': '德国', 'value': '德国', 'disabled': True},
        {'label': '加拿大', 'value': '加拿大'}
    ],
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='基础的下拉选择',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择国家：',
                            options=[
                                {
                                    'group': '亚洲',
                                    'options': [
                                        {'label': '中国', 'value': '中国'}
                                    ]
                                },
                                {
                                    'group': '北美洲',
                                    'options': [
                                        {'label': '美国', 'value': '美国'},
                                        {'label': '加拿大', 'value': '加拿大'}
                                    ]
                                },
                                {
                                    'group': '欧洲',
                                    'options': [
                                        {'label': '俄罗斯', 'value': '俄罗斯'},
                                        {'label': '德国', 'value': '德国', 'disabled': True}
                                    ]
                                }
                            ],
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '分组下拉选择',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择国家：',
    options=[
        {
            'group': '亚洲',
            'options': [
                {'label': '中国', 'value': '中国'}
            ]
        },
        {
            'group': '北美洲',
            'options': [
                {'label': '美国', 'value': '美国'},
                {'label': '加拿大', 'value': '加拿大'}
            ]
        },
        {
            'group': '欧洲',
            'options': [
                {'label': '俄罗斯', 'value': '俄罗斯'},
                {'label': '德国', 'value': '德国', 'disabled': True}
            ]
        }
    ],
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='分组下拉选择',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择离散色彩：',
                            colorsMode='diverging',
                            colorsNameWidth=50,
                            options=[
                                {
                                    'label': 'Balance_5',
                                    'value': 'Balance_5',
                                    'colors': ['#181c43', '#3888ba', '#f1eceb', '#c05a3c', '#3c0912']
                                },
                                {
                                    'label': 'Curl_6',
                                    'value': 'Curl_6',
                                    'colors': ['#151d44', '#117d79', '#b6cbaf', '#e6b7a2', '#ae4060', '#340d35']
                                },
                                {
                                    'label': '钴蓝',
                                    'value': '钴蓝',
                                    'colors': ['#6b9bb8']
                                }
                            ],
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdSelect(
                            placeholder='请选择连续色彩：',
                            colorsNameWidth=50,
                            options=[
                                {
                                    'label': 'Amp',
                                    'value': 'Amp',
                                    'colors': ['#f1edec', '#d7a291', '#c0583b', '#901029', '#3c0912']
                                },
                                {
                                    'label': 'Deep',
                                    'value': 'Deep',
                                    'colors': ['#fdfecc', '#78cea3', '#488e9e', '#404d8c', '#281a2c']
                                }
                            ],
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '色带渲染模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdParagraph(
                            [
                                fac.AntdText('　　色带模式下展示预设的色彩型输入更加形象直观')
                            ]
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择离散色彩：',
    colorsMode='diverging',
    colorsNameWidth=50,
    options=[
        {
            'label': 'Balance_5',
            'value': 'Balance_5',
            'colors': ['#181c43', '#3888ba', '#f1eceb', '#c05a3c', '#3c0912']
        },
        {
            'label': 'Curl_6',
            'value': 'Curl_6',
            'colors': ['#151d44', '#117d79', '#b6cbaf', '#e6b7a2', '#ae4060', '#340d35']
        },
        {
            'label': '钴蓝',
            'value': '钴蓝',
            'colors': ['#6b9bb8']
        }
    ],
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
),

fac.AntdSelect(
    placeholder='请选择连续色彩：',
    colorsNameWidth=50,
    options=[
        {
            'label': 'Amp',
            'value': 'Amp',
            'colors': ['#f1edec', '#d7a291', '#c0583b', '#901029', '#3c0912']
        },
        {
            'label': 'Deep',
            'value': 'Deep',
            'colors': ['#fdfecc', '#78cea3', '#488e9e', '#404d8c', '#281a2c']
        }
    ],
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='色带渲染模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择国家（多选）：',
                            options=[
                                {'label': '中国', 'value': '中国'},
                                {'label': '美国', 'value': '美国'},
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国'},
                                {'label': '加拿大', 'value': '加拿大'}
                            ],
                            mode='multiple',
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        # 自由新增模式下，输入框内即使输入不存在的选项
                        # 按下enter之后也会被添加到已选择
                        fac.AntdSelect(
                            placeholder='请选择国家（自由新增）：',
                            options=[
                                {'label': '中国', 'value': '中国'},
                                {'label': '美国', 'value': '美国'},
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国'},
                                {'label': '加拿大', 'value': '加拿大'}
                            ],
                            mode='tags',
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '多选与自由新增模式',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择国家（多选）：',
    options=[
        {'label': '中国', 'value': '中国'},
        {'label': '美国', 'value': '美国'},
        {'label': '俄罗斯', 'value': '俄罗斯'},
        {'label': '德国', 'value': '德国'},
        {'label': '加拿大', 'value': '加拿大'}
    ],
    mode='multiple',
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
),

# 自由新增模式下，输入框内即使输入不存在的选项
# 按下enter之后也会被添加到已选择
fac.AntdSelect(
    placeholder='请选择国家（自由新增）：',
    options=[
        {'label': '中国', 'value': '中国'},
        {'label': '美国', 'value': '美国'},
        {'label': '俄罗斯', 'value': '俄罗斯'},
        {'label': '德国', 'value': '德国'},
        {'label': '加拿大', 'value': '加拿大'}
    ],
    mode='tags',
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='多选与自由新增模式',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择国家：',
                            options=[
                                {'label': '中国', 'value': '中国'},
                                {'label': '美国', 'value': '美国'},
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国'},
                                {'label': '加拿大', 'value': '加拿大'}
                            ],
                            defaultValue=['中国', '美国'],
                            mode='multiple',
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置默认选中值',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择国家：',
    options=[
        {'label': '中国', 'value': '中国'},
        {'label': '美国', 'value': '美国'},
        {'label': '俄罗斯', 'value': '俄罗斯'},
        {'label': '德国', 'value': '德国'},
        {'label': '加拿大', 'value': '加拿大'}
    ],
    defaultValue=['中国', '美国'],
    mode='multiple',
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='设置默认选中值',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择项目：',
                            options=[
                                {'label': f'项目{i}', 'value': f'项目{i}'}
                                for i in range(200)
                            ],
                            mode='multiple',
                            listHeight=500,
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '修改下拉选择最大高度',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择项目：',
    options=[
        {'label': f'项目{i}', 'value': f'项目{i}'}
        for i in range(200)
    ],
    mode='multiple',
    listHeight=500,
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='修改下拉选择最大高度',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择项目：',
                            options=[
                                {'label': f'项目{i}', 'value': f'项目{i}'}
                                for i in range(200)
                            ],
                            mode='multiple',
                            listHeight=500,
                            maxTagCount=3,  # 设置最大显示3个
                            style={
                                # 使用css样式固定宽度
                                'width': '350px'
                            }
                        ),

                        fac.AntdDivider(
                            '设置输入框已选择选项最大显示数量',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择项目：',
    options=[
        {'label': f'项目{i}', 'value': f'项目{i}'}
        for i in range(200)
    ],
    mode='multiple',
    listHeight=500,
    maxTagCount=3, # 设置最大显示3个
    style={
        # 使用css样式固定宽度
        'width': '350px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='设置输入框已选择选项最大显示数量',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSelect(
                            placeholder='请选择项目：',
                            options=[],
                            style={
                                # 使用css样式固定宽度
                                'width': '350px'
                            }
                        ),

                        fac.AntdDivider(
                            '自主控制显示空状态示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
fac.AntdSelect(
    placeholder='请选择项目：',
    options=[],
    style={
        # 使用css样式固定宽度
        'width': '350px'
    }
)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='自主控制显示空状态示例',
                    className='div-highlight'
                ),

                html.Div(
                    [
                        fac.AntdSpin(
                            html.Pre('[]', id='select-demo-output'),
                            text='回调中'
                        ),
                        fac.AntdSelect(
                            id='select-demo',
                            placeholder='请选择国家：',
                            mode='multiple',
                            options=[
                                {'label': '中国', 'value': '中国'},
                                {'label': '美国', 'value': '美国'},
                                {'label': '俄罗斯', 'value': '俄罗斯'},
                                {'label': '德国', 'value': '德国', 'disabled': True},
                                {'label': '加拿大', 'value': '加拿大'}
                            ],
                            style={
                                # 使用css样式固定宽度
                                'width': '200px'
                            }
                        ),

                        fac.AntdDivider(
                            '回调示例',
                            lineColor='#f0f0f0',
                            innerTextOrientation='left'
                        ),

                        fac.AntdCollapse(
                            fuc.FefferySyntaxHighlighter(
                                showLineNumbers=True, 
                                language='python',
                                 codeTheme='coy-without-shadows',
                                codeString='''
html.Pre('[]', id='select-demo-output'),
fac.AntdSelect(
    id='select-demo',
    placeholder='请选择国家：',
    mode='multiple',
    options=[
        {'label': '中国', 'value': '中国'},
        {'label': '美国', 'value': '美国'},
        {'label': '俄罗斯', 'value': '俄罗斯'},
        {'label': '德国', 'value': '德国', 'disabled': True},
        {'label': '加拿大', 'value': '加拿大'}
    ],
    style={
        # 使用css样式固定宽度
        'width': '200px'
    }
)
...
@app.callback(
    Output('select-demo-output', 'children'),
    Input('select-demo', 'value'),
    prevent_initial_call=True
)
def button_callback_demo(value):

    return str(value)'''
                            ),
                            title='点击查看代码',
                            is_open=False,
                            ghost=True
                        )

                    ],
                    style={
                        'marginBottom': '40px',
                        'padding': '10px 10px 20px 10px',
                        'border': '1px solid #f0f0f0'
                    },
                    id='回调示例',
                    className='div-highlight'
                ),

                html.Div(style={'height': '100px'})
            ],
            style={
                'flex': 'auto'
            }
        ),
        html.Div(
            fac.AntdAnchor(
                linkDict=[
                    {'title': '主要参数说明', 'href': '#主要参数说明'},
                    {
                        'title': '使用示例',
                        'href': '#使用示例',
                        'children': [
                            {'title': '基础的下拉选择', 'href': '#基础的下拉选择'},
                            {'title': '分组下拉选择', 'href': '#分组下拉选择'},
                            {'title': '色带渲染模式', 'href': '#色带渲染模式'},
                            {'title': '多选与自由新增模式', 'href': '#多选与自由新增模式'},
                            {'title': '设置默认选中值', 'href': '#设置默认选中值'},
                            {'title': '修改下拉选择最大高度', 'href': '#修改下拉选择最大高度'},
                            {'title': '设置输入框已选择选项最大显示数量', 'href': '#设置输入框已选择选项最大显示数量'},
                            {'title': '自主控制显示空状态示例', 'href': '#自主控制显示空状态示例'},
                            {'title': '回调示例', 'href': '#回调示例'}
                        ]
                    },
                ],
                offsetTop=0
            ),
            style={
                'flex': 'none',
                'margin': '20px'
            }
        )
    ],
    style={
        'display': 'flex'
    }
)
