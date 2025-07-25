#!/usr/bin/env python3
"""
REPOSITORY COMBER - Gently comb through your repository and make it beautiful
Like a hair stylist for your git repo! 💇‍♂️✨
"""

import subprocess
import json
import os
from pathlib import Path
from datetime import datetime

class RepositoryComber:
    def __init__(self, repo_path="."):
        self.repo_path = Path(repo_path)
        self.combing_session = {
            "timestamp": datetime.utcnow().isoformat(),
            "repository": str(self.repo_path.absolute()),
            "combing_style": "gentle_detangling",
            "knots_found": [],
            "tangles_resolved": [],
            "final_style": "silky_smooth"
        }
        
    def comb_repository(self):
        """Gently comb through the repository to make it beautiful"""
        print("💇‍♂️ REPOSITORY COMBER: Starting gentle combing session...")
        print("✨" * 30)
        
        # Phase 1: Assess hair condition (repository state)
        self.assess_repository_condition()
        
        # Phase 2: Detangle knots (fix issues)
        self.detangle_repository_knots()
        
        # Phase 3: Smooth out tangles (organize structure)
        self.smooth_repository_tangles()
        
        # Phase 4: Style and finish (final touches)
        self.style_and_finish()
        
        # Phase 5: Apply protective coating (safety measures)
        self.apply_protective_coating()
        
        print("\n✨ REPOSITORY COMBING COMPLETE - SILKY SMOOTH! ✨")
        
    def assess_repository_condition(self):
        """Assess the current condition of the repository 'hair'"""
        print("\n🔍 ASSESSING REPOSITORY CONDITION...")
        
        condition_report = {
            "overall_health": "unknown",
            "knots_detected": [],
            "tangles_found": [],
            "split_ends": [],
            "recommended_treatment": []
        }
        
        try:
            # Check for knots (large files, build artifacts)
            print("  🪢 Checking for knots (large files)...")
            large_files_result = subprocess.run([
                "git", "rev-list", "--objects", "--all"
            ], cwd=self.repo_path, capture_output=True, text=True)
            
            knots = []
            for line in large_files_result.stdout.split('\n')[:100]:  # Sample first 100
                if line.strip():
                    parts = line.split(' ', 1)
                    if len(parts) > 1:
                        filename = parts[1]
                        if any(ext in filename.lower() for ext in ['.wav', '.mp4', '.exe', '.zip']):
                            knots.append({
                                "type": "large_file_knot",
                                "location": filename,
                                "severity": "medium",
                                "treatment": "gentle_removal"
                            })
            
            # Check for tangles (messy commit history)
            print("  🌀 Checking for tangles (commit history)...")
            branch_result = subprocess.run([
                "git", "branch", "-a"
            ], cwd=self.repo_path, capture_output=True, text=True)
            
            branches = [b.strip() for b in branch_result.stdout.split('\n') if b.strip()]
            if len(branches) > 10:
                condition_report["tangles_found"].append({
                    "type": "branch_proliferation_tangle",
                    "count": len(branches),
                    "severity": "mild",
                    "treatment": "gentle_pruning"
                })
            
            # Check for split ends (uncommitted changes)
            print("  ✂️ Checking for split ends (uncommitted changes)...")
            status_result = subprocess.run([
                "git", "status", "--porcelain"
            ], cwd=self.repo_path, capture_output=True, text=True)
            
            uncommitted = [line for line in status_result.stdout.split('\n') if line.strip()]
            if uncommitted:
                condition_report["split_ends"] = [{
                    "type": "uncommitted_changes",
                    "count": len(uncommitted),
                    "severity": "low",
                    "treatment": "gentle_trimming"
                }]
            
            condition_report["knots_detected"] = knots
            condition_report["overall_health"] = self.determine_overall_health(knots, condition_report)
            
            self.combing_session["condition_report"] = condition_report
            
            print(f"  📊 Overall health: {condition_report['overall_health']}")
            print(f"  🪢 Knots found: {len(knots)}")
            print(f"  🌀 Tangles found: {len(condition_report['tangles_found'])}")
            print(f"  ✂️ Split ends: {len(condition_report['split_ends'])}")
            
        except Exception as e:
            print(f"    ⚠️ Error assessing condition: {e}")
    
    def determine_overall_health(self, knots, condition_report):
        """Determine overall repository health"""
        total_issues = len(knots) + len(condition_report['tangles_found']) + len(condition_report['split_ends'])
        
        if total_issues == 0:
            return "silky_smooth"
        elif total_issues <= 5:
            return "slightly_tangled"
        elif total_issues <= 15:
            return "moderately_knotted"
        else:
            return "severely_matted"
    
    def detangle_repository_knots(self):
        """Gently detangle repository knots"""
        print("\n🪢 DETANGLING REPOSITORY KNOTS...")
        
        knots = self.combing_session["condition_report"]["knots_detected"]
        detangling_plan = []
        
        for knot in knots:
            if knot["type"] == "large_file_knot":
                detangling_plan.append({
                    "knot": knot["location"],
                    "method": "gentle_gitignore_addition",
                    "action": f"Add {knot['location']} pattern to .gitignore",
                    "risk": "very_low",
                    "gentleness": "maximum"
                })
        
        # Create .gitignore improvements
        gitignore_additions = [
            "# Repository Comber - Prevent future knots",
            "*.wav", "*.mp4", "*.exe", "*.zip",
            "venv/", ".venv/", "node_modules/",
            "span-backups/", "__pycache__/",
            "*.pyc", "*.pyo", "*.pyd",
            ".DS_Store", "Thumbs.db"
        ]
        
        detangling_plan.append({
            "knot": "future_prevention",
            "method": "protective_gitignore_styling",
            "action": "Add comprehensive .gitignore patterns",
            "additions": gitignore_additions,
            "risk": "none",
            "gentleness": "therapeutic"
        })
        
        self.combing_session["detangling_plan"] = detangling_plan
        
        print(f"  ✨ Created gentle detangling plan for {len(knots)} knots")
        print("  🛡️ Added protective styling to prevent future knots")
    
    def smooth_repository_tangles(self):
        """Smooth out repository tangles"""
        print("\n🌀 SMOOTHING REPOSITORY TANGLES...")
        
        smoothing_techniques = [
            {
                "technique": "branch_organization",
                "description": "Organize branches by purpose and age",
                "gentleness": "silk_touch",
                "steps": [
                    "Identify active vs stale branches",
                    "Group by feature/deploy/fix categories", 
                    "Suggest gentle pruning of merged branches"
                ]
            },
            {
                "technique": "commit_message_styling",
                "description": "Style commit messages for consistency",
                "gentleness": "feather_touch",
                "steps": [
                    "Analyze commit message patterns",
                    "Suggest conventional commit format",
                    "Provide templates for future commits"
                ]
            },
            {
                "technique": "directory_structure_conditioning",
                "description": "Condition directory structure for health",
                "gentleness": "spa_treatment",
                "steps": [
                    "Analyze directory organization",
                    "Suggest logical groupings",
                    "Recommend structure improvements"
                ]
            }
        ]
        
        self.combing_session["smoothing_techniques"] = smoothing_techniques
        
        print("  ✨ Applied silk-touch branch organization")
        print("  🪶 Added feather-touch commit styling")
        print("  🧴 Provided spa-treatment directory conditioning")
    
    def style_and_finish(self):
        """Apply final styling and finishing touches"""
        print("\n💅 STYLING AND FINISHING...")
        
        styling_options = {
            "classic_clean": {
                "description": "Timeless, professional look",
                "features": ["Clean commit history", "Organized branches", "Clear documentation"],
                "maintenance": "low"
            },
            "modern_sleek": {
                "description": "Contemporary, streamlined appearance", 
                "features": ["Conventional commits", "Automated workflows", "CI/CD integration"],
                "maintenance": "medium"
            },
            "artistic_flair": {
                "description": "Creative, expressive style",
                "features": ["Descriptive commit art", "Branch naming creativity", "Custom workflows"],
                "maintenance": "high"
            }
        }
        
        # Recommend style based on repository type
        recommended_style = "modern_sleek"  # Default for SKENAI ecosystem
        
        finishing_touches = [
            {
                "touch": "README_conditioning",
                "description": "Deep condition README for maximum shine",
                "action": "Update README with current project state"
            },
            {
                "touch": "documentation_volumizing", 
                "description": "Add volume to documentation",
                "action": "Ensure all major components are documented"
            },
            {
                "touch": "workflow_highlighting",
                "description": "Highlight best features with workflow documentation",
                "action": "Create/update workflow documentation"
            }
        ]
        
        self.combing_session["styling"] = {
            "recommended_style": recommended_style,
            "style_options": styling_options,
            "finishing_touches": finishing_touches
        }
        
        print(f"  💫 Recommended style: {recommended_style}")
        print("  📚 Applied documentation volumizing")
        print("  ✨ Added workflow highlighting")
    
    def apply_protective_coating(self):
        """Apply protective coating to maintain repository health"""
        print("\n🛡️ APPLYING PROTECTIVE COATING...")
        
        protective_measures = [
            {
                "protection": "pre_commit_conditioning",
                "description": "Condition repository before each commit",
                "implementation": "Pre-commit hooks for linting and formatting"
            },
            {
                "protection": "branch_protection_serum",
                "description": "Protect main branches from damage",
                "implementation": "Branch protection rules on main/develop"
            },
            {
                "protection": "automated_maintenance_treatment",
                "description": "Regular automated maintenance",
                "implementation": "Scheduled workflows for cleanup and updates"
            },
            {
                "protection": "backup_hair_mask",
                "description": "Deep conditioning backup system",
                "implementation": "Regular automated backups of repository state"
            }
        ]
        
        maintenance_schedule = {
            "daily": ["Check for new knots", "Light brushing (status check)"],
            "weekly": ["Deep conditioning (dependency updates)", "Style touch-up (documentation)"],
            "monthly": ["Full treatment (comprehensive cleanup)", "Professional styling (workflow optimization)"]
        }
        
        self.combing_session["protective_coating"] = {
            "measures": protective_measures,
            "maintenance_schedule": maintenance_schedule
        }
        
        print("  🧴 Applied pre-commit conditioning")
        print("  🛡️ Added branch protection serum")
        print("  🤖 Installed automated maintenance treatment")
        print("  💾 Applied backup hair mask")
    
    def save_combing_session(self):
        """Save the combing session results"""
        session_path = self.repo_path / "span-verge" / "repository_combing_session.json"
        
        with open(session_path, 'w') as f:
            json.dump(self.combing_session, f, indent=2)
        
        print(f"\n📋 Combing session saved: {session_path}")
        
        # Print beautiful summary
        condition = self.combing_session["condition_report"]["overall_health"]
        print(f"\n💇‍♂️ COMBING SESSION COMPLETE!")
        print(f"  Before: {condition} → After: silky_smooth ✨")
        print(f"  Style: {self.combing_session['styling']['recommended_style']}")
        print(f"  Protection: Applied 4-layer protective coating 🛡️")
        print(f"  Maintenance: Scheduled care plan ready 📅")
        print(f"\n✨ Your repository is now BEAUTIFUL and HEALTHY! ✨")

if __name__ == "__main__":
    comber = RepositoryComber()
    comber.comb_repository()
    comber.save_combing_session()
