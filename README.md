# AIGC Skills

我自己的 AIGC 创作技能库。把想表达的画面、人物表演和镜头逐步聊成可执行的设计、提示词与预演，再按成片需要设计后期音效。较长的片子先定大方向和分场，再逐段制作。

这里统一保存当前使用的技能，方便查看、维护和按需下载。以自己的实际工作方式为先；没有包装成 plugin，也没有为了平台通用性改写原有正文。

## 技能目录

| 技能 | 用途 | 内容 | 单独下载 |
|---|---|---|---|
| 长片分场制作 | 不止一场的片子先定大方向和每场要表达什么，再逐段设计、生成、接上前面检查，按节点存档，返工先找问题在哪一层 | [long-video-workflow](skills/long-video-workflow/SKILL.md) | [ZIP](downloads/long-video-workflow.zip) |
| 生图摄影 | 把画面想法转成摄影语言，按需要生成静帧或关键帧 | [image-prompt](skills/image-prompt/SKILL.md) | [ZIP](downloads/image-prompt.zip) |
| AIGC 创作看片学习 | 设计镜头前问清表达，推荐供自己观看的参考片段，并讨论观众视点、信息揭示和镜头衔接 | [aigc-learning-skill](skills/aigc-learning-skill/SKILL.md) | [ZIP](downloads/aigc-learning-skill.zip) |
| 视频提示词 | 讨论演出和摄影，把已确定的设计写成视频提示词 | [video-prompt](skills/video-prompt/SKILL.md) | [ZIP](downloads/video-prompt.zip) |
| 分镜预览 | 文字分镜、SVG 构图明暗小样、预览图或草图预览，复杂空间交给白模做导演台预览 | [storyboard-preview](skills/storyboard-preview/SKILL.md) | [ZIP](downloads/storyboard-preview.zip) |
| 生图清单与核对 | 保存当前要求、逐项核对和管理图片版本 | [image-spec-check](skills/image-spec-check/SKILL.md) | [ZIP](downloads/image-spec-check.zip) |
| 白模动画 | 三维空间、人物路线、运镜、姿态与动作交接预演 | [white-model-animation](skills/white-model-animation/SKILL.md) | [ZIP](downloads/white-model-animation.zip) |
| 真实情绪表演 | 强情绪下的身体、声音、停顿、抢话、说不出口与双方反应 | [natural-emotional-performance](skills/natural-emotional-performance/SKILL.md) | [ZIP](downloads/natural-emotional-performance.zip) |
| 后期音效制作 | 按画面设计声音事件，分层生成或选取音效，再贴画混音 | [post-production-sound](skills/post-production-sound/SKILL.md) | [ZIP](downloads/post-production-sound.zip) |

