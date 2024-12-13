#!/usr/bin/env python
import sys
from content_creation.crew import ContentCreationCrew

def run():
    """
    Run the Content Creation Crew with dynamic inputs
    """
    inputs = {
        'content_type': sys.argv[1] if len(sys.argv) > 1 else 'blog post',
        'target_audience': sys.argv[2] if len(sys.argv) > 2 else 'tech professionals',
        'tone': sys.argv[3] if len(sys.argv) > 3 else 'professional',
        'style': sys.argv[4] if len(sys.argv) > 4 else 'informative',
        'primary_topic': sys.argv[5] if len(sys.argv) > 5 else 'AI trends'
    }
    
    print("Content Creation Inputs:")
    for key, value in inputs.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    crew = ContentCreationCrew().crew()
    result = crew.kickoff(inputs=inputs)
    
    print("\nContent Creation Complete!")
    print("Output files can be found in the 'output' directory:")
    print("1. trend_research.md")
    print("2. content_strategy.md")
    print("3. content_draft.md")
    print("4. optimized_content.md")

if __name__ == "__main__":
    run()
