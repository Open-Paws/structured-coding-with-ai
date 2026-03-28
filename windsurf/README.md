# Windsurf Instruction Set

Configuration files for Windsurf (AI-powered code editor). All instruction files live in `.windsurf/rules/`.

## Structure

```
.windsurf/
  rules/                   # 14 markdown files with HTML comment trigger types
```

## How It Works

Each file in `.windsurf/rules/` starts with an HTML comment declaring its trigger type. Windsurf supports four trigger types:

- **Always On** (`<!-- trigger: always_on -->`) -- loaded into every conversation automatically
- **Model Decision** (`<!-- trigger: model_decision -->`) -- the model decides whether to load based on the current task
- **Glob** (`<!-- trigger: glob: pattern -->`) -- loaded when the active file matches the glob pattern
- **Manual** (`<!-- trigger: manual -->`) -- user invokes explicitly

### Character Limits

Windsurf enforces hard character limits: **6,000 characters per file** and a **12,000 character combined ceiling for all Always On rules**. The four Always On files in this set total approximately 8,500 characters, leaving headroom under the 12K ceiling. All 14 files are under the 6K per-file limit (largest is ~3,300 characters).

## Setup

Copy into your project root:

```bash
cp -r .windsurf your-project/
```

Review the trigger types in each file and adjust for your project. Note: Windsurf maintains persistent memories about your project. For sensitive advocacy work, review these memories regularly and clear any that contain investigation details, activist identities, or other sensitive data.
