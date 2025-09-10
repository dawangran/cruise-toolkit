
# cruise-toolkit

**cruise-toolkit** 是一个统一的 Python 工具包，整合了单细胞/时空转录组流程中的条码拆分、CB/UMI 校正、统计与比对等功能，  
并提供唯一的命令行入口 —— `cruise-toolkit`。  

该工具封装了原始的 `cruise.py` 流程脚本，保持参数兼容，便于在科研工作流中快速调用。

---

## 🔧 安装

从源码安装（开发模式）：

```bash
git clone https://github.com/<your-org>/cruise-toolkit.git
cd cruise-toolkit
pip install -e .
```

未来可直接通过 PyPI 安装：

```bash
pip install cruise-toolkit
```

---

## 🚀 快速开始

运行主流程（完全兼容你原来调用 `cruise.py` 的方式）：

```bash
cruise-toolkit \
  --bam input.bam \
  --fastqs fq1.fastq.gz,fq2.fastq.gz \
  --valid-cell valid.cell.tsv \
  --adapt CTACGATCCGACTTTCTGCG \
  --model BBBBBBBBBBCCTTCCBBBBBBBBBBCGATGUUUUUUUUUUTTTT \
  --threads 16 \
  --cb-tags CC,CB \
  --umi-tag UB \
  --outdir cruise_out
```

---

## 🖥️ CLI 用法

查看帮助：

```bash
cruise-toolkit -h
cruise-toolkit --help
```

这会展示 **`cruise.py` 的原生参数**，包括 `--bam`、`--fastqs`、`--adapt`、`--model`、`--cb-tags`、`--umi-tag` 等。  

全局参数（在任何命令前使用）：  
- `--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}`  
  设置日志级别（默认 INFO）  
- `--log-file run.log`  
  保存日志到文件  
- `--version`  
  查看版本号  

示例：  

```bash
cruise-toolkit --log-level DEBUG --log-file run.log \
  --bam input.bam --fastqs fq1.fq.gz,fq2.fq.gz --outdir cruise_out
```

---

## 📜 参数说明（常用）

| 参数 | 说明 |
|------|------|
| `--bam` | 输入 BAM 文件 |
| `--fastqs` | 输入 Fastq 文件，多个文件用逗号分隔 |
| `--valid-cell` | 有效的 cell barcode 列表 |
| `--adapt` | 接头序列 |
| `--model` | CB/UMI 模型字符串 |
| `--threads` | 线程数 |
| `--cb-tags` | cell barcode 标签（如 `CC,CB`） |
| `--umi-tag` | UMI 标签（如 `UB`） |
| `--outdir` | 输出目录 |
| `--keep-sample-tmp` / `--no-keep-sample-tmp` | 是否保留中间文件 |

> 所有参数的定义与原始 `cruise.py` 保持一致。  
> 你可以直接用 `cruise-toolkit --help` 查看完整参数列表。

---

## 📝 日志系统

所有运行都可以加上全局日志参数：  

```bash
cruise-toolkit --log-level INFO --log-file pipeline.log \
  --bam input.bam --fastqs fq1.fq.gz,fq2.fq.gz ...
```

日志会同时打印到终端，并写入 `pipeline.log` 文件。

---

## 🧪 开发与测试

```bash
# 安装依赖
pip install -e .[dev]

# 运行测试
pytest -q
```

---

## 👤 作者

- 相然 王 (<your_email@example.com>)

---

## 📄 License

MIT License
