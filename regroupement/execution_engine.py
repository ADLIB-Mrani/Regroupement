"""
Execution Engine - Optionally executes the generated plan
"""
import subprocess
import os
from typing import Dict, Any, Optional


class ExecutionEngine:
    """Engine for executing implementation plans"""
    
    def __init__(self, auto_execute: bool = False, working_dir: Optional[str] = None):
        self.auto_execute = auto_execute
        self.working_dir = working_dir or os.getcwd()
        self.execution_log = []
        
    def execute_plan(self, plan: Dict[str, Any], dry_run: bool = True) -> Dict[str, Any]:
        """Execute the implementation plan"""
        
        if dry_run or not self.auto_execute:
            return {
                'executed': False,
                'dry_run': True,
                'message': 'Execution skipped (dry run mode). Plan displayed only.',
                'plan': plan.get('plan', '')
            }
        
        # In a real implementation, this would parse the plan and execute steps
        # For safety, we'll just return a simulation
        return {
            'executed': False,
            'dry_run': False,
            'message': 'Auto-execution disabled for safety. Review plan and execute manually.',
            'plan': plan.get('plan', '')
        }
    
    def execute_command(self, command: str, safe_mode: bool = True) -> Dict[str, Any]:
        """Execute a single command"""
        
        if safe_mode:
            return {
                'command': command,
                'executed': False,
                'output': None,
                'message': 'Safe mode enabled. Command not executed.'
            }
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self.working_dir,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            log_entry = {
                'command': command,
                'executed': True,
                'returncode': result.returncode,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'success': result.returncode == 0
            }
            
            self.execution_log.append(log_entry)
            return log_entry
            
        except Exception as e:
            log_entry = {
                'command': command,
                'executed': False,
                'error': str(e),
                'success': False
            }
            self.execution_log.append(log_entry)
            return log_entry
    
    def get_execution_log(self) -> list:
        """Get the execution log"""
        return self.execution_log
