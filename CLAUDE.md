# Claude Code Instructions for Build Web, Guide AI

## Project Overview

This is a Quarto book teaching web development (HTML, CSS, JavaScript, WordPress, React) with AI collaboration as a core methodology. The book targets business students and emphasises professional judgment alongside technical skills.

## Key Principles

### Pedagogical Approach

1. **Concept before code** – Always explain the underlying concept using real-world analogies before showing syntax
2. **AI as exploration tool** – Include AI prompts that guide learners to discover patterns
3. **Business context** – Connect every technical concept to business value
4. **Progressive complexity** – Start simple, build incrementally
5. **Mental models over memorization** – Build understanding, not just syntax recall

### Writing Style

- Clear, direct prose
- Active voice
- Short paragraphs
- UK/Australian English spelling (colour, organisation, behaviour)
- No emojis unless specifically requested
- Technical accuracy without jargon overload

### Chapter Structure

Each chapter should follow this pattern:

```markdown
# Chapter Title {#sec-chapter-slug}

## The Concept First
[Real-world explanation without code]

## Understanding Through [Analogy]
[Business or everyday examples]

## Discovering [Concept] with Your AI Partner
### Exploration 1: [Prompt]
### Exploration 2: [Prompt]
[Guide learners through AI interactions]

## From Concept to Code
[Simplest possible implementation]

## Building Your Mental Model
[Diagrams, visualisations, multiple perspectives]

## Business Applications
[When and why this matters commercially]

## Practice Exercises
[Leveled exercises: Level 1-5]

## Chapter Summary
[Key takeaways as bullet points]

## Reflection
[Checklist of understanding]

## Your Learning Journal
[Prompts for journaling]

## Next Steps
[Bridge to next chapter]
```

### Exercise Levels

- **Level 1**: Direct application of examples
- **Level 2**: Minor modifications to examples
- **Level 3**: Combining concepts from chapter
- **Level 4**: Problem-solving requiring judgment
- **Level 5**: Open-ended design challenges

### Code Examples

- Keep examples minimal – show the concept, not production code
- Always include comments explaining the concept (not just what the code does)
- Use consistent naming conventions:
  - HTML: kebab-case for classes/IDs
  - CSS: kebab-case for classes
  - JavaScript: camelCase for variables/functions
  - React: PascalCase for components

### AI Prompt Examples

Include AI prompts in fenced code blocks:

```
Ask your AI:
Show me the simplest HTML that demonstrates semantic structure
```

### Callouts

Use Quarto callouts for:

- `.callout-tip` – Helpful hints
- `.callout-note` – Additional context
- `.callout-warning` – Common mistakes
- `.callout-important` – Critical information

### Unit Learning Outcomes (ULOs)

The book supports these technology-agnostic learning outcomes:

1. **Critically evaluate** and iteratively improve digital solutions
2. **Communicate effectively** with technical and non-technical stakeholders
3. **Translate stakeholder needs** into actionable technical requirements
4. **Make and defend technology choices** based on business context
5. **Assess emerging technologies** through systematic evaluation

Reference ULOs where relevant: "This develops ULO 4 – making and defending technology choices."

## File Organisation

```
web-dev-step-by-step-ai/
├── _quarto.yml           # Book configuration
├── index.qmd             # Preface
├── acknowledgments.qmd   # Thanks
├── chapter-XX-*.qmd      # Main chapters
├── projects/             # End-of-part projects
├── exercises/            # Additional exercises
├── assets/               # Images, CSS
├── templates/            # Starter code templates
└── notes/                # Development notes (not published)
```

## Development Workflow

1. **Draft in notes/** – Work out ideas before committing to chapters
2. **One chapter at a time** – Complete and review before moving on
3. **Test AI prompts** – Verify prompts produce useful outputs
4. **Cross-reference** – Link between chapters using `@sec-chapter-slug`

## Common Tasks

### Adding a new chapter

1. Create `chapter-XX-topic.qmd`
2. Add to `_quarto.yml` in appropriate part
3. Follow chapter structure template
4. Include AI exploration prompts
5. Add business context section
6. Create leveled exercises

### Building the book

```bash
quarto preview              # Live preview
quarto render               # Build HTML
quarto render --to pdf      # Build PDF (requires LaTeX)
```

## Quality Checklist

Before committing a chapter:

- [ ] Concept explained before code shown
- [ ] At least 2 AI exploration prompts included
- [ ] Business context section present
- [ ] Exercises at multiple levels (1-5)
- [ ] Reflection checklist included
- [ ] Links to previous/next chapters work
- [ ] Code examples tested and working
- [ ] UK/Australian spelling used
