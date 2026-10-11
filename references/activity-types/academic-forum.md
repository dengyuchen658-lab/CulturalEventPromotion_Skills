# 学术会议／论坛

- `primary_type`: `lecture`
- 次类型：国际论坛、学术会议、主旨演讲、分论坛、圆桌。
- 范围：学术活动的议题传播、学术身份、国际化表达和参会信息；不把科学学术、人文学术或数字人文处理成同一种装饰风格。
- 与[内容母本](../content-master-schema.md)、[双语内容规则](../bilingual-content.md)、[双语字体与排版策略](../bilingual-typography.md)和[统一QA](../quality-control-and-iteration.md)共同使用。

## 成品画布与比例锁定

- 本轮用户要求及本Skill母本默认均为**4:5竖版、2400×3000px**，中文和英文完整成品一致。用户后续明确指定其他规格时才覆盖，并记录该指令来源。
- 将用户规格写入`deliverables.canvas`，同时绑定排版画布、PNG真实像素、PDF页面比例、预览图、交付清单和文件名。不能为了容纳长英文或多机构信息自行改成2:3。
- 参考海报的比例、横向主视觉素材的比例、生成模型输出比例不替代最终海报规格。素材可等比放置和合理裁切，文字按4:5重排；禁止拉伸旧成图或裁掉必要信息来伪装为正确比例。
- 返工后将实际文件尺寸与用户原始规格核对，再执行交付校验；不得只让错误母本与错误文件相互匹配。尺寸不符回退排版／导出层，两种语言均修正。

## 内容与证据

按资料提取中文名称、官方英文名称、学术主题、副标题／年度议题、日期、时间、时区、线下地点、线上／线下／混合形式、主办承办协办、学术指导／支持机构、主旨嘉宾、单位和职务、分论坛／圆桌／工作坊、议程摘要、会议语言、同传／字幕、面向人群、报名截止、费用、线上平台、联系信息和官网。每个值保存原文依据、来源文件和页码／区域；缺失、冲突及待确认字段分别标记，不靠论坛类别补事实。

- 官方英文专名优先；没有官方译名时允许制作标为`pending`的工作译文审阅稿，不将其写成已确认官方名称。
- 国际活动分别检查会议日期、每日时段、报到时段及其时区；举办地不能替代资料中的时区依据。关键行动信息或时区待确认时限制正式发布状态，不妨碍明确标记的设计测试。
- 不虚构真实专家、职务、机构、合作关系、论文、研究成果、议程、费用、会议平台、网址或二维码。
- 自拟测试活动只在用户允许时使用；所有自拟值明确标记“虚构测试数据”和`test_only`，与真实资料字段隔离。该测试标记不意味着现有事实校验器已支持正式交付。

## 学科、视觉与字体适配

先判断研究对象与研究方法，再选择母题和字体。使用清晰网格、稳定对齐和可追踪的学科线索体现学术气质；国际化由准确双语、导航信息和可阅读的版式体现，不依赖地球、国旗、霓虹或伪数据装饰。

| 学科／场景 | 可选视觉依据 | 标题字体选择 |
|---|---|---|
| 人文、历史、艺术史、考古、文化遗产 | 有来源的文献、图像、档案、地图、材料痕迹 | 清晰宋体、人文黑体；文化关系成立时可局部使用克制书法／行楷 |
| 社会科学、教育、传播 | 议题关系、研究材料、交流网络 | 中性黑体或人文无衬线；需要出版气质时可用可读衬线字体 |
| 自然科学、工程、医学、计算机 | 有依据的结构、观测、材料、图解、网络 | 中性黑体、现代无衬线或易读衬线；不因“文化活动”或“学术论坛”身份套用书法 |
| 数字人文、数字遗产、数字媒介 | 与主题相关的扫描、档案、标注、点云、数字重建 | 可用像素短标题体现数字媒介，用宋体／行楷强调人文对象；不强制双字体组合 |
| 跨学科国际论坛 | 主议题的证据、方法或交流结构 | 中性高可读字体优先；按议题决定有限强调字体，保持中英文角色一致 |

随包候选见[字体资源索引](../../assets/fonts/font-catalog.md)：

- [VonwaonBitmap-16px](../../assets/fonts/vonwaon-bitmap/VonwaonBitmap-16px.ttf)：适合相关数字主题的大标题、短标签。
- [VonwaonBitmap-16pxLite](../../assets/fonts/vonwaon-bitmap/VonwaonBitmap-16pxLite.ttf)：可用于已核验覆盖的年份、日期、议程日期；Lite不等于更细字重。
- [演示夏行楷](../../assets/fonts/slide-xiaxing/演示夏行楷.ttf)：适合相关人文／遗产标题的局部强调，不用于长英文、密集正文、机构和嘉宾表。

候选字体不是全类默认。逐次检查真实文案的字形覆盖、许可、字距和缩略图可读性。数字人文测试中的“像素字＋行楷”是研究方法与研究对象共同决定的方案，不泛化到所有技术论坛。

## 复杂信息与嘉宾组织

