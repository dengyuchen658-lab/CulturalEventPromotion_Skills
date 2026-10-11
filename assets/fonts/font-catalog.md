# 随包字体资源

使用时从Skill根目录解析资源路径，无需全局安装，不依赖用户下载目录。以下为候选资源，依据活动学科、研究对象、表达方向及字形覆盖选择；不强制所有海报使用。

| 资源 | 核验家族／样式 | 适合角色 | 使用限制 |
|---|---|---|---|
| [VonwaonBitmap-16px.ttf](vonwaon-bitmap/VonwaonBitmap-16px.ttf) | VonwaonBitmap 16px／Regular，Version 1.00 | 数字人文、数字媒介与技术主题中的短标题、数字 | 像素是媒介气质，不自动代表所有科学研究；不用于密集嘉宾、机构、议程与细则 |
| [VonwaonBitmap-16pxLite.ttf](vonwaon-bitmap/VonwaonBitmap-16pxLite.ttf) | VonwaonBitmap 16pxLite／Regular | 已核验字符的短标题、日期、标签 | Lite为较小字库版本，不等于更细字重；缺字时选择有覆盖的完整版或另一合适字体 |
| [演示夏行楷.ttf](slide-xiaxing/演示夏行楷.ttf) | Slidexiaxing／Regular，Version 1.000 | 文化遗产、历史、艺术等相关主题的大标题或有限强调文字 | 不用于密集正文；自然科学、医学、工程等活动不得因“学术论坛”身份直接套用 |
| [思源宋体CN](source-han-serif-cn/font-config.md) | Regular／Medium／Bold | 需要宋体结构和正式出版气质的标题、信息与正文 | 字重、覆盖及许可按该配置文件核对 |

## 覆盖与排版核验

- 本次检查记录：16px完整版映射7542个字符，Lite映射4040个字符，演示夏行楷映射6973个字符；字库数量不等于任何未来文案都能排印。
- 本轮数字人文论坛实际标题字符及ASCII英文、数字均有覆盖。每次使用仍须核验新文案中的姓名、机构、学科术语和标点，禁止静默替换成方框或错误字符。
- 像素字体以原生16px网格的整数倍作为优先试排尺寸，检查导出和手机缩略图的网格与笔画；可读性优先，不以整数倍为不可调整的硬约束。
- 中英文可使用不同字体体现对应的信息角色；英文无需照搬中文行楷。正文使用有覆盖、许可适用且容易阅读的黑体、宋体、衬线或无衬线字体。

## 来源与许可记录

三份TTF由用户提供，加入时保持原始二进制内容。字体内版权字段分别为Haoyu Qiu（2021）和keynoteart（2020）。

像素字体随下载包附带的[license.txt](vonwaon-bitmap/license.txt)声明“Vonwaon Bitmap Font Lite (1.0)”适用CC0，并允许个人、教育和商业项目使用。原文随包保存；该文件标题明确为Lite，16px完整版与该声明的对应关系尚未单独核验，不扩大解释为全部文件许可已确认。

演示夏行楷下载包未附可核验的许可文本；字体内版权声明不是授权条款。保留其用户提供、用于本轮本地设计测试的来源记录，商业用途和对外分发范围标为待确认。不要据下载站广告或文件名自行认定“免费商用”，也不要生成不存在的许可证。

## 成员强制模板字体

六套成员模板保留完整资源与原加载路径，字体无需全局安装。艺术街区、工作坊及体育赛事必须按 [类别模板路由](../../references/category-template-routing.md) 使用指定文件，不能从本索引自由挑选替代模板字体。

| 模板 | 实际字体目录与角色 |
|---|---|
| 艺术街区中文 | [字体目录](../category-templates/art-district/zh-CN/assets/fonts/)：澹雅明体DYmingB.ttf 用于标题；Harmony Regular／Medium／Bold 用于信息与数字 |
| 艺术街区英文 | [字体目录](../category-templates/art-district/en/assets/fonts/)：Trajan Bold 标题非数字；Futura Std Book／Medium／Bold 信息；Harmony Regular／Medium／Bold 数字 |
| 工作坊中文 | [字体目录](../category-templates/workshop/zh-CN/fonts/)：HarmonyOS Sans SC 六份 TTF，实际角色依模板 |
| 工作坊英文 | [字体目录](../category-templates/workshop/en/fonts/)：同系列六份 TTF，字母、数字、标点均依模板 |

按字体文件哈希去重共 19 份新字体资源；多个模板中的相同文件保留各自路径，以免破坏原脚本。Futura Maxi、Trajan Regular 和其他附带字重保留，只有模板允许或用户明确指定时使用，不自动替换当前角色。每次新文案仍须核对字形覆盖、实际注册、字重与测量。

来源为用户提供的小组成员包，复制时保持二进制不变。未随包提供独立完整许可证或购买授权凭据。Futura Maxi 内置条款明确限制复制与分发；澹雅明体内置字段为 IPA Open Font License v1.0；其余字体的文件名、版权字段或许可网址不构成完整授权核验。当前记录为课程本地合并；对外发布字体包时须按实际许可证确认，不能把它们标为全部免费商用。逐文件元数据及哈希见 [字体记录](member-template-fonts.json)。

## 体育赛事成员字体

[中文字体目录](../category-templates/sports/zh-CN/fonts/) 与 [英文字体目录](../category-templates/sports/en/fonts/) 各保留江城律动黑.ttf 和 HarmonyOS Sans SC 六字重。主标题实际加载江城律动黑，其余文字按模板使用 Harmony；不能静默替换。文件字节数与 SHA256 见各包 references/font-assets.json，来源为用户小组成员包，二进制保持原样。未据文件名新增免费商用或对外分发授权结论。
