---
name: updateAgentModeRules
description: Analyze conversation to update agent mode execution rules based on user expectations.
argument-hint: Specific focus area or issue pattern to address in the rules.
---
Analyze the current conversation critically to update the agent mode execution rules:

1. Review all user messages, especially those expressing frustration, dissatisfaction, or clarifying expectations
2. Identify patterns where the assistant:
   - Failed to take immediate action
   - Claimed to fix something without verifying
   - Asked unnecessary questions instead of acting
   - Misunderstood the user's true intent
3. Extract the core expectations and behaviors the user wants the assistant to follow
4. Update `.github/instructions/agent_mode_critical_execution.instructions.md` to:
   - Add new rules that address identified issues
   - Strengthen existing rules that were violated
   - Make instructions more proactive and actionable
   - Use clear, imperative language with concrete examples
5. Ensure the metadata uses correct format: `applyTo: "**"` to apply to all files
6. Verify the updated file follows the same structure as other instruction files in the project
7. Remove any outdated or redundant rules that don't align with user expectations

The goal is to make the instruction file capture real user expectations from actual interactions, not theoretical best practices.
