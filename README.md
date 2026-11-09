# ai-design-director

An agent skill that makes AI-built designs stop looking AI-made. 中文说明见 [SKILL.md](SKILL.md)。

Three stages — **Discover → Define → Deliver** — and seven techniques:

1. Random seed strings to break the model's default taste
2. Bold, concrete creative briefs (with human taste in the loop)
3. An independent screenshot-only critic subagent that scores each iteration
4. Image generation instead of gradients and blobs
5. Video generation for animated elements and state transitions
6. Subtraction: cut what adds no value
7. A checklist of common "AI tells" to remove

## Install

Works with any agent that reads `SKILL.md` skills (Claude Code, Codex, and others):

```bash
git clone https://github.com/66666-design/ai-design-director ~/.claude/skills/ai-design-director
```

Or copy `SKILL.md` into your agent's skills / instructions folder.

## Credit

Inspired by Anshu Chimala, "How to turn your AI into a world-class designer", Lenny's Newsletter (2026-09-01):
https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world

This repository is an independent rewrite and extension; it does not reproduce the original article. Technique 7's checklist is our own.

## License

MIT