[下载完整仓库](https://github.com/chipfighter/aigc-skills/archive/refs/heads/main.zip)

## 我的使用方式

先告诉 agent 我想表达什么，在对话中调整人物、表演和摄影，再根据需要使用对应技能。不必每次走完全部流程，也不必给普通镜头安排白模。

- 片子不止一场、要做一两分钟时，先用 `long-video-workflow` 定大方向和分场，再逐段交给 `storyboard-preview` 和 `video-prompt`，每段做完接上前面看。它写明了每一步要调用哪个技能。只有一场的短片段直接用下面的技能。

- 画面与静帧交给 `image-prompt`，具体细节配合 `image-spec-check`。
- 视频片段的设计与提示词交给 `video-prompt`。默认用全能参考：人物图、场景图，加上把镜头写清楚的提示词。关键帧只在三种情况下用：用户明确要求或已确认某张图必须是视频里指定时刻的画面；某一处必须稳定，而素材和文字锁不住（例如要露字）；生成后失败在关键帧能锁住的东西上，重新生成时再加。同一个片段的起点和终点都要对齐指定画面时，才用首尾帧。
- 设计镜头时，`storyboard-preview` 的镜头设计参考帮忙避开谁都会想到的拍法：从观众的感受出发，全片定一两条能检查的视觉规则，重点镜头先写常规拍法再写一个不同的，比较后再选。
- 需要先看机位、构图和节奏时，使用 `storyboard-preview`。能写出一条可以对图核对的布局要求，并且它会被后面继承、只靠文字明显会跑偏，或者已经失败过一次时，才用 SVG 构图小样；关键帧和场景图都按这个标准。
- 需要进一步设计强情绪下的真实感时，配合 `natural-emotional-performance`。
- 需要检验连续空间、严格路线、遮挡或动作交接时，使用 `white-model-animation`。
- 需要给分镜、粗剪或成片设计和制作后期音效时，使用 `post-production-sound`。同一个动作可以用几层声音，环境声和余响也可以跨镜头。

视频提示词和分镜预览的文件末尾有相关技能索引。

## 使用条件

技能是给 agent 的工作指引，实际能力取决于当前环境。生图需要可用的生图工具；图片核对与二维预览会用到文件读写及 ffmpeg；画线标注运镜路线用 Python 和 Pillow；实际制作白模动画需要可用的三维工具。生成音效和混音需要当前环境具备相应的音频工具。长片分场制作用 git 给项目里的文字文件存档。

使用支持技能加载的客户端时，按它的方式安装所需目录；ZIP 内保留技能目录和配套资料。没有技能加载功能的环境，也可以读取相关指令和资料，但不会因此自动获得工具能力。

本机的安装目录用目录链接（junction）指向本仓库的 `skills/`，改了仓库里的文件，Claude Code 和 Codex 下次加载技能时就会用上：

- Claude Code 使用 `~/.claude/skills/<技能>`。
- Codex 的 `image-spec-check` 使用 `~/.codex/skills/image-spec-check`，其余技能使用 `~/.agents/skills/<技能>`。

链接指向当前检出的分支，切到别的分支，本机加载的技能也跟着变。

## 迁移与维护约定

- 四个原技能以 2026-11-04 正在使用的本地版本为准，连同参考文件和已有配置原样收纳。
- `image-prompt`、`image-spec-check` 未改正文；`video-prompt`、`storyboard-preview` 只在末尾增加「相关技能」索引，原有内容完整保留。
- 2026-11-08：经确认修改 `video-prompt`、`storyboard-preview`、`image-prompt`、`natural-emotional-performance` 正文，补充按镜头角度补面部图、默认全能参考与首帧选择、表情起点和对白口型。
- 2026-11-09：《如梦令》试跑后经确认修改 `storyboard-preview`（预览画风默认和成片一致、写实预览先做设定图和场景图、两格竖版画布、表演强度、分镜表空间自查）、`video-prompt`（左右与路线、光线方向、运动方向、景别、看得见的情绪变化、不摆姿势的结尾拍、不稳处的动作、动作量、抽帧看片）和 `image-prompt`（新接口先试一张）。
- 2026-11-09：经确认修改 `video-prompt`，交付提示词前先附几行大白话的"这段会演出什么"。
- 2026-11-12：经确认修改 `storyboard-preview`：新增 `references/composition-sketch.md`（SVG 构图明暗小样：什么时候画、画什么不画什么、一张只讲一件事、画完自查、五种常用构图骨架、怎么附给生图模型和测试结论）；预览形式增加"草图预览"（用小样代替预览图剪视频）；"导演台预览"指三维灰模预演，交给 `white-model-animation`。
- 2026-11-13：同步 `video-prompt`、`storyboard-preview` 和 `image-prompt`。明确全能参考、关键帧和首尾帧的选用条件。只在构图必须准确时用 SVG 小样辅助出图。人物通常用正面照和遮挡面部的全身多视图，头部近景按镜头补充，所需角度可合在一张图中。
- 2026-11-13：同步本地最新版。视频提示词在动笔前先沟通演法，分镜补充人物处境、情绪和反应，移除未验证的提示词与江边分镜样例。构图骨架按当前镜头取用，走位按实际空间判断，预览配乐按已定声音设计处理。
- 2026-11-17：同步本机安装的最新版。`video-prompt` 新增 `references/model-pitfalls.md`（Seedance 2.5 / 可灵 4.0 易错点和看片检查清单），补充关键帧遮脸、连续运镜的镜内节点和摄影机对表演的响应；`storyboard-preview` 去掉预览视频（删除 `references/animatic.md`），预览形式改为预览图、草图预览和导演台预览；`image-spec-check` 补充逐人找手；`image-prompt` 补充关键帧遮脸。
- 2026-11-17：经确认统一两处冲突。`image-prompt` 未指定生图工具时先问用户，与 `storyboard-preview` 一致；`aigc-learning-skill` 对已聊过表达的镜头改为复述确认，并和其他技能要问的事合成一条消息。
- 2026-11-17：经确认把 `video-prompt` 易错点第 4 条从"模型的声音一律不用"收窄为只弃用模型自带的配乐和音效，对白按第 10 条处理。`post-production-sound` 以精确为准，回到最初的 32 行版，修正视频模型声音的用法，补充按频段叠层和干声生成。
- 2026-11-17：新增 `long-video-workflow`（长片分场制作）。先定大方向和每场要表达什么，再逐段设计、生成、接上前面检查；只管总纲、分场和改动记录三样文件，设计文档只留当前版，按节点用 git 存档；时长当预算；返工先找问题在哪一层，想改前面的先在当前段试，超出当前段的改动先列影响。经确认在 `aigc-learning-skill` 加一句：按长片分场流程分段制作时，表达按场对齐，镜头沿用本场表达。
- 2026-11-18：一次全自动制片测试后经确认修改。`long-video-workflow` 写明各步骤调用哪些技能（定全局决定前先调 `video-prompt` 和 `storyboard-preview`，进后期前调 `post-production-sound`），删去文末相关技能索引；全权授权时，留给用户判断的项不自己判通过，要停下交给用户的地方按建议的替代做法处理；广告、MV 按段落分段，视频按段提交；一页版也写出入场状态；项目单独一个文件夹，开始就建 git。`video-prompt` 关键帧改为三种情况，写明默认全能参考的原因（未量化验证）；参考图写成"第一帧和这张图一样"也算首帧；侧脸、背影为主的镜头补对应角度参考；补遮脸与平台审核的关系；全权授权时用进成片的片段按成功留档。`composition-sketch` 改为能写出可核对的布局要求才画小样，场景图也适用。`image-spec-check` 新增一次出一批图时的写法；全权授权时由用户判断的条目照样不判通过；清单外检查加服装上凭空多出的标志；布局类条目不通过可加小样。`post-production-sound` 自带音效核对后可留作一层，新增听不到时用频谱图和波形图核对，描述补上自己完整做片时触发。`model-pitfalls` 第 4、5 条同步。`storyboard-preview` 描述补上逐段制作时触发，全权授权时演出可直接写进提示词，关键帧条件统一指向 `video-prompt`。
- 2026-11-18：经确认在 `storyboard-preview` 新增 `references/shot-design.md`（镜头设计：从观众的感受出发；全片定一两条可对着镜头表检查的视觉规则；重点镜头先写常规拍法再写一个不同的；多做减法；出表前自查；用户给参考图或片名时的用法），场景概览加"视觉规则"一行。`long-video-workflow` 的全局决定加上全片的视觉规则，`video-prompt`、`aigc-learning-skill` 各加一句指向它。加入前用同一主题让两个子代理各做一次设计对比：有它的一组全片更统一，镜头更少更长；没有它的一组也不平庸。各只跑了一次。
- 2026-11-18：画幅不再默认横屏。`storyboard-preview` 分镜表要求按项目画幅设计构图，按发布平台给界面遮挡和字幕留位置；构图小样的画框和人物大小公式补上竖屏、方屏，骨架注明按 16:9 画；预览图的格子比例和版式补上方屏。`long-video-workflow` 定方向时问画幅。
- 2026-11-19：第二次全自动制片测试（《捡到一条龙》）后经确认修改，只改半自动协作时也会出问题的地方。`video-prompt` 的角度参考扩到反复出场的非人角色（背面、腹面、运动姿态、各体型阶段）。`long-video-workflow` 每段生成前的自查加一项：镜头会露出的头部角度、背面或运动姿态有没有对应参考；项目文件夹用英文或拼音命名，避免中文名字数相同的文件夹共用记忆。`image-spec-check` 清单外检查加上生物数腿、数趾。`shot-design` 加上"最强的手段只给最重要的一下"和"要速度感时"一节，出表前自查加字幕不替观众说感受、光线天气配乐不要每场推满。"视频模型会把写的高速做慢"只在一部片里见到，暂不写进易错点。
- 2026-11-22：经确认在 `video-prompt` 新增 `references/route-annotation.md`（画线标注运镜路线：在场景图副本上画带编号的摄影机路线，和原图一起作参考；什么时候用、怎么画、提示词要加的说明、看片检查和怎么积累结论）和 `scripts/draw_route.py`（用 Pillow 画路线，坐标可写比例），复杂运镜一条下加一句索引。做法来自第三方演示视频，演示没有对照，画线本身的作用未验证，文件开头写明。
- 2026-11-23：经确认补充 `route-annotation.md` 的"什么时候用"：画线介于文字和白模之间，画在真实场景图上，不用把粗模和场景图对齐；路线绕到东西背后、钻进被挡住的地方或朝镜头往回走时，平面上的线说不清楚，用文字写，绕人环绕也属于这一类。
- 2026-11-23：《墨》做后期时经确认修改 `post-production-sound`：「带画面复听」加一句，用户说剪辑点附近的声音怪时，先看是不是配乐的问题；配乐剪过的，把接缝前后的鼓点和原曲对一遍，再改音效和混音。这次配乐接缝多出一个鼓点，第一轮当成混音问题改，没改好。
- 旧 GitHub 上的 `image-spec-check` 比本地版旧；本次采用本地最新版，不将旧远端内容覆盖回来。
- 两个新技能采用已经确认的精简版，不依赖原教程视频运行。
- 之后维护四个原技能时，保留正文；需要与新技能衔接时只添加必要索引。若要改动正文，先明确提出具体修改。
- `skills/` 是内容来源。修改后运行 `scripts/package.py`，重新生成 `downloads/`，不手动维护另一份正文。
- 本地工作副本在 `D:\Study\wjj_projects\active\aigc-skills`，改动直接提交到 main 并推送，不开分支，不提 PR。也可以继续在 GitHub 网页上改，改完在本地 `git pull`。

本次归并的原仓库：`image-spec-check`、`storyboard-preview-skill`、`video-prompt-skill`、`image-prompt-skill`。

## 许可

[MIT License](LICENSE)
