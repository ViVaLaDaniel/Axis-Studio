import os
import json
import logging
from typing import Dict, Any, List

class PerformanceGovernor:
    """
    Performance Governor for AXIS Studio.
    Enforces performance budgets defined in 15_AXIS_PERFORMANCE_BUDGET.json.
    """
    
    def __init__(self, budget_file: str = None):
        self.logger = logging.getLogger("PerformanceGovernor")
        self.budget = self._load_budget(budget_file)
        
    def _load_budget(self, budget_file: str = None) -> Dict[str, Any]:
        """Load performance budget from JSON file."""
        if not budget_file:
            # Default location
            budget_file = os.path.join("04_EXECUTION_DEV", "15_AXIS_PERFORMANCE_BUDGET.json")
        
        if not os.path.exists(budget_file):
            self.logger.warning(f"Budget file not found: {budget_file}. Using defaults.")
            return self._default_budget()
        
        with open(budget_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _default_budget(self) -> Dict[str, Any]:
        """Default performance budget if file not found."""
        return {
            "javascript": {
                "max_size_kb": 150,
                "max_size_bytes": 150 * 1024
            },
            "css": {
                "max_size_kb": 100,  # Synced with 15_PERFORMANCE_BUDGET.json
                "max_size_bytes": 100 * 1024
            },
            "images": {
                "lcp_max_kb": 200,
                "lcp_max_bytes": 200 * 1024
            }
        }
    
    def check_file_size(self, file_path: str, file_type: str) -> Dict[str, Any]:
        """Check if a file meets the performance budget."""
        if not os.path.exists(file_path):
            return {
                'status': 'ERROR',
                'message': f'File not found: {file_path}'
            }
        
        file_size = os.path.getsize(file_path)
        file_size_kb = file_size / 1024
        
        budget_key = file_type.lower()
        if budget_key not in self.budget:
            return {
                'status': 'UNKNOWN',
                'message': f'No budget defined for file type: {file_type}'
            }
        
        max_size = self.budget[budget_key].get('max_size_bytes', float('inf'))
        
        if file_size > max_size:
            return {
                'status': 'FAIL',
                'file': file_path,
                'size_kb': round(file_size_kb, 2),
                'budget_kb': max_size / 1024,
                'message': f'File exceeds budget: {file_size_kb:.2f} KB > {max_size/1024:.2f} KB'
            }
        else:
            return {
                'status': 'PASS',
                'file': file_path,
                'size_kb': round(file_size_kb, 2),
                'budget_kb': max_size / 1024,
                'message': f'File within budget: {file_size_kb:.2f} KB <= {max_size/1024:.2f} KB'
            }
    
    def check_directory(self, directory: str) -> List[Dict[str, Any]]:
        """Check all JS and CSS files in a directory."""
        results = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                if file.endswith('.js'):
                    result = self.check_file_size(file_path, 'javascript')
                    results.append(result)
                elif file.endswith('.css'):
                    result = self.check_file_size(file_path, 'css')
                    results.append(result)
        
        return results
    
    def generate_report(self, results: List[Dict[str, Any]]) -> str:
        """Generate a performance report."""
        if not results:
            return "ℹ️ No files to check."
        
        report = f"⚡ Performance Budget Report\n"
        report += f"{'='*60}\n\n"
        
        passed = [r for r in results if r['status'] == 'PASS']
        failed = [r for r in results if r['status'] == 'FAIL']
        
        if failed:
            report += f"❌ FAILED ({len(failed)})\n"
            for r in failed:
                report += f"  {r['file']}: {r['size_kb']} KB (Budget: {r['budget_kb']} KB)\n"
            report += "\n"
        
        if passed:
            report += f"✅ PASSED ({len(passed)})\n"
            for r in passed:
                report += f"  {r['file']}: {r['size_kb']} KB (Budget: {r['budget_kb']} KB)\n"
        
        return report


if __name__ == "__main__":
    # Example usage
    governor = PerformanceGovernor()
    results = governor.check_directory(".")
    print(governor.generate_report(results))
