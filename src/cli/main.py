import argparse
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.orchestrator import AxisOrchestrator

def main():
    parser = argparse.ArgumentParser(
        description='AXIS Studio CLI - Autonomous AI System for Shopify Themes'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # axis run
    run_parser = subparsers.add_parser('run', help='Run the orchestrator')
    
    # axis init
    init_parser = subparsers.add_parser('init', help='Initialize a new AXIS project')
    
    # axis status
    status_parser = subparsers.add_parser('status', help='Check system status')
    
    # axis generate
    generate_parser = subparsers.add_parser('generate', help='Generate code using LLM')
    generate_parser.add_argument('prompt', type=str, help='Generation prompt')
    generate_parser.add_argument('--provider', type=str, default='gemini',
                                 help='LLM provider to use')
    
    # axis create-theme
    theme_parser = subparsers.add_parser('create-theme', help='Create a new Shopify theme')
    theme_parser.add_argument('brief', type=str, help='Theme brief (e.g. "Minimalist fashion store")')
    theme_parser.add_argument('--name', type=str, default='my-axis-theme', help='Theme directory name')
    theme_parser.add_argument('--provider', type=str, default='gemini', help='LLM provider')
    
    args = parser.parse_args()
    
    if args.command == 'run':
        print("🚀 Starting AXIS Orchestrator...")
        orchestrator = AxisOrchestrator()
        orchestrator.run()
    elif args.command == 'init':
        print("🔧 Initializing AXIS project...")
        print("(Not implemented yet)")
    elif args.command == 'status':
        print("✅ AXIS Studio v10.5 - Scientific Edition")
        print("📂 Project Root: ./")
        print("🧠 Brain: 00_CORE_BRAIN")
        print("⚙️ Runtime: src/")
    elif args.command == 'generate':
        print(f"🤖 Generating with {args.provider}...")
        try:
            from src.adapters.llm_provider import LLMProviderFactory
            provider = LLMProviderFactory.create(args.provider)
            
            if not provider.is_available():
                print(f"❌ Provider '{args.provider}' is not available.")
                return
            
            print(f"📝 Prompt: {args.prompt}")
            response = provider.generate(args.prompt)
            print(f"\n✨ Response:\n{response}")
            
            if hasattr(provider, 'close'):
                provider.close()
                
        except Exception as e:
            print(f"❌ Error: {e}")
            
    elif args.command == 'create-theme':
        print(f"🏭 Starting Theme Factory: '{args.name}'")
        try:
            from src.core.generator import ThemeGenerator
            generator = ThemeGenerator(args.provider)
            
            generator.generate_theme(args.brief, args.name)
            
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
