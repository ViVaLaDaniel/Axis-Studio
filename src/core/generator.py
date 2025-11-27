"""
Theme Generator Module for AXIS Studio.

Autonomous generation of Shopify themes with:
- CRO pattern analysis
- Competitor intelligence integration
- Best practices from top themes
- Interactive path selection
"""

import os
import json
import logging
from typing import Dict, Any, List, Optional

from src.core.context import AxisContext
from src.adapters.llm_provider import LLMProvider, LLMProviderFactory
from src.orchestrator import AxisOrchestrator


class ThemeGenerator:
    """
    Autonomous Theme Factory with CRO optimization.
    
    Process:
    1. Analyze brief (extract niche, archet type)
    2. Load best practices from competitors
    3. Select CRO patterns
    4. Ask user for output path
    5. Generate theme with optimization
    """
    
    def __init__(self, provider_name: str = 'gemini_browser'):
        self.logger = logging.getLogger("ThemeGenerator")
        self.context = AxisContext()
        self.context.load_brain()
        
        self.orchestrator = AxisOrchestrator()
        
        self.logger.info(f"Initializing LLM Provider: {provider_name}")
        self.provider = LLMProviderFactory.create(provider_name)
        
        # Load Brain modules
        self._load_brain_modules()
            
    def _load_brain_modules(self):
        """Load ALL knowledge databases (CRO, design, psychology, retention, copy)."""
        brain = self.context.brain
        
        # Original knowledge bases
        self.cro_patterns = brain.get("AXIS_CRO_PATTERNS", {})
        self.cro_scientist = brain.get("25_AXIS_CRO_SCIENTIST", {})
        self.competitor_intel = brain.get("24_AXIS_COMPETITOR_INTEL", {})
        self.theme_blueprint = brain.get("AI_THEME_BLUEPRINT", {})
        
        # NEW: Comprehensive knowledge system
        self.design_patterns_schema = brain.get("DESIGN_PATTERNS_SCHEMA", {})
        self.psychology_db = brain.get("PSYCHOLOGY_DB", {})
        self.retention_db = brain.get("RETENTION_DB", {})
        self.copywriting_db = brain.get("COPYWRITING_DB", {})
        
        # Theme-specific databases
        self.theme_db_dawn = brain.get("THEME_DB_DAWN", {})
        self.theme_db_impact = brain.get("THEME_DB_IMPACT", {})
        
        self.logger.info(f"Loaded 9 knowledge databases: CRO, Design, Psychology, Retention, Copywriting, Theme DBs")
        
    def generate_theme(self, brief: str, theme_name: str):
        """
        Generate a full theme based on the brief.
        
        Workflow:
        1. Analyze niche from brief
        2. Load best practices
        3. Ask user for output path
        4. Generate optimized theme
        """
        self.logger.info(f"🚀 Starting Theme Generation: '{theme_name}'")
        self.logger.info(f"📝 Brief: {brief}")
        
        # Step 1: Analyze brief → extract niche
        niche = self._analyze_niche(brief)
        self.logger.info(f"🔍 Detected niche: {niche}")
        
        # Step 2: Load best practices
        best_practices = self._get_best_practices(niche)
        self.logger.info(f"📚 Loaded best practices from: {', '.join(best_practices.get('competitor_themes', []))}")
        
        # Step 3: Select CRO patterns
        cro_plan = self._select_cro_patterns(niche, brief)
        self.logger.info(f"🎯 CRO patterns: {', '.join(cro_plan.get('patterns', []))}")
        
        # Step 4: Ask user for output path
        theme_root = self._ask_output_path(theme_name)
        
        # Step 5: Login if needed
        if hasattr(self.provider, 'login'):
            print("🔐 Logging in to LLM Provider...")
            self.provider.login()
            
        # Step 6: Generate theme files
        self._generate_shopify_theme(theme_root, theme_name, brief, niche, cro_plan, best_practices)
        
        self.logger.info(f"✅ Theme Generation Complete: {theme_root}")
        
        # Generate CRO report
        self._generate_cro_report(theme_root, niche, cro_plan)
        
        if hasattr(self.provider, 'close'):
            self.provider.close()
    
    def _analyze_niche(self, brief: str) -> str:
        """
        Extract niche from brief using LLM.
        
        Examples:
        - "VIP theme for luxury watches" → "luxury watches"
        - "Modern furniture store" → "furniture"
        """
        prompt = f"""
        Extract the product niche from this brief:
        "{brief}"
        
        Return ONLY the niche category (1-2 words). Examples:
        - "luxury watches"
        - "fashion apparel"
        - "furniture"
        - "wellness products"
        """
        
        try:
            niche = self.provider.generate(prompt).strip().lower()
            return niche
        except Exception as e:
            self.logger.warning(f"Niche extraction failed: {e}. Defaulting to 'general'")
            return "general"
    
    def _get_best_practices(self, niche: str) -> Dict[str, Any]:
        """
        Load best practices from competitor themes.
        
        Returns dict with:
        - competitor_themes: List of top themes to learn from
        - key_features: Features to include
        - avoid: Anti-patterns to avoid
        """
        intel = self.competitor_intel.get("top_10_themes_2025", {})
        
        # Map niches to competitors
        niche_mapping = {
            "luxury": ["rank_3_prestige", "rank_2_impact"],
            "fashion": ["rank_2_impact", "rank_8_impulse"],
            "furniture": ["rank_9_expanse"],
            "wellness": ["rank_6_refresh"],
            "watches": ["rank_3_prestige"],  # luxury watches
            "general": ["rank_1_dawn"]
        }
        
        # Find matching competitors
        competitor_keys = []
        for key, themes in niche_mapping.items():
            if key in niche:
                competitor_keys = themes
                break
        
        if not competitor_keys:
            competitor_keys = ["rank_1_dawn"]  # fallback
        
        # Extract features
        features = []
        themes = []
        for key in competitor_keys:
            theme_data = intel.get(key, {})
            themes.append(theme_data.get("name", key))
            features.extend(theme_data.get("key_features", []))
        
        return {
            "competitor_themes": themes,
            "key_features": list(set(features)),  # deduplicate
            "niche": niche
        }
    
    def _select_cro_patterns(self, niche: str, brief: str) -> Dict[str, Any]:
        """
        Select CRO patterns based on niche.
        
        Uses decision tree from 25_AXIS_CRO_SCIENTIST.json
        """
        scientist = self.cro_scientist.get("workflow", {}).get("phase_2_select_cro_patterns", {})
        decision_tree = scientist.get("decision_tree", {})
        
        # Determine archetype
        archetype = "if_fashion"  # default
        if "luxury" in niche or "watch" in niche:
            archetype = "if_luxury"
        elif "wellness" in niche or "health" in niche:
            archetype = "if_wellness"
        elif "b2b" in niche or "wholesale" in niche:
            archetype = "if_b2b"
        
        patterns_data = decision_tree.get(archetype, decision_tree.get("if_fashion", {}))
        
        return {
            "archetype": archetype.replace("if_", ""),
            "patterns": patterns_data.get("patterns", []),
            "avoid": patterns_data.get("avoid", [])
        }
    
    def _ask_output_path(self, theme_name: str) -> str:
        """
        Ask user where to create the theme.
        
        Options:
        1. Default: C:/Users/wiwal/Desktop/AXIS_Themes/{theme_name}
        2. Custom path (user input)
        """
        print("\n" + "="*60)
        print("📂 WHERE TO CREATE THE THEME?")
        print("="*60)
        
        default_path = f"C:/Users/wiwal/Desktop/AXIS_Themes/{theme_name}"
        
        print(f"\n1. Default: {default_path}")
        print("2. Custom path (you choose)")
        print("3. Current project output folder: output/{theme_name}")
        
        choice = input("\nEnter choice (1/2/3) [default: 1]: ").strip() or "1"
        
        if choice == "1":
            theme_root = default_path
        elif choice == "2":
            custom_path = input("Enter full path: ").strip()
            theme_root = os.path.join(custom_path, theme_name)
        else:
            theme_root = os.path.join(self.context.project_root, "output", theme_name)
        
        print(f"\n✅ Theme will be created at: {theme_root}\n")
        return theme_root
    
    def _generate_shopify_theme(self, theme_root: str, theme_name: str, brief: str, 
                                 niche: str, cro_plan: Dict, best_practices: Dict):
        """Generate complete Shopify theme with OS 2.0 structure."""
        
        # Build enhanced context for LLM
        context = f"""
        NICHE: {niche}
        ARCHETYPE: {cro_plan.get('archetype')}
        BEST PRACTICES FROM: {', '.join(best_practices.get('competitor_themes', []))}
        CRO PATTERNS TO APPLY: {', '.join(cro_plan.get('patterns', []))}
        AVOID: {', '.join(cro_plan.get('avoid', []))}
        """
        
        # 1. Config
        self._generate_file(theme_root, "config/settings_schema.json", brief, 
                          "Shopify settings_schema.json with theme customization options", context)
        
        # 2. Layout
        self._generate_file(theme_root, "layout/theme.liquid", brief,
                          "Shopify theme.liquid. Must include {{ content_for_header }}, {{ content_for_layout }}, performance optimizations", context)
        
        # 3. Assets (CSS + JS)
        self._generate_file(theme_root, "assets/base.css", brief,
                          f"Main CSS with design tokens for {niche}. Use CSS variables, mobile-first, performance budget < 50KB", context)
        
        self._generate_file(theme_root, "assets/theme.js", brief,
                          "Main JavaScript. Modular, < 100KB, no jQuery. Handle ATC, quick view, etc.", context)
        
        # 4. Sections
        sections = [
            ("header.liquid", "Header with logo, navigation, cart icon"),
            ("hero.liquid", f"Hero section optimized for {niche}. Include video/image toggle, CTA"),
            ("featured-collection.liquid", "Featured products grid with quick-add"),
            ("testimonials.liquid", "Social proof section with verified reviews"),
            ("footer.liquid", "Footer with links, newsletter, trust badges")
        ]
        
        for filename, description in sections:
            self._generate_file(theme_root, f"sections/{filename}", brief, description, context)
        
        # 5. Templates
        templates = [
            ("index.json", "Homepage template using sections"),
            ("product.json", "Product page template with CRO patterns"),
            ("collection.json", "Collection page with filtering"),
            ("cart.json", "Cart page with upsells")
        ]
        
        for filename, description in templates:
            self._generate_file(theme_root, f"templates/{filename}", brief, description, context)
        
        # 6. Snippets
        snippets = [
            ("product-card.liquid", "Reusable product card snippet"),
            ("icon-cart.liquid", "SVG cart icon"),
            ("price.liquid", "Price display with compare-at-price")
        ]
        
        for filename, description in snippets:
           self._generate_file(theme_root, f"snippets/{filename}", brief, description, context)
    
    def _generate_file(self, theme_root: str, relative_path: str, brief: str, 
                       file_description: str, niche_context: str = ""):
        """Generate a single file using LLM with comprehensive knowledge base context."""
        full_path = os.path.join(theme_root, relative_path)
        self.logger.info(f"  👉 Generating: {relative_path}...")
        
        # Extract niche from context
        niche = self._extract_niche_from_context(niche_context)
        
        # Build knowledge-enriched prompt
        knowledge_context = self._build_knowledge_context(relative_path, niche)
        
        prompt = f"""
        ACT AS: Senior E-Commerce Expert (10+ years: Shopify + UX + CRO + Psychology).
        
        TASK: Write code for '{relative_path}'
        
        PROJECT BRIEF: {brief}
        
        FILE PURPOSE: {file_description}
        
        {niche_context}
        
        KNOWLEDGE BASE CONTEXT:
        {knowledge_context}
        
        CRITICAL RULES:
        - Return ONLY the code. No markdown blocks, no explanations.
        - Follow Shopify OS 2.0 standards
        - Performance-first (lazy load images, minimal JS)
        - Accessible (WCAG 2.1 AA)
        - Mobile-first responsive design
        - Use modern CSS (Grid, Flexbox, CSS variables)
        - Apply psychology principles (see knowledge base)
        - Use effective copywriting (see formulas)
        - No jQuery, no Bootstrap
        
        OUTPUT: Pure code for {relative_path}
        """
        
        try:
            code = self.provider.generate(prompt)
            code = self._clean_response(code)
            
            # Write file
            self.orchestrator.execute_task({
                "type": "file_create",
                "name": f"Create {relative_path}",
                "details": {
                    "path": full_path,
                    "content": code
                }
            })
            
        except Exception as e:
            self.logger.error(f"  ❌ Failed to generate {relative_path}: {e}")
    
    
    def _extract_niche_from_context(self, context: str) -> str:
        """Extract niche keyword from context string."""
        niches = ["luxury", "fashion", "furniture", "wellness", "b2b", "watches"]
        for niche in niches:
            if niche in context.lower():
                return niche
        return "general"
    
    def _build_knowledge_context(self, file_path: str, niche: str) -> str:
        """Build enriched context from knowledge databases based on file type and niche."""
        context_parts = []
        
        # Determine file type
        if "hero" in file_path or "image-with-text" in file_path:
            # Hero section knowledge
            if self.theme_db_dawn:
                dawn_hero = self.theme_db_dawn.get("SECTIONS_LIBRARY", {}).get("hero_image_with_text", {})
                context_parts.append(f"HERO BEST PRACTICE (Dawn): {dawn_hero.get('purpose', '')} with responsive: {dawn_hero.get('responsive', '')}")
            
            if self.copywriting_db:
                headline = self.copywriting_db.get("HEADLINE_FORMULAS", {}).get("benefit_oriented", {})
                context_parts.append(f"HEADLINE FORMULA: {headline.get('formula', '')}")
        
        elif "product" in file_path or "main-product" in file_path:
            # Product page knowledge
            if self.psychology_db:
                niche_psych = self.psychology_db.get("NICHE_SPECIFIC_PSYCHOLOGY", {}).get(niche, {})
                context_parts.append(f"PSYCHOLOGY ({niche}): {niche_psych.get('copy_tone', '')} | CRO use: {niche_psych.get('cro_patterns', {}).get('use', [])}")
            
            if self.copywriting_db:
                product_desc = self.copywriting_db.get("PRODUCT_DESCRIPTIONS", {}).get("framework", "")
                context_parts.append(f"PRODUCT COPY FRAMEWORK: {product_desc}")
        
        elif "header" in file_path:
            # Header knowledge
            if self.theme_db_dawn:
                dawn_header = self.theme_db_dawn.get("SECTIONS_LIBRARY", {}).get("header", {})
                context_parts.append(f"HEADER COMPONENTS (Dawn): {dawn_header.get('components', [])}")
        
        elif ".css" in file_path or "base.css" in file_path:
            # Design patterns knowledge
            if self.design_patterns_schema:
                colors = self.design_patterns_schema.get("COLOR_SYSTEM", {})
                spacing = self.design_patterns_schema.get("SPACING_SYSTEM", {})
                context_parts.append(f"COLOR SYSTEM: Use semantic colors with psychology. SPACING: {spacing.get('scale', {})}. Follow mobile-first responsive design.")
        
        elif "footer" in file_path:
            # Retention patterns
            if self.retention_db:
                email_signup = self.retention_db.get("ON_SITE_RETENTION", {}).get("exit_intent_popups", {})
                context_parts.append(f"RETENTION: Include email signup with incentive. Exit-intent best practice: {email_signup}")
        
        # Add CTA guidance for all files
        if self.copywriting_db:
            ctas = self.copywriting_db.get("CTA_PATTERNS", {})
            value_cta = ctas.get("value_focused", {})
            context_parts.append(f"CTA BEST PRACTICE: {value_cta.get('variants', [])} (psychology: {value_cta.get('psychology', '')})")
        
        return "\n".join(context_parts) if context_parts else "Use best practices from knowledge base."
    
    def _clean_response(self, text: str) -> str:
        """Remove markdown code blocks from LLM response."""
        text = text.strip()
        
        # Remove opening ```language
        if text.startswith("```"):
            first_newline = text.find("\n")
            if first_newline != -1:
                text = text[first_newline+1:]
        
        # Remove closing ```
        if text.endswith("```"):
            text = text[:-3]
            
        return text.strip()
    
    def _generate_cro_report(self, theme_root: str, niche: str, cro_plan: Dict):
        """Generate CRO optimization report."""
        report = f"""
# CRO Optimization Report

**Niche:** {niche}
**Archetype:** {cro_plan.get('archetype', 'general')}

## Applied CRO Patterns
{chr(10).join('- ' + p for p in cro_plan.get('patterns', []))}

## Avoided Patterns (Not suitable for this niche)
{chr(10).join('- ' + p for p in cro_plan.get('avoid', []))}

## Estimated Conversion Lift
+20-30% vs generic theme (based on industry benchmarks)

## Recommended A/B Tests
1. Hero CTA color variations
2. Product page layout (sticky ATC vs standard)
3. Social proof placement (above vs below fold)

---
Generated by AXIS Studio CRO Scientist
"""
        
        report_path = os.path.join(theme_root, "CRO_REPORT.md")
        self.orchestrator.execute_task({
            "type": "file_create",
            "name": "Generate CRO Report",
            "details": {
                "path": report_path,
                "content": report
            }
        })
        
        print(f"\n📊 CRO Report generated: {report_path}\n")
