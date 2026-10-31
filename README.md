# stash-plugins

Stash 插件源（Plugin Source Index）— 通过 GitHub Pages 提供 Stash 插件索引。

## 插件源 URL

在 **Stash → 设置 → 插件 → 可用插件 → 添加源** 中添加：

```
https://k6cc.github.io/stash-plugins/plugins/main/index.yml
```

> **备用（raw URL，无需启用 Pages）**：
> ```
> https://raw.githubusercontent.com/k6cc/stash-plugins/main/plugins/main/index.yml
> ```

## 包含的插件

| 插件 | 版本 | 类型 | 说明 | 源码仓库 |
|------|------|------|------|---------|
| Binge | 0.10.9 | 纯 UI | Instagram 风格社交与发现层（汉化版） | [binge-cn](https://github.com/k6cc/binge-cn) |
| nfoSceneParser | 1.7.0 | 纯后台 | 从 NFO 或文件名模式填充场景数据 | [nfoSceneParser-jav](https://github.com/k6cc/nfoSceneParser-jav) |
| Scene Translate | 2.9.4 | Python + UI | 场景/图片/图库编辑页一键翻译 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| sceneGallerySync | 1.9.8 | Python + UI | 自动创建图库并关联影片 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Studio Tools | 1.5.10 | 纯 UI | 工作室合并与 StashDB 搜索 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| JavStashLinker | 1.5.11 | Python + UI | 批量匹配 JAVStash 演员 ID | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Performer Merge | 1.6.7 | 纯 UI | 重名演员检测与合并（需 Stash v0.31.0+） | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Tag Merge | 2.7.6 | 纯 UI | 按映射库合并相似 tags | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Tag Merge Auto | 1.2.5 | 纯后台 | 后台自动合并 tags（钩子 + 全库扫描） | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Studio Tools Auto | 1.1.3 | 纯后台 | 后台自动整理工作室（钩子 + 存量扫描） | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Scene Translate Auto | 1.3.1 | 纯后台 | 后台自动翻译场景标题/简介（钩子 + 存量扫描） | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Javstash Autofill+ | 1.3.2 | 纯后台 | 新演员按名刮削 JAVStash 补全+stash_id；新场景按 oshash 补空白字段+stash_id；存量回填 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| O Stats I18n | 2.2.0-3 | Python + UI | 统计页 O 统计与观看时长追踪（O Stats 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| Lockdown I18n | 2.20.0-1 | 纯 UI | 把 Stash 锁定在演员/工作室/标签上直到脱身（Lockdown 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| Insights I18n | 2.14.1-1 | 纯 UI | 统计页数据仪表盘：你/操作/库/文件与画质/元数据健康/收藏（Insights 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| Ascension I18n | 1.4.1-4 | Python + UI | 演员与场景的评级/分档系统（Ascension 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| Xenith I18n | 3.2.1 | Python + UI | 演员与场景的 Elo 对决评分与排行榜（Xenith 多语言重构，中文名「争锋」，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| stashDiscover | 2.6.5 | Python + UI | 演员页「发现」标签：从 stash-box 实例发现本地未拥有的场景，加入库 / Jackett 搜索资源 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| ImageMetaSync | 1.0.2 | 纯后台 | 把场景元数据（演员/工作室/日期/tag/标题/番号）回填到图库图片（封面/fanart/剧照），多演员/无演员图库跳过 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Collapsable Plugin Settings I18n | 0.10.7-1 | 纯 UI | 「设置 → 插件」与「设置 → 任务 → 插件任务」的插件分组可折叠/可搜索/可排序，并可用滑块代替启用/禁用按钮（Collapsable Plugin Settings 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| O Cheevs I18n | 0.3.0-1 | Python + UI | 成就系统：观看时长 / O 数 / 观看视频数三类成就，分普通至传说五档，达成弹提示，含独立成就页面与顶栏奖杯入口（O Cheevs 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |
| Tasks Toolkit I18n | 0.6.4-1 | Python + UI | 把 Stash 自己的任务与各工具包的只读扫描集中到一处：Autopilot 自动巡检、安全队列、定时例程与调度器、任务查看与历史（Tasks Toolkit 多语言重构，中文/英文跟随 Stash 界面语言） | [stash-i18n](https://github.com/k6cc/stash-i18n) |

## 安装方法

1. 在 Stash 中添加上方插件源 URL
2. 从可用插件列表中选择需要的插件点击安装
3. 安装完成后重新加载插件（`设置 > 插件 > 重新加载`）

## 前置依赖

### 纯 UI 插件（无需 Python）

- Binge
- Studio Tools
- Performer Merge
- Tag Merge
- Lockdown I18n
- Insights I18n
- Collapsable Plugin Settings I18n

### Python 插件（需 Python 3.x）

- nfoSceneParser（需 `requests`）
- Scene Translate（需 `requests`）
- sceneGallerySync（需 `requests`）
- JavStashLinker（需 `requests`）
- Tag Merge Auto（仅标准库，无需 pip 安装）
- Studio Tools Auto（仅标准库，无需 pip 安装）
- Scene Translate Auto（仅标准库，无需 pip 安装）
- Javstash Autofill+（仅标准库，无需 pip 安装）
- O Stats I18n（仅标准库，无需 pip 安装）
- O Cheevs I18n（仅标准库，无需 pip 安装）
- Tasks Toolkit I18n（仅标准库，无需 pip 安装）
- Ascension I18n（需 `requests`）
- Xenith I18n（需 `stashapp-tools`，见插件内 requirements.txt）
- stashDiscover（仅标准库，无需 pip 安装；需已配置 stash-box 实例，Jackett/qBittorrent 可选）
- ImageMetaSync（需 `requests`）

**Docker 部署**：Stash 官方镜像已预装 Python。

**Windows / macOS 裸机部署**：

```powershell
python --version                  # 验证 Python
```

若报错：

```powershell
winget install Python.Python.3.12  # Windows
brew install python@3.12           # macOS
```

需要 `requests` 的插件（nfoSceneParser、Scene Translate、sceneGallerySync、JavStashLinker、Ascension I18n、ImageMetaSync）：

```powershell
pip install requests
```

## 仓库结构

```
stash-plugins/
└── plugins/
    └── main/
        └── index.yml    # 插件索引文件
```

## GitHub Pages

本仓库启用了 GitHub Pages，分支 `main` / `(root)`。访问以下 URL 获取插件索引：

```
https://k6cc.github.io/stash-plugins/plugins/main/index.yml
```

## 相关仓库

| 仓库 | 说明 |
|------|------|
| [binge-cn](https://github.com/k6cc/binge-cn) | Binge 插件源码 + Release |
| [nfoSceneParser-jav](https://github.com/k6cc/nfoSceneParser-jav) | nfoSceneParser 插件源码 + Release |
| [stash-i18n](https://github.com/k6cc/stash-i18n) | 第三方插件汉化版（i18n）源码 + Release |
| [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) | sceneTranslate + sceneGallerySync + studioTools + JavStashLinker + performerMerge + tagMerge + Auto 系列 + sceneTranslateAuto + javstashAutofill+ + stashDiscover + ImageMetaSync 源码 + Release |

## License

各插件的 License 见对应源码仓库。