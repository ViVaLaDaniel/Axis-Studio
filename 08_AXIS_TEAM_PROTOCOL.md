# AXIS STUDIOS: TEAM COLLABORATION PROTOCOL v2.0 (OMEGA PATCH)
OBJECTIVE: Standardize workflows for scalable teams (1-10 developers) with strict handoff formats.

🎭 ROLES & RESPONSIBILITIES
RoleFocusPrimary OutputSecondary OutputToolsStrategist (CPO)Market analysis, "Killer Features"CONCEPT_SPEC.jsonCompetitive Analysis ReportGoogle Trends, Brain, File 02ArchitectStructure, Data schema, DependenciesSCHEMA_SKELETON.json + DEPENDENCY.mdArchitecture Decision RecordVS Code, File 00, File 09DeveloperLiquid, JS, CSS ImplementationWorking Code (PR)Unit Tests (optional)Shopify CLI, Git, File 03QA EngineerValidation, Testing, SecurityQA_REPORT.md + Bug TicketsPerformance ReportReal Devices, Lighthouse, File 05/07

📦 HANDOFF ARTIFACTS (STRICT FORMAT)
1. STRATEGY → ARCHITECT
Input: Verbal brief or User Story
Deliverable: CONCEPT_SPEC.json
```json
{
  "theme_name": "Luxe Perfume",
  "target_niche": "Luxury D2C Perfume Brands",
  "target_audience": {
    "age_range": "25-45",
    "avg_order_value": "$80-$150",
    "psychographics": ["Quality-conscious", "Story-driven buyers"]
  },
  "killer_feature": {
    "name": "Scent Story Video Grid",
    "description": "Each perfume has a 10-second vertical video showcasing its 'story'",
    "conversion_goal": "Increase Time on Site by 20%, AOV by 15%"
  },
  "must_have_sections": [
    "Video Hero with Scent Selector",
    "Bento Grid Collection (Video-first)",
    "Ingredient Story Accordion",
    "Scent Quiz (Interactive)"
  ],
  "technical_requirements": {
    "autoplay": true,
    "muted": true,
    "aspect_ratios": ["9:16", "1:1"],
    "max_videos_per_section": 6,
    "performance_target": "LCP < 1.2s"
  },
  "vibe": "Luxury + Modern (Think: Aesop meets Instagram)",
  "reference_sites": [
    "https://www.aesop.com",
    "https://www.loewe.com/usa/en/home"
  ]
}
```
Architect Checklist:

- All technical requirements are implementable with Axis Stack (File 00)
- Killer Feature passes Feasibility Check (File 06b)
- Performance targets are realistic (File 15)


