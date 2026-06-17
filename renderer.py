class Renderer:
    def render(self, entry: dict) -> str:
        if entry['severity'] == 'Requires Professional Service':
            md = f"### Diagnosis: {entry['fault_category']}\n\n"
            md += "> **Verdict: Beyond DIY repair. Safety risks involved. Professional repair or replacement recommended.**\n\n"
        else:
            md = f"### Diagnosis: {entry['fault_category']}\n\n"
            md += f"**Estimated Time**: {entry['est_time_min']} mins | **Severity**: {entry['severity']}\n\n"
            
        if entry.get('safety_notes'):
            md += "#### Safety Warnings\n"
            for note in entry['safety_notes']:
                md += f"- **{note}**\n"
            md += "\n"
            
        md += "#### Possible Causes\n"
        md += ", ".join(entry['possible_causes']) + "\n\n"
        
        md += "#### Solution Steps\n"
        for i, step in enumerate(entry['solution_steps'], 1):
            md += f"{i}. {step}\n"
        md += "\n"
            
        if entry.get('tools'):
            md += f"**Tools Required**: {', '.join(entry['tools'])}\n"
            
        return md