- 常规入口：论坛名称／核心主题 > 日期、地点、形式 > 核心嘉宾／议程价值 > 报名截止、费用、语言及行动 > 主办承办等身份信息。主旨嘉宾确为传播核心时可提升嘉宾模块；有报名门槛或国际参与时提升行动和语言模块，记录理由。
- 标题与议题避免争夺同一级视觉重心；日期和地点保持快速辨识。主办承办采用明确分组，不全部压缩成不可读底部小字。
- 议程按日期、场次或分论坛分组，区分开幕／主旨、分论坛、圆桌和闭幕；时间、讲者和题目未提供就不补造。
- 嘉宾姓名、单位、职务、讲题使用资料确认值；头像使用原始获准素材。仅有人数或来源地区时可用有据概述，不能自动生成姓名、头像或头衔。
- 三个日期可采用三列概要；更多场次或长讲题改用纵向列表、配套议程海报或详细资料入口，不强行维持三列。完整母本保留主海报未排入的内容。
- 混合活动同时保留线下地点、线上方式与注册条件；线上免费但需注册等条件不能漏掉。没有链接就不生成报名二维码或虚假入口。

## 双语与制作

- 中英文共享事实母本和视觉概念，逐项对应名称、日期、时间、时区、地点、形式、嘉宾、议程、主办承办、费用、注册条件和语言服务。
- 英文按完整语义重新断行，可扩大标题区、移动主视觉、调整字号和机构模块；不靠压缩字宽或不断缩小字号容纳长名称。
- 中文行楷的英文对应可以采用正式衬线字体，中文像素标题的英文对应可以采用覆盖合适的像素字；匹配信息角色与气质，不要求字形机械相同。正文仍使用可读字体。
- 图像生成只制作无正式文字的主视觉。名称、专名、日期、议程、费用、Logo和二维码通过可控排版或原始素材加入；工具不能通过提示词读取和准确使用本地TTF。
- 在实际交付尺寸及手机预览下检查大小写、数字、专名、字形缺失、孤行、文本框溢出、文字交叠、对比和安全区；两种语言分别检查，公共效果未经测试时标记未验证。

## 可复用主视觉提示词

先用已确认的学科、议题、母题和实际输出需求替换尖括号变量。只保留适用的学科分支；像素、书法、青绿色、石质碎片均不是固定默认。成品默认4:5、2400×3000px；主视觉素材另按已分配区域构图。

```text
Create an original academic forum key visual for <discipline and approved research topic>.
The final Chinese and English posters are portrait 4:5 at 2400x3000 px unless the user explicitly overrides this. This request generates only artwork for <reserved image region>; its asset aspect ratio does not override the final poster canvas.
Use one coherent visual metaphor grounded in <verified research object, material or method>. It may involve archival materials, diagrams, field observation, knowledge networks, manuscripts, maps or material evidence when relevant. Do not invent research results or use decorative pseudo-data.
Build a clear editorial composition for <canvas and use scene>, with a strong future title area, a separate quiet area for event details, a consistent grid, generous margins and controlled negative space. Keep the academic tone calm, precise and professional, with a restrained palette selected for this topic.
For humanities, historical arts or archaeology, use relevant archival textures, material traces or historical diagrams only when supported; restrained brush-like gestures may support an appropriate cultural topic.
For natural sciences, engineering, medicine or computer science, use relevant precise structures, observation-based forms or analytical spatial systems. Avoid generic calligraphy, antique ornament and unrelated literary styling.
For digital humanities or digital heritage, connect the humanistic research object with its digital method through a coherent transition, annotation, scan or reconstruction metaphor; avoid generic gaming or neon sci-fi aesthetics.
Generate no lettering, Chinese characters, English words, names, dates, logos, institutional marks, QR codes, watermarks or unreadable pseudo-text. Do not generate speaker portraits or recognizable historical objects without approved inputs. Preserve clean text-safe zones for accurate controlled typography later.
The result must be an original scholarly visual identity. Learn composition and information hierarchy from approved references without copying their imagery, calligraphy or layout verbatim.
```

## 可复用文字排版提示词

该提示用于可控文字排版阶段，字体路径从Skill资源索引解析，不交给图像模型虚拟重绘。省略缺失且不适用字段，明确记录待确认项目。

```text
Create Chinese and English academic forum posters from one approved content master and the selected text-free key visual.
Lock both complete poster canvases to portrait 4:5, 2400x3000 px, unless the user explicitly specifies a different size. Reflow all titles and information modules within this canvas; do not stretch a previous raster poster, drop required copy or change the ratio to accommodate text. Verify actual exported PNG dimensions and PDF page ratios against the original user requirement.
Use H1 for the official forum title and primary academic identity, H2 for the research theme or annual topic, H3 for date, time, timezone, venue, event format and participation action. Group verified speakers, agenda, language services, registration deadline, fees, hosts and organizers according to their relevance to the audience.
Select authorized, available fonts by discipline and information role. Humanities and heritage titles may use readable Song-style or restrained calligraphic display typography. Natural sciences, engineering and medicine favor clear neutral typography. Pixel typography is optional for a relevant digital method or medium, and is limited to legible display text or short labels.
Use the bundled TTF files only after checking the actual glyph coverage and license status. Keep dense speaker, institution, agenda and registration text in readable fonts.
Reflow the English title and institution names independently. Match Chinese and English hierarchy and tone rather than forcing identical line breaks, font shapes or text boxes. Preserve all confirmed names, numbers, dates, timezones, institutions, fees, URLs and conditions exactly.
Do not invent missing speakers, academic titles, agenda entries, organizations, platforms, registration links or QR codes. Label working translations and test drafts clearly. Check text overflow, overlap, contrast, safe zones and mobile readability separately for both language versions.
```