2. ARCHITECT → DEVELOPER
Input: CONCEPT_SPEC.json
Deliverable: SCHEMA_SKELETON.json + DEPENDENCY.md
Example: `schemas/video-scent-grid-skeleton.json`
```json
{
  "section_name": "video-scent-grid",
  "file_path": "sections/video-scent-grid.liquid",
  "dependencies": {
    "snippets": ["video-player.liquid", "product-card-compact.liquid"],
    "assets": ["component-video-grid.css", "component-video-grid.js"],
    "external": ["None"]
  },
  "schema_structure": {
    "settings": [
      {
        "type": "header",
        "content": "Content"
      },
      {
        "type": "text",
        "id": "heading",
        "label": "Heading",
        "default": "Discover Your Scent"
      },
      {
        "type": "range",
        "id": "videos_per_row",
        "label": "Videos per Row (Desktop)",
        "min": 2,
        "max": 4,
        "step": 1,
        "default": 3
      }
    ],
    "blocks": [
      {
        "type": "video_item",
        "name": "Video Item",
        "settings": [
          {
            "type": "video",
            "id": "video_file",
            "label": "Video File"
          },
          {
            "type": "product",
            "id": "linked_product",
            "label": "Linked Product"
          },
          {
            "type": "checkbox",
            "id": "autoplay",
            "label": "Autoplay",
            "default": true
          }
        ]
      }
    ],
    "presets": [
      {
        "name": "Video Scent Grid",
        "blocks": [
          {"type": "video_item"},
          {"type": "video_item"},
          {"type": "video_item"}
        ]
      }
    ]
  },
  "performance_constraints": {
    "max_video_weight": "2MB per video",
    "max_blocks": 6,
    "lazy_load": "All videos except first"
  },
  "accessibility_requirements": [
    "Keyboard navigation for video controls",
    "ARIA labels for play/pause buttons",
    "prefers-reduced-motion: disable autoplay"
  ]
}
```
Example: `DEPENDENCY.md`
```markdown
# Video Scent Grid - Dependency Map

## Direct Dependencies
- `snippets/video-player.liquid` (NEW - must create)
- `snippets/product-card-compact.liquid` (EXISTS)
- `assets/component-video-grid.css` (NEW - must create)
- `assets/component-video-grid.js` (NEW - must create)

## Indirect Dependencies
- `assets/base.css` (for CSS variables)
- `assets/global.js` (for IntersectionObserver polyfill if needed)

## External Dependencies
- NONE

## Impact Score
- **Conversion Impact:** HIGH (Killer Feature)
- **Performance Risk:** MEDIUM (Video weight management needed)
- **Complexity:** MEDIUM (Web Components + Lazy Loading)

## Breaking Changes
- If `video-player.liquid` is modified, this section breaks.
```
Developer Checklist:

- Skeleton is valid JSON (no comments, no trailing commas)
- All dependencies are documented
- Performance constraints are clear
- Accessibility requirements are explicit


3. DEVELOPER → QA
Input: Pull Request (PR) with code
Deliverable: QA_REPORT.md
Pre-QA Requirements (Automated):

- ✅ CI Tests (File 07) must be GREEN
- ✅ Theme Check passes with 0 errors
- ✅ Lighthouse score > 90
- ✅ Security Scan (File 11) shows no CRITICAL issues

Example: `QA_REPORT.md`
```markdown
# QA Report: Video Scent Grid Section
**Date:** 2025-11-23  
**Tester:** QA Engineer Name  
**PR:** #142  
**Status:** ⚠️ ISSUES FOUND (2 High, 1 Medium)

## Test Environment
- **Device:** iPhone 14 Pro (iOS 17), MacBook Pro (Safari 17)
- **Theme Version:** v1.2.0-beta

## Test Results

### ✅ PASSED (7/10)
1. **Desktop Layout:** Grid displays correctly at 1920px
2. **Mobile Layout:** Videos stack vertically on < 768px
3. **Autoplay:** Videos autoplay when muted
4. **Lazy Loading:** Videos below fold load on scroll
5. **Keyboard Nav:** Tab key navigates through video controls
6. **Schema Settings:** All settings in Theme Editor work as expected
7. **Performance:** Lighthouse score = 94

### ❌ FAILED (3/10)

#### **HIGH: Videos don't play on Safari iOS**
- **Steps to Reproduce:**
  1. Open Product Page on iPhone Safari
  2. Scroll to Video Grid section
  3. Videos show black screen, don't autoplay
- **Expected:** Videos autoplay (muted)
- **Actual:** Videos don't play at all
- **Root Cause:** Missing `playsinline` attribute on `<video>` tag
- **Fix Required:** Add `playsinline` to video tag in `video-player.liquid`

#### **HIGH: Sticky ATC overlaps video controls**
- **Steps to Reproduce:**
  1. Open Product Page on mobile
  2. Scroll to Video Grid
  3. Try to pause video
- **Expected:** Can click pause button
- **Actual:** Sticky ATC bar blocks button (z-index conflict)
- **Fix Required:** Adjust Sticky ATC z-index or add bottom padding to section

#### **MEDIUM: Long product titles break layout**
- **Steps to Reproduce:**
  1. Add video with product title "The Ultimate Luxurious Perfume Collection for Spring 2025"
  2. View on mobile
- **Expected:** Text truncates with ellipsis
- **Actual:** Text wraps, pushes CTA button off-screen
- **Fix Required:** Add `text-overflow: ellipsis` and `max-width` to product title

## Performance Metrics
- **LCP:** 1.1s ✅
- **CLS:** 0.05 ✅
- **FID:** 45ms ✅
- **Bundle Size:** JS 12KB, CSS 8KB ✅

## Security
- **XSS Check:** ✅ All user inputs escaped
- **CSRF Check:** ✅ N/A (no forms)

## Recommendations
1. Fix Safari iOS issue ASAP (BLOCKER for launch)
2. Test on Android devices (Samsung, Pixel)
3. Add unit tests for z-index hierarchy

**Next Steps:** Developer to fix HIGH issues, re-submit for QA Round 2.
```

