# B2B Python版

#### 灵感来源:[B2B原版](https://github.com/dd-center/B2B)

### 特性

- 支持原版B2B的所有功能
- 能够在浏览器中直接播放直播

### 使用

- 安装依赖 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask requests` ;
- 运行B2B Python `python main.py [--port PORT]` ;
- 在播放器中输入 `http://127.0.0.1:[PORT(默认为5000)]/[房间号]` 播放直播;
- 或者在浏览器中输入 `http://127.0.0.1:[PORT(默认为5000)]/player/[房间号]` 在浏览器中播放直播;
- 以上两种方法都支持选择播放源，在URL后加上 `?source=[SOURCE]` 即可.