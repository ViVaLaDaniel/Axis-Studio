"""
Theme Analyzer — Automated Knowledge Base Builder for AXIS Studio.

This tool analyzes Shopify themes and generates detailed JSON decompositions
for the knowledge base (00_CORE_BRAIN/THEME_DB_*.json).

Usage:
    python src/utils/theme_analyzer.py --theme dawn --source github --url https://github.com/Shopify/dawn
    python src/utils/theme_analyzer.py --batch top10  # Analyze all top 10 themes
"""

import os
import json
import re
import logging
from pathlib import Path
from typing import Dict, Any, List
import subprocess


class ThemeAnalyzer:
    """
    Analyzes Shopify themes and generates knowledge base entries.
    
    Process:
    1. Download theme (GitHub or demo store)
    2. Parse file structure
    3. Extract settings_schema
    4. Analyze sections, snippets, components
    5. Generate JSON decomposition
    """
    
    def __init__(self, output_dir: str = "00_CORE_BRAIN"):
        self.logger = logging.getLogger("ThemeAnalyzer")
        self.output_dir = output_dir
        
        # Load schema template
        schema_path = os.path.join(output_dir, "THEME_DECOMPOSITION_SCHEMA.json")
        with open(schema_path, 'r', encoding='utf-8') as f:
            self.schema_template = json.load(f)
    
    def analyze_theme(self, theme_name: str, theme_path: str) -> Dict[str, Any]:
        """
        Analyze a theme directory and generate full decomposition.
        
        Args:
            theme_name: Name of the theme (e.g., 'Dawn', 'Impact')
            theme_path: Path to theme directory
            
        Returns:
            Complete theme decomposition JSON
        """
        self.logger.info(f"Analyzing theme: {theme_name} at {theme_path}")
        
        decomposition = {
            "THEME_METADATA": self._analyze_metadata(theme_name, theme_path),
            "FILE_STRUCTURE": self._analyze_file_structure(theme_path),
            "SECTIONS_LIBRARY": self._analyze_sections(theme_path),
            "COMPONENTS_LIBRARY": self._analyze_components(theme_path),
            "UX_PATTERNS": self._detect_ux_patterns(theme_path),
            "SETTINGS_ANALYSIS": self._analyze_settings(theme_path),
            "PERFORMANCE_PROFILE": self._analyze_performance(theme_path)
        }
        
        return decomposition
    
    def _analyze_metadata(self, theme_name: str, theme_path: str) -> Dict[str, Any]:
        """Extract theme metadata."""
        metadata = {
            "name": theme_name,
            "last_analyzed": "2025-11-27",
            "shopify_version": "OS 2.0"
        }
        
        # Try to read config/settings_schema.json for theme info
        settings_path = os.path.join(theme_path, "config", "settings_schema.json")
        if os.path.exists(settings_path):
            with open(settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)
                # Extract theme_info if present
                for item in settings:
                    if item.get("name") == "theme_info":
                        metadata.update({
                            "version": item.get("theme_version", "1.0.0"),
                            "developer": item.get("theme_author", "Unknown")
                        })
        
        return metadata
    
    def _analyze_file_structure(self, theme_path: str) -> Dict[str, Any]:
        """Analyze directory structure and file counts."""
        structure = {
            "directories": {
                "assets": self._count_files(theme_path, "assets"),
                "config": self._count_files(theme_path, "config"),
                "layout": self._count_files(theme_path, "layout"),
                "sections": self._count_files(theme_path, "sections"),
                "snippets": self._count_files(theme_path, "snippets"),
                "templates": self._count_files(theme_path, "templates")
            }
        }
        
        # Analyze bundle sizes
        assets_path = os.path.join(theme_path, "assets")
        if os.path.exists(assets_path):
            structure["directories"]["assets"]["total_css_size_kb"] = self._calculate_size(assets_path, ".css")
            structure["directories"]["assets"]["total_js_size_kb"] = self._calculate_size(assets_path, ".js")
        
        return structure
    
    def _count_files(self, base_path: str, subdir: str) -> Dict[str, Any]:
        """Count files in a directory."""
        dir_path = os.path.join(base_path, subdir)
        if not os.path.exists(dir_path):
            return {"count": 0, "files": []}
        
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
        return {
            "count": len(files),
            "files": files
        }
    
    def _calculate_size(self, dir_path: str, extension: str) -> int:
        """Calculate total size of files with given extension (in KB)."""
        total_size = 0
        for file in os.listdir(dir_path):
            if file.endswith(extension):
                file_path = os.path.join(dir_path, file)
                total_size += os.path.getsize(file_path)
        return total_size // 1024  # Convert to KB
    
    def _analyze_sections(self, theme_path: str) -> Dict[str, Any]:
        """Analyze all sections and extract schemas."""
        sections_path = os.path.join(theme_path, "sections")
        if not os.path.exists(sections_path):
            return {}
        
        sections = {}
        for filename in os.listdir(sections_path):
            if filename.endswith(".liquid"):
                section_name = filename.replace(".liquid", "")
                section_data = self._parse_section_file(os.path.join(sections_path, filename))
                sections[section_name] = section_data
        
        return sections
    
    def _parse_section_file(self, file_path: str) -> Dict[str, Any]:
        """Parse a Liquid section file and extract schema."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract schema using regex
        schema_match = re.search(r'{%\s*schema\s*%}(.*?){%\s*endschema\s*%}', content, re.DOTALL)
        
        section_data = {
            "file": file_path,
            "schema_settings": {},
            "blocks": []
        }
        
        if schema_match:
            try:
                schema_json = json.loads(schema_match.group(1))
                section_data["schema_settings"] = schema_json.get("settings", [])
                section_data["blocks"] = schema_json.get("blocks", [])
            except json.JSONDecodeError:
                self.logger.warning(f"Could not parse schema in {file_path}")
        
        return section_data
    
    def _analyze_components(self, theme_path: str) -> Dict[str, Any]:
        """Analyze reusable components (snippets)."""
        snippets_path = os.path.join(theme_path, "snippets")
        if not os.path.exists(snippets_path):
            return {}
        
        components = {}
        key_components = ["product-card", "price", "icon", "card"]
        
        for filename in os.listdir(snippets_path):
            if filename.endswith(".liquid"):
                # Check if it's a key component
                for key in key_components:
                    if key in filename:
                        component_name = filename.replace(".liquid", "")
                        components[component_name] = {
                            "file": f"snippets/{filename}",
                            "purpose": f"Reusable {key} component"
                        }
        
        return components
    
    def _detect_ux_patterns(self, theme_path: str) -> Dict[str, Any]:
        """Detect UX patterns by analyzing JS and Liquid files."""
        patterns = {}
        
        # Check for common patterns
        assets_path = os.path.join(theme_path, "assets")
        if os.path.exists(assets_path):
            js_files = [f for f in os.listdir(assets_path) if f.endswith(".js")]
            
            # Detect patterns based on filenames
            pattern_indicators = {
                "sticky_header": ["sticky", "header"],
                "drawer_cart": ["cart-drawer", "cart-notification"],
                "predictive_search": ["predictive-search", "search"],
                "quick_view": ["quick-view", "quick-add"]
            }
            
            for pattern_name, keywords in pattern_indicators.items():
                for keyword in keywords:
                    if any(keyword in js_file for js_file in js_files):
                        patterns[pattern_name] = {
                            "detected": True,
                            "implementation": f"JS file containing '{keyword}'"
                        }
                        break
        
        return patterns
    
    def _analyze_settings(self, theme_path: str) -> Dict[str, Any]:
        """Analyze settings_schema.json."""
        settings_path = os.path.join(theme_path, "config", "settings_schema.json")
        if not os.path.exists(settings_path):
            return {"total_settings": 0}
        
        with open(settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
        
        total_settings = 0
        categories = []
        
        for item in settings:
            if "settings" in item:
                setting_count = len(item["settings"])
                total_settings += setting_count
                categories.append({
                    "name": item.get("name", "Unnamed"),
                    "settings_count": setting_count
                })
        
        return {
            "total_settings": total_settings,
            "categories": categories
        }
    
    def _analyze_performance(self, theme_path: str) -> Dict[str, Any]:
        """Analyze performance characteristics."""
        assets_path = os.path.join(theme_path, "assets")
        
        profile = {
            "bundle_sizes": {
                "css_total_kb": 0,
                "js_total_kb": 0
            },
            "optimizations": []
        }
        
        if os.path.exists(assets_path):
            profile["bundle_sizes"]["css_total_kb"] = self._calculate_size(assets_path, ".css")
            profile["bundle_sizes"]["js_total_kb"] = self._calculate_size(assets_path, ".js")
            
            # Detect optimizations
            all_files = os.listdir(assets_path)
            if any("webp" in f.lower() for f in all_files):
                profile["optimizations"].append("Uses WebP images")
            if any("lazy" in f.lower() for f in all_files):
                profile["optimizations"].append("Lazy loading implemented")
        
        return profile
    
    def save_decomposition(self, theme_name: str, decomposition: Dict[str, Any]):
        """Save theme decomposition to JSON file."""
        output_file = os.path.join(self.output_dir, f"THEME_DB_{theme_name.upper()}.json")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(decomposition, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"✅ Saved decomposition to {output_file}")
        print(f"\n✅ Theme analysis complete: {output_file}")
    
    def download_theme_github(self, repo_url: str, target_dir: str):
        """Download theme from GitHub."""
        self.logger.info(f"Cloning theme from {repo_url}")
        
        # Use git clone
        subprocess.run(["git", "clone", repo_url, target_dir], check=True)
        
        self.logger.info(f"✅ Theme downloaded to {target_dir}")


def main():
    """CLI entry point."""
    import argparse
    
    logging.basicConfig(level=logging.INFO)
    
    parser = argparse.ArgumentParser(description="Analyze Shopify themes for knowledge base")
    parser.add_argument("--theme", type=str, help="Theme name (e.g., 'Dawn')")
    parser.add_argument("--path", type=str, help="Path to theme directory")
    parser.add_argument("--github", type=str, help="GitHub repo URL (optional, for download)")
    parser.add_argument("--output", type=str, default="00_CORE_BRAIN", help="Output directory")
    
    args = parser.parse_args()
    
    analyzer = ThemeAnalyzer(output_dir=args.output)
    
    # If GitHub URL provided, download first
    if args.github:
        download_path = f"temp_{args.theme}"
        analyzer.download_theme_github(args.github, download_path)
        theme_path = download_path
    else:
        theme_path = args.path
    
    if not theme_path:
        print("Error: Provide either --path or --github")
        return
    
    # Analyze theme
    decomposition = analyzer.analyze_theme(args.theme, theme_path)
    
    # Save to knowledge base
    analyzer.save_decomposition(args.theme, decomposition)


if __name__ == "__main__":
    main()
