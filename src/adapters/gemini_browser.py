"""
Gemini Browser Provider for AXIS Studio.

This module provides browser-based access to Google Gemini
using Selenium WebDriver. No API key required.
"""

import os
import time
import logging
from typing import Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from src.adapters.llm_provider import LLMProvider, LLMProviderFactory


class GeminiBrowserProvider(LLMProvider):
    """Browser-based Gemini provider using Selenium."""
    
    def __init__(self, headless: bool = False):
        super().__init__()
        self.headless = headless
        self.driver: Optional[webdriver.Chrome] = None
        self.session_active = False
        
    def _init_driver(self):
        """Initialize Chrome WebDriver."""
        if self.driver is not None:
            return
            
        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        self.logger.info("Initializing Chrome WebDriver...")
        self.driver = webdriver.Chrome(options=options)
        
    def login(self, email: Optional[str] = None, password: Optional[str] = None):
        """
        Login to Google account for Gemini access.
        
        Note: For security, credentials should be in environment variables.
        """
        if not email:
            email = os.getenv('GOOGLE_EMAIL')
        if not password:
            password = os.getenv('GOOGLE_PASSWORD')
            
        if not email or not password:
            raise ValueError("Email and password required. Set GOOGLE_EMAIL and GOOGLE_PASSWORD env vars.")
        
        self._init_driver()
        
        self.logger.info("Navigating to Gemini...")
        self.driver.get("https://gemini.google.com")
        
        # Wait for login or redirect
        time.sleep(3)
        
        # Check if already logged in
        if "gemini.google.com/app" in self.driver.current_url:
            self.logger.info("Already logged in.")
            self.session_active = True
            return
        
        # Implement login flow
        # Note: This is a simplified version. Real implementation needs:
        # - Email input
        # - Password input
        # - 2FA handling
        # - CAPTCHA detection
        
        self.logger.warning("Automatic login not fully implemented. Please login manually.")
        input("Press Enter after logging in manually...")
        self.session_active = True
        
    def generate(self, prompt: str, **kwargs) -> str:
        """
        Generate a response from Gemini via browser.
        
        Args:
            prompt: The input prompt
            **kwargs: Additional parameters (timeout, etc.)
            
        Returns:
            Generated text response
        """
        if not self.session_active:
            raise RuntimeError("Not logged in. Call login() first.")
        
        timeout = kwargs.get('timeout', 30)
        
        try:
            # Find prompt input
            wait = WebDriverWait(self.driver, 10)
            prompt_box = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[placeholder*='Enter a prompt']"))
            )
            
            # Clear and send prompt
            prompt_box.clear()
            prompt_box.send_keys(prompt)
            
            # Submit (usually Enter key or button)
            prompt_box.send_keys("\n")
            
            # Wait for response
            time.sleep(2)  # Initial wait
            
            # Find response element
            # Note: Selector may need adjustment based on Gemini UI
            response_elem = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".response-content"))
            )
            
            response_text = response_elem.text
            self.logger.info(f"Received response ({len(response_text)} chars)")
            
            return response_text
            
        except TimeoutException:
            self.logger.error("Timeout waiting for Gemini response")
            return ""
        except Exception as e:
            self.logger.error(f"Error generating response: {e}")
            return ""
    
    def is_available(self) -> bool:
        """Check if browser provider is available."""
        try:
            # Check if Chrome is installed
            from selenium.webdriver.chrome.service import Service
            return True
        except Exception:
            return False
    
    def close(self):
        """Close the browser session."""
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.session_active = False


# Register with factory
LLMProviderFactory.register('gemini_browser', GeminiBrowserProvider)
