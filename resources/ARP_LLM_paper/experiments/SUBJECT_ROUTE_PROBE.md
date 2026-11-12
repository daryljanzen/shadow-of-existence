# Subject route: the isolation probe (2026-11-12)

No API key is available to this seat (`ANTHROPIC_API_KEY` is unset). The route is therefore fresh `claude -p` sessions launched from a neutral directory outside the repository. Each session uses:
- no setting sources and no MCP servers;
- no tools and no session persistence;
- a one-line system prompt;
- the environment variables that carry extra CLAUDE.md directories and the account email removed.

```
cd /tmp/subj_<trial> && env -u CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD -u CLAUDE_ADDITIONAL_DIRECTORIES \
  -u CLAUDE_CODE_USER_EMAIL claude -p --setting-sources "" --strict-mcp-config --no-session-persistence \
  --tools "" --system-prompt "<one line>" --output-format json "<trial materials>"
```

## Probes (model `claude-opus-5-5`, 2026-11-12)

Each probe asked the subject to quote everything in its context other than the message, and to name any personal names, emails, or project or repository names it could see.

1. **From the scratchpad under this seat's session**
   - No repository file, CLAUDE.md, memory or programme instruction was present.
   - **The working-directory path contained the repository's name.**
   - So subjects must not run from there.
2. **From `/tmp/subj_probe`**
   - No repository file, CLAUDE.md, memory or programme content was present.
   - The path is neutral.
3. **What still reaches every subject, identically in every condition:**
   - the Agent SDK's fixed preamble ("You are a Claude agent, built on Anthropic's Claude Agent SDK"), the environment block, the model name and the date;
   - **the account owner's email** as user context, injected by the account and not removable through the environment;
   - a commit-attribution reminder naming a session URL.
4. **Cost of one realistic trial** (a 4.2k-token input with a 0.7k-token answer): 12 s wall, 10.5 s API, $0.047 at list price.

**Reading.** The route meets the order's condition: no repository files, no CLAUDE.md, no memory, and nothing from the programme's content. What leaks is identity (an email and a session link), the same in every condition, and carries none of the programme. It is recorded here, and with every trial, rather than hidden. An API key would remove it entirely.