🚨 EMERGENCY PROTOCOL (RED BUTTON)
Scenario: Critical Bug on Live Site
Example: "Cart Drawer not opening after Black Friday deployment"
Step 1: IMMEDIATE ROLLBACK (< 5 minutes)
```bash
# On local machine
git log --oneline  # Find last stable commit
git revert HEAD    # Revert latest commit
git push origin main

# On Shopify CLI
shopify theme push --theme=LIVE_THEME_ID
```

**Slack Alert Template:**
```
🚨 RED BUTTON ACTIVATED 🚨
Issue: Cart Drawer broken on Live Site
Action: Reverted to commit abc123f (v1.1.5)
Impact: 0 customer-facing features lost
Next: Debug locally, hotfix in 2 hours
Responsible: @developer-name
```

Step 2: ISOLATE & REPRODUCE (< 30 minutes)
```bash
# Create hotfix branch
git checkout -b hotfix/cart-drawer-emergency

# Run theme locally
shopify theme dev --store=YOUR_STORE.myshopify.com

# Test in isolation
# Check browser console for errors
# Check File 18 (Memory Log) for similar past bugs
```

Step 3: FIX & FAST-TRACK QA (< 1 hour)
Hotfix Protocol:

- Skip full QA (File 05)
- Run ONLY critical tests:
  - Does cart open?
  - Can items be added/removed?
  - Does checkout work?
- Security Scan (File 11) - MANDATORY
- Performance Check (File 15) - Skip if no asset changes

```bash
# Commit fix
git commit -m "hotfix(cart): fix drawer not opening on iOS Safari (M087)"

# Push to production
git push origin hotfix/cart-drawer-emergency
shopify theme push --theme=LIVE_THEME_ID
```

Step 4: POST-MORTEM (< 24 hours)
Template: `POSTMORTEM_2025-11-23.md`
```markdown
# Post-Mortem: Cart Drawer Failure (Nov 23, 2025)

## Incident Summary
- **Time:** 2025-11-23 14:00 UTC
- **Duration:** 37 minutes downtime
- **Impact:** ~200 users affected, 5 lost checkouts
- **Root Cause:** Missing `open` attribute in cart-drawer.liquid after refactor

## Timeline
- 14:00 - Deployment v1.2.0 goes live
- 14:12 - First customer report via chat
- 14:15 - Engineering alerted
- 14:20 - Rollback initiated
- 14:25 - Rollback complete (Live site working)
- 14:37 - Hotfix deployed

## Root Cause Analysis
- **What Happened:** Developer removed `open` attribute during code cleanup
- **Why CI Didn't Catch It:** Visual Regression tests were disabled (performance optimization)
- **File Conflict:** None (human error)

## Action Items
1. ✅ Re-enable Visual Regression in CI (File 07) - DONE
2. ✅ Add Memory Log entry (M087) - DONE
3. ⏳ Add unit test for cart-drawer open state - IN PROGRESS
4. ⏳ Document "never remove ARIA attributes without review" in File 00 - IN PROGRESS

## Lessons Learned
- **DON'T:** Disable tests for "performance optimization"
- **DO:** Always run full QA on cart/checkout features
- **Prevention:** Add pre-commit hook to check for removed ARIA attributes
```

