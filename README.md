# AI智能伴侣

一个基于Streamlit和DeepSeek API的AI伴侣聊天应用。

## 功能特性

- 🤖 与AI伴侣进行实时聊天
- 💬 支持流式输出，打字机效果
- 📝 会话管理：新建、保存、加载、删除会话
- 🎭 自定义伴侣昵称和性格
- 💾 聊天记录本地保存

## 快速开始

### 方式一：运行完整版（需要DeepSeek API Key）

#### 1. 安装依赖

```bash
pip install -r requirements.txt
```

#### 2. 配置API Key

复制 `.env.example` 为 `.env`，并填入你的DeepSeek API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：
```
DEEPSEEK_API_KEY=你的API密钥
```

#### 3. 运行应用

```bash
streamlit run 03.AI_partner_1.py
```

### 方式二：运行Demo版（无需API Key）

直接运行Demo版本，体验模拟的AI伴侣对话：

```bash
streamlit run demo.py
```

应用将在浏览器中打开，默认地址：http://localhost:8501

## 使用说明

1. **新建会话**：点击侧边栏的"新建会话"按钮开始新对话
2. **自定义伴侣**：在侧边栏修改伴侣的昵称和性格
3. **会话管理**：可以加载历史会话或删除不需要的会话
4. **开始聊天**：在底部输入框输入消息，与AI伴侣对话

## 项目结构

```
ai-partner/
├── 03.AI_partner_1.py    # 主程序
├── requirements.txt      # 依赖列表
├── .env.example          # 环境变量示例
├── README.md             # 项目说明
└── resources/            # 资源文件目录（可选）
```

## 注意事项

- 需要有效的DeepSeek API Key
- 聊天记录保存在 `sessions/` 目录下
- 建议使用现代浏览器以获得最佳体验

## 许可证

MIT License