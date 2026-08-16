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
| Binge | 0.5.5 | UI | Instagram 风格社交与发现层（汉化版） | [binge-cn](https://github.com/k6cc/binge-cn) |
| nfoSceneParser | 1.6.1 | Python + UI | 从 NFO 或文件名模式填充场景数据 | [nfoSceneParser-jav](https://github.com/k6cc/nfoSceneParser-jav) |
| Scene Translate | 2.6.4 | Python + UI | 场景/图片/图库编辑页一键翻译 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| sceneGallerySync | 1.6.0 | Python + UI | 自动创建图库并关联影片 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |
| Studio Tools | 1.0.0 | UI | 工作室合并与 StashDB 搜索 | [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) |

## 安装方法

1. 在 Stash 中添加上方插件源 URL
2. 从可用插件列表中选择需要的插件点击安装
3. 安装完成后重新加载插件（`设置 > 插件 > 重新加载`）

## 前置依赖

### UI 插件（无需 Python）

- Binge
- Studio Tools

### Python 插件（需 Python 3.x）

- nfoSceneParser（需 `requests`）
- Scene Translate（仅标准库，无需 pip 安装）
- sceneGallerySync（仅标准库，无需 pip 安装）

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

nfoSceneParser 额外需要 `requests`：

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
| [stash-jav-tools](https://github.com/k6cc/stash-jav-tools) | sceneTranslate + sceneGallerySync + studioTools 源码 + Release |

## License

各插件的 License 见对应源码仓库。