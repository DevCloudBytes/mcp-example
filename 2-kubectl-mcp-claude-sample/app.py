import gradio as gr
import subprocess
import logging
from command_sanitizer import validate_kubectl_command

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def execute_kubectl(command: str) -> str:
    """Safely execute kubectl commands"""
    try:
        if not validate_kubectl_command(command):
            return "Error: Invalid or dangerous command"
            
        result = subprocess.run(
            ["kubectl"] + command.split(),
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.stdout or result.stderr
    except Exception as e:
        logger.error(f"Command failed: {str(e)}")
        return f"Error: {str(e)}"

app = gr.Interface(
    fn=execute_kubectl,
    inputs=gr.Textbox(label="kubectl command (without 'kubectl')", placeholder="get pods -n default"),
    outputs=gr.Textbox(label="Command Output"),
    title="Kubernetes MCP Server",
    description="Safe kubectl command executor"
)

app.launch(
    server_name="0.0.0.0",
    server_port=7860,
    mcp_server=True  # This is critical for MCP support
)
