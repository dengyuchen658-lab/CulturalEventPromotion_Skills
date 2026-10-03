# 运行工作区

Skill 本体只存规则、脚本、模板和测试。每个实际海报项目在 Skill 目录之外创建独立工作区：

```text
work/<project-id>/
├── input/          # 原始资料，只读保留
├── extracted/      # OCR、文本、表格和素材索引
├── state/          # brief.yaml、分类和概念状态
├── drafts/         # 主视觉和排版候选
├── output/         # 通过 QA 的交付文件
└── reports/        # manifest、交付清单、质量报告和迭代记录
```

## 建议文件

- `reports/input-manifest.json`
- `state/brief.yaml`
- `state/prompt-plan.yaml`
- `reports/delivery-manifest.yaml`
- `reports/quality-report.md`

## 版本与保留

原始输入不覆盖；提取结果可重建；已批准概念和正式输出采用递增版本号。完全重做可清除视觉锁定，但保留已确认事实和有效文化证据。

运行产物、缓存和临时预览不提交到 Skill 仓库。课程统一测试任务和 LaTeX 模板发布后，可在 `tests/course-benchmark/` 和相应报告目录扩展，不修改通用工作流。

