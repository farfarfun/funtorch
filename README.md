# funtorch

`funtorch` 是一个面向 PyTorch 工具链的轻量 Python 包，目前提供版本化的可导入包基础。

## 安装

```bash
uv add funtorch
```

## 最小示例

```python
import funtorch

print(funtorch.__version__)
```

## 开发

```bash
uv run ruff check --fix .
uv run ruff format .
uv run pytest
uv run funbuild install
```

发布统一通过 `funbuild` 的完整流水线：

```bash
uv run funbuild build
```

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
