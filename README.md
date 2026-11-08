# AIGC Skills

我自己的 AIGC 创作技能库：把想表达的画面、人物表演和镜头，逐步聊成可执行的设计、提示词与预演。

这里统一保存当前使用的技能，方便查看、维护和按需下载。以自己的实际工作方式为先；没有包装成 plugin，也没有为了平台通用性改写原有正文。

## 技能目录

| 技能 | 用途 | 内容 | 单独下载 |
|---|---|---|---|
| 生图摄影 | 把画面想法转成摄影语言，按需要生成静帧或关键帧 | [image-prompt](skills/image-prompt/SKILL.md) | [ZIP](downloads/image-prompt.zip) |
| 视频提示词 | 讨论演出和摄影，把已确定的设计写成视频提示词 | [video-prompt](skills/video-prompt/SKILL.md) | [ZIP](downloads/video-prompt.zip) |
| 分镜预览 | 文字分镜、预览图、带声音和运镜示意的预览视频 | [storyboard-preview](skills/storyboard-preview/SKILL.md) | [ZIP](downloads/storyboard-preview.zip) |
| 生图清单与核对 | 保存当前要求、逐项核对和管理图片版本 | [image-spec-check](skills/image-spec-check/SKILL.md) | [ZIP](downloads/image-spec-check.zip) |
| 白模动画 | 三维空间、人物路线、运镜、姿态与动作交接预演 | [white-model-animation](skills/white-model-animation/SKILL.md) | [ZIP](downloads/white-model-animation.zip) |
| 真实情绪表演 | 强情绪下的身体、声音、停顿、抢话、说不出口与双方反应 | [natural-emotional-performance](skills/natural-emotional-performance/SKILL.md) | [ZIP](downloads/natural-emotional-performance.zip) |

[下载完整仓库](https://github.com/chipfighter/aigc-skills/archive/refs/heads/main.zip)

## 我的使用方式

先告诉 agent 我想表达什么，在对话中调整人物、表演和摄影，再根据需要使用对应技能。不必每次走完全部流程，也不必给普通镜头安排白模。

- 画面与静帧交给 `image-prompt`，具体细节配合 `image-spec-check`。
- 视频片段的设计与提示词交给 `video-prompt`。
- 需要先看机位、构图和节奏时，使用 `storyboard-preview`。
- 需要进一步设计强情绪下的真实感时，配合 `natural-emotional-performance`。
- 需要检验连续空间、严格路线、遮挡或动作交接时，使用 `white-model-animation`。

这些技能保留原有协作关系。视频提示词和分镜预览的文件末尾，各有一小节指向两个新技能的索引。

## 使用条件

技能是给 agent 的工作指引，实际能力取决于当前环境。生图需要可用的生图工具；图片核对与二维预览会用到文件读写及 ffmpeg；实际制作白模动画需要可用的三维工具。

使用支持技能加载的客户端时，按它的方式安装所需目录；ZIP 内保留技能目录和配套资料。没有技能加载功能的环境，也可以读取相关指令和资料，但不会因此自动获得工具能力。

本仓库上传和维护不会自动覆盖本地安装的副本，本地更新另行安排。

## 迁移与维护约定

- 四个原技能以 2026-11-04 正在使用的本地版本为准，连同参考文件和已有配置原样收纳。
- `image-prompt`、`image-spec-check` 未改正文；`video-prompt`、`storyboard-preview` 只在末尾增加「相关技能」索引，原有内容完整保留。
- 2026-11-08：经确认修改 `video-prompt`、`storyboard-preview`、`image-prompt`、`natural-emotional-performance` 正文，补充按镜头角度补面部图、默认全能参考与首帧选择、表情起点和对白口型。
- 2026-11-09：《如梦令》试跑后经确认修改 `storyboard-preview`（预览画风默认和成片一致、写实预览先做设定图和场景图、两格竖版画布、表演强度、分镜表空间自查）、`video-prompt`（左右与路线、光线方向、运动方向、景别、看得见的情绪变化、不摆姿势的结尾拍、不稳处的动作、动作量、抽帧看片）和 `image-prompt`（新接口先试一张）。
- 旧 GitHub 上的 `image-spec-check` 比本地版旧；本次采用本地最新版，不将旧远端内容覆盖回来。
- 两个新技能采用已经确认的精简版，不依赖原教程视频运行。
- 之后维护四个原技能时，保留正文；需要与新技能衔接时只添加必要索引。若要改动正文，先明确提出具体修改。
- `skills/` 是内容来源。修改后运行 `scripts/package.py`，重新生成 `downloads/`，不手动维护另一份正文。
- GitHub 更新可以通过网页或接口完成，不要求本地 Git 命令。仓库仍保留 GitHub 的修改历史。

本次归并的原仓库：`image-spec-check`、`storyboard-preview-skill`、`video-prompt-skill`、`image-prompt-skill`。

## 许可

[MIT License](LICENSE)
