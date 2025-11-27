import os
import re
import logging
from typing import List, Dict, Any

class SecurityScanner:
    """
    Security Scanner for AXIS Studio.
    Scans Liquid, JavaScript, and CSS files for common vulnerabilities.
    """
    
    def __init__(self):
        self.logger = logging.getLogger("SecurityScanner")
        self.violations: List[Dict[str, Any]] = []
        
    def scan_file(self, file_path: str) -> List[Dict[str, Any]]:
        """Scan a single file for security issues."""
        if not os.path.exists(file_path):
            self.logger.warning(f"File not found: {file_path}")
            return []
        
        file_violations = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        # Determine file type
        ext = os.path.splitext(file_path)[1]
        
        if ext == '.liquid':
            file_violations.extend(self._scan_liquid(lines, file_path))
        elif ext == '.js':
            file_violations.extend(self._scan_javascript(lines, file_path))
        elif ext == '.css':
            file_violations.extend(self._scan_css(lines, file_path))
            
        return file_violations
    
    def _scan_liquid(self, lines: List[str], file_path: str) -> List[Dict[str, Any]]:
        """Scan Liquid files for XSS vulnerabilities."""
        violations = []
        
        for i, line in enumerate(lines, 1):
            # Check for unescaped output
            # Dangerous: {{ user_input }} without filters
            if re.search(r'\{\{\s*[^}]*\s*\}\}', line):
                # Check if it has escape filter
                if not re.search(r'\|\s*escape', line):
                    violations.append({
                        'file': file_path,
                        'line': i,
                        'severity': 'WARNING',
                        'type': 'XSS',
                        'message': 'Potential XSS: Unescaped output detected. Consider using | escape filter.',
                        'code': line.strip()
                    })
            
            # Check for missing content_for_header
            if 'theme.liquid' in file_path and i < 20:
                if 'content_for_header' in line:
                    # Good, found it
                    pass
                    
        return violations
    
    def _scan_javascript(self, lines: List[str], file_path: str) -> List[Dict[str, Any]]:
        """Scan JavaScript files for dangerous patterns."""
        violations = []
        
        for i, line in enumerate(lines, 1):
            # Check for eval()
            if re.search(r'\beval\s*\(', line):
                violations.append({
                    'file': file_path,
                    'line': i,
                    'severity': 'CRITICAL',
                    'type': 'DANGEROUS_FUNCTION',
                    'message': 'Use of eval() is forbidden. This is a security risk.',
                    'code': line.strip()
                })
            
            # Check for innerHTML
            if re.search(r'\.innerHTML\s*=', line):
                violations.append({
                    'file': file_path,
                    'line': i,
                    'severity': 'WARNING',
                    'type': 'XSS',
                    'message': 'Use of innerHTML can lead to XSS. Consider using textContent or sanitization.',
                    'code': line.strip()
                })
            
            # Check for document.write
            if re.search(r'document\.write\s*\(', line):
                violations.append({
                    'file': file_path,
                    'line': i,
                    'severity': 'WARNING',
                    'type': 'BAD_PRACTICE',
                    'message': 'document.write() is deprecated and can cause issues.',
                    'code': line.strip()
                })
                
        return violations
    
    def _scan_css(self, lines: List[str], file_path: str) -> List[Dict[str, Any]]:
        """Scan CSS files for issues."""
        violations = []
        
        # CSS security issues are rare, but we can check for best practices
        for i, line in enumerate(lines, 1):
            # Check for !important overuse (code smell, not security)
            if line.count('!important') > 1:
                violations.append({
                    'file': file_path,
                    'line': i,
                    'severity': 'INFO',
                    'type': 'CODE_SMELL',
                    'message': 'Multiple !important declarations on one line. Consider refactoring.',
                    'code': line.strip()
                })
                
        return violations
    
    def scan_directory(self, directory: str) -> List[Dict[str, Any]]:
        """Recursively scan a directory."""
        all_violations = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(('.liquid', '.js', '.css')):
                    file_path = os.path.join(root, file)
                    violations = self.scan_file(file_path)
                    all_violations.extend(violations)
        
        return all_violations
    
    def generate_report(self, violations: List[Dict[str, Any]]) -> str:
        """Generate a human-readable security report."""
        if not violations:
            return "✅ No security violations found."
        
        report = f"🛡️ Security Scan Report\n"
        report += f"{'='*60}\n\n"
        
        # Group by severity
        critical = [v for v in violations if v['severity'] == 'CRITICAL']
        warnings = [v for v in violations if v['severity'] == 'WARNING']
        info = [v for v in violations if v['severity'] == 'INFO']
        
        if critical:
            report += f"🔴 CRITICAL ({len(critical)})\n"
            for v in critical:
                report += f"  {v['file']}:{v['line']} - {v['message']}\n"
            report += "\n"
        
        if warnings:
            report += f"🟡 WARNINGS ({len(warnings)})\n"
            for v in warnings:
                report += f"  {v['file']}:{v['line']} - {v['message']}\n"
            report += "\n"
        
        if info:
            report += f"ℹ️ INFO ({len(info)})\n"
            for v in info:
                report += f"  {v['file']}:{v['line']} - {v['message']}\n"
        
        return report


if __name__ == "__main__":
    # Example usage
    scanner = SecurityScanner()
    violations = scanner.scan_directory(".")
    print(scanner.generate_report(violations))
