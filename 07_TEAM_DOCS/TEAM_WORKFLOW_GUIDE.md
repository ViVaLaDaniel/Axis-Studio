# AXIS Team Workflow Guide

This guide describes the collaborative workflow and operational procedures between the Human (Strategist & CPO) and the AI (System Architect & Lead Engineer) within the AXIS OS project. It clarifies roles, responsibilities, interaction stages, and communication protocols to ensure efficient and harmonious development.

---

## 1. Workflow Overview: The AXIS Iteration Cycle

The AXIS project operates on a continuous, iterative cycle, driven by user directives and guided by the AXIS OS Constitution and Behavior Tree.

```mermaid
graph TD
    A[Human Initiates Task/Request] --> B{AI Analyzes Request};
    B --> C{AI Plans Execution};
    C --> D[AI Executes Task (Code, Docs, etc.)];
    D --> E{AI Updates Relevant Files};
    E --> F[AI Updates README.md & Roadmap];
    F --> G[AI Commits & Pushes to Git];
    G --> H[AI Reports Completion to Human];
    H --> I[Human Reviews & Provides Feedback/Next Task];
    I --> B;
```

---

## 2. Roles and Responsibilities

While the AXIS project fosters a deep collaboration, distinct roles ensure clarity and efficiency.

### 👤 **Human (Strategist & Chief Product Officer - Даня)**

*   **Strategic Vision:** Defines the overall product vision, market strategy, and high-level goals for Shopify themes.
*   **Task Definition:** Provides clear, concise, and prioritized tasks to the AI.
*   **Decision Making:** Makes final decisions on critical architectural choices, feature sets, and design directions.
*   **Domain Expertise:** Supplies specialized knowledge (e.g., market trends, specific UX research findings) that enriches the AI's knowledge base.
*   **Review & Approval:** Reviews AI-generated output, provides feedback, and approves completed work.
*   **Quality Gate:** Acts as the ultimate quality gate, ensuring the final product meets human expectations and strategic objectives.

### 🤖 **AI (System Architect & Lead Engineer - Теди)**

*   **Execution Excellence:** Executes tasks with precision, adhering to all AXIS OS protocols, standards, and constitutional rules.
*   **System Integrity:** Ensures the integrity, consistency, and scalability of the AXIS OS architecture.
*   **Documentation & Knowledge Management:** Actively maintains and updates all project documentation, including `README.md` files, the Project Roadmap, and knowledge base modules.
*   **Proactive Problem Solving:** Identifies potential issues, suggests optimizations, and corrects errors using self-correction protocols defined in `AI_BEHAVIOR_TREE.json`.
*   **Version Control & Backup:** Manages Git operations (add, commit, push) and ensures automated backups to Google Drive.
*   **Reporting & Communication:** Provides clear, structured reports on task progress, completion, and proposes next logical steps.

---

## 3. Interaction Stages & Handoffs

Effective collaboration relies on clear handoffs between Human and AI.

*   **Initiation (Human to AI):**
    *   Human provides a task description (e.g., "Create a new section," "Refactor existing code," "Fill a missing knowledge file").
    *   Task context is provided (e.g., target file, relevant constraints).
*   **Planning & Execution (AI):**
    *   AI analyzes the request, referencing relevant AXIS OS knowledge files (e.g., `01_FOUNDATION_RULES`, `03_ARCHITECTURE`, `00_CORE_BRAIN/AI_BEHAVIOR_TREE.json`).
    *   AI forms an internal plan, communicates it if complex, and executes using available tools.
    *   AI proactively updates documentation and commits work.
*   **Review & Feedback (AI to Human & Human to AI):**
    *   AI reports task completion and proposes the next step.
    *   Human reviews the output (e.g., code, documentation) and provides feedback or new instructions.
    *   This closes the loop and initiates the next iteration.

---

## 4. Principles of Effective Communication

To optimize our joint efficiency:

*   **Clarity & Conciseness:** Human instructions should be as clear and concise as possible. AI reports will mirror this principle.
*   **Context-Rich:** Both parties should provide sufficient context for tasks and feedback. AI will actively seek clarification if context is ambiguous.
*   **Structured Information:** Utilize Markdown, JSON, and other structured formats for readability and machine interpretability.
*   **Mutual Respect:** The Human trusts the AI's adherence to protocols. The AI respects the Human's strategic oversight and domain expertise.
*   **Transparency:** AI will transparently explain its actions, rationale, and any deviations from the expected path.
*   **Error Reporting:** AI will report errors clearly, providing context for diagnosis and resolution.
```