---

## 🔄 DAILY STANDUP FORMAT

**Time:** 9:00 AM (15 minutes MAX)

**Each team member answers:**
1. **Yesterday:** What did I complete?
2. **Today:** What am I working on?
3. **Blockers:** What's stopping me?

**Example:**
```
Developer A:
  Yesterday: Completed Video Grid section
  Today: Fix Safari iOS bug from QA
  Blockers: Need design approval for mobile layout

Strategist:
  Yesterday: Researched beauty industry trends
  Today: Define concept for "Gift Finder Quiz"
  Blockers: None
```

📊 WEEKLY METRICS REVIEW
Every Friday 4:00 PM
Metrics to Review:

- Velocity: How many sections shipped this week?
- Quality: QA pass rate (target: >80% first-time)
- Performance: Average Lighthouse score across all sections
- Memory Log: New mistakes logged (target: <3 per week)
- Client Satisfaction: Any complaints or feature requests?

Action Items:

- If QA pass rate < 80%: More peer reviews needed
- If mistakes > 5/week: Training session on File 11 (Security)


🤝 CONFLICT RESOLUTION
Scenario 1: Design vs Performance
Example: Designer wants 4K hero video (20MB)
Resolution Process:

1. Check File 01b (Priority Rules): Performance > Design
2. Architect proposes alternative: 1080p video (2MB) with lazy-loaded 4K option
3. Designer approves or escalates to CPO
4. CPO makes final call (usually sides with performance per File 01b)


Scenario 2: Developer disagrees with Architecture
Example: Developer thinks Schema is too complex
Resolution Process:

1. Developer documents concern in PR comments
2. Architect reviews and either:
   - Simplifies schema, OR
   - Explains why complexity is necessary (File 09 dependency reasons)
3. If still unresolved: QA Engineer mediates (user experience perspective)
4. Final escalation: CPO decides

Rule: Architecture decisions are NOT democratic. Architect has final say (unless overruled by CPO).

📱 COMMUNICATION CHANNELS
ChannelPurposeResponse TimeSlack #axis-devDaily updates, quick questions< 2 hoursSlack #axis-urgentBugs, blockers, emergencies< 15 minutesGitHub PR CommentsCode review, technical discussion< 24 hoursEmailWeekly reports, client communication< 48 hoursZoomWeekly standup, post-mortemsScheduled

🎓 ONBOARDING NEW TEAM MEMBERS
Day 1: System Familiarization

- Read File 00 (Tech Rules)
- Read File 01 (Design System)
- Read File 03 (Master System)
- Read THIS FILE (Team Protocol)

Day 2-3: Guided Practice

- Shadow a Developer on simple section creation
- Review 3 past PRs to understand code style
- Run QA checklist (File 05) on staging theme

Day 4-5: First Task

- Assigned: Create a "Testimonial Slider" section
- Architect provides skeleton
- Peer review before QA

Week 2: Full Autonomy

- Can work on sections independently
- Attends all standups and reviews
- Added to on-call rotation (for emergencies)


✅ DEFINITION OF DONE
A task is "Done" when:

- ✅ Code is merged to main branch
- ✅ QA Report shows 0 CRITICAL or HIGH issues
- ✅ Documentation (File 04) is generated
- ✅ Memory Log (File 18) is updated if bugs were found
- ✅ Performance Budget (File 15) is not exceeded
- ✅ Client/Stakeholder approves (if applicable)

NOT Done:

- ❌ "Works on my machine"
- ❌ "QA can test later"
- ❌ "I'll document it tomorrow"


VERSION: 2.0 (OMEGA PATCH)
LAST UPDATED: 2025-11-23
MAINTAINED BY: Team Lead + CPO