from dash import html
from dash import dcc
import feffery_antd_components as fac

import callbacks.AntdInput

docs_content = html.Div(
    [
        html.H2(
            'AntdInput(id, className, style, *args, **kwargs)',
            style={
                'borderLeft': '4px solid grey',
                'padding': '3px 0 3px 10px',
                'backgroundColor': '#f5f5f5'
            }
        ),

        fac.AntdAnchor(
            linkDict=[
                {'title': '主要参数说明', 'href': '#主要参数说明'},
                {
                    'title': '使用示例',
                    'href': '#使用示例',
                    'children': [
                        {'title': '基础的输入框', 'href': '#基础的输入框'},
                        {'title': 'default模式下设置前后缀内容', 'href': '#default模式下设置前后缀内容'},
                        {'title': '其他输入框模式', 'href': '#其他输入框模式'},
                        {'title': '设置初始状态填充值', 'href': '#设置初始状态填充值'},
                        {'title': '文本域模式下显示已输入内容字数', 'href': '#文本域模式下显示已输入内容字数'},
                        {'title': '回调示例', 'href': '#回调示例'},
                    ]
                },
            ],
            containerId='docs-content',
            targetOffset=200
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

        dcc.Markdown(open('documents/AntdInput.md', encoding='utf-8').read(),
                     dangerously_allow_html=True),

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
                fac.AntdInput(
                    size='small',
                    placeholder='基础的输入框',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    size='middle',
                    placeholder='基础的输入框',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    size='large',
                    placeholder='基础的输入框',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),

                fac.AntdDivider(
                    '基础的输入框',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdInput(
                                    size='small',
                                    placeholder='基础的输入框',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Br(),
                                fac.AntdInput(
                                    size='middle',
                                    placeholder='基础的输入框',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Br(),
                                fac.AntdInput(
                                    size='large',
                                    placeholder='基础的输入框',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                ```
                                '''),
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
            id='基础的输入框',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdInput(
                    placeholder='default输入框示例',
                    addonBefore='前缀示例',
                    addonAfter='后缀示例',
                    style={
                        'width': '300px',
                        'marginBottom': '5px'
                    }
                ),

                fac.AntdDivider(
                    'default模式下设置前后缀内容',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdInput(
                                    placeholder='default输入框示例',
                                    addonBefore='前缀示例',
                                    addonAfter='后缀示例',
                                    style={
                                        'width': '300px',
                                        'marginBottom': '5px'
                                    }
                                )
                                ```
                                '''),
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
            id='其他三种输入框模式',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdInput(
                    mode='search',
                    placeholder='search输入框示例',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    mode='text-area',
                    placeholder='text-area输入框示例',
                    style={
                        'width': '200px',
                        'marginBottom': '5px',
                        'height': '80px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    mode='password',
                    placeholder='password输入框示例',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),

                fac.AntdDivider(
                    '其他输入框模式',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdInput(
                                    mode='search',
                                    placeholder='search输入框示例',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                
                                fac.AntdInput(
                                    mode='text-area',
                                    placeholder='text-area输入框示例',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px',
                                        'height': '80px'
                                    }
                                ),
                
                                fac.AntdInput(
                                    mode='password',
                                    placeholder='password输入框示例',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                )
                                ```
                                '''),
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
            id='其他输入框模式',
            className='div-highlight'
        ),

        html.Div(
            [

                fac.AntdInput(
                    defaultValue='预填充文字',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    mode='search',
                    defaultValue='预填充文字',
                    style={
                        'width': '200px',
                        'marginBottom': '5px'
                    }
                ),
                html.Br(),
                fac.AntdInput(
                    mode='text-area',
                    defaultValue='预填充文字',
                    style={
                        'width': '200px',
                        'marginBottom': '5px',
                        'height': '80px'
                    }
                ),

                fac.AntdDivider(
                    '设置初始状态填充值',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdInput(
                                    defaultValue='预填充文字',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                
                                fac.AntdInput(
                                    mode='search',
                                    defaultValue='预填充文字',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px'
                                    }
                                ),
                
                                fac.AntdInput(
                                    mode='text-area',
                                    defaultValue='预填充文字',
                                    style={
                                        'width': '200px',
                                        'marginBottom': '5px',
                                        'height': '80px'
                                    }
                                )
                                ```
                                '''),
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
            id='设置初始状态填充值',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdInput(
                    mode='text-area',
                    defaultValue='0123456789',
                    allowClear=True,
                    maxLength=10,
                    showCount=True,
                    style={
                        'width': '400px'
                    }
                ),

                fac.AntdDivider(
                    '文本域模式下显示已输入内容字数',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdInput(
                                    mode='text-area',
                                    defaultValue='0123456789',
                                    allowClear=True,
                                    maxLength=10,
                                    showCount=True,
                                    style={
                                        'width': '400px'
                                    }
                                )
                                ```
                                '''),
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
            id='文本域模式下显示已输入内容字数',
            className='div-highlight'
        ),

        html.Div(
            [
                fac.AntdSpin(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdInput(
                                    id='input-value-demo',
                                    placeholder='value直接作为Input',
                                    style={
                                        'width': '250px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Span(id='input-value-demo-output')
                            ]
                        ),

                        html.Br(),

                        fac.AntdSpace(
                            [
                                fac.AntdInput(
                                    id='input-nSubmit-demo',
                                    placeholder='nSubmit作为Input，value作为State',
                                    style={
                                        'width': '250px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Span(id='input-nSubmit-demo-output')
                            ]
                        ),
                        html.Br(),

                        fac.AntdSpace(
                            [
                                fac.AntdInput(
                                    id='input-nClicksSearch-demo',
                                    mode='search',
                                    placeholder='nClicksSearch作为Input，value作为State',
                                    style={
                                        'width': '320px',
                                        'marginBottom': '5px'
                                    }
                                ),
                                html.Span(id='input-nClicksSearch-demo-output')
                            ]
                        )
                    ],
                    text='回调中'
                ),

                fac.AntdDivider(
                    '回调示例',
                    lineColor='#f0f0f0',
                    innerTextOrientation='left'
                ),

                fac.AntdCollapse(
                    dcc.Markdown('''
                                ```Python
                                fac.AntdSpace(
                                    [
                                        fac.AntdInput(
                                            id='input-value-demo',
                                            placeholder='value直接作为Input',
                                            style={
                                                'width': '250px',
                                                'marginBottom': '5px'
                                            }
                                        ),
                                        html.Span(id='input-value-demo-output')
                                    ]
                                ),
        
                                html.Br(),
        
                                fac.AntdSpace(
                                    [
                                        fac.AntdInput(
                                            id='input-nSubmit-demo',
                                            placeholder='nSubmit作为Input，value作为State',
                                            style={
                                                'width': '250px',
                                                'marginBottom': '5px'
                                            }
                                        ),
                                        html.Span(id='input-nSubmit-demo-output')
                                    ]
                                ),
                                html.Br(),
        
                                fac.AntdSpace(
                                    [
                                        fac.AntdInput(
                                            id='input-nClicksSearch-demo',
                                            mode='search',
                                            placeholder='nClicksSearch作为Input，value作为State',
                                            style={
                                                'width': '320px',
                                                'marginBottom': '5px'
                                            }
                                        ),
                                        html.Span(id='input-nClicksSearch-demo-output')
                                    ]
                                )
                                ...
                                @app.callback(
                                    Output('input-value-demo-output', 'children'),
                                    Input('input-value-demo', 'value'),
                                    prevent_initial_call=True
                                )
                                def input_value_callback_demo(value):
                                
                                    return fac.AntdText(f'value: {value}', italic=True)
                                
                                
                                @app.callback(
                                    Output('input-nSubmit-demo-output', 'children'),
                                    Input('input-nSubmit-demo', 'nSubmit'),
                                    State('input-nSubmit-demo', 'value'),
                                    prevent_initial_call=True
                                )
                                def input_nSubmit_callback_demo(nSubmit, value):
                                
                                    if nSubmit and value:
                                        return fac.AntdText(f'nSubmit: {nSubmit}   value: {value}', italic=True)
                                
                                
                                @app.callback(
                                    Output('input-nClicksSearch-demo-output', 'children'),
                                    Input('input-nClicksSearch-demo', 'nClicksSearch'),
                                    State('input-nClicksSearch-demo', 'value'),
                                    prevent_initial_call=True
                                )
                                def input_nClicksSearch_callback_demo(nClicksSearch, value):

                                    if nClicksSearch and value:
                                        return fac.AntdText(f'nClicksSearch: {nClicksSearch}   value: {value}', italic=True)

                                ```
                                '''),
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
    ]
)
