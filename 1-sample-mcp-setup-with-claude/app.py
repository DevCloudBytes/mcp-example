import gradio as gr
import math
import logging
import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Console output
        logging.FileHandler('projectile_calculator.log')  # File output
    ]
)

logger = logging.getLogger(__name__)

logger.info("="*50)
logger.info(f"Projectile Calculator Server v1.0")
logger.info(f"Started at {datetime.datetime.now()}")
logger.info("="*50)


def compute_projectile_distance(initial_speed, angle, target_distance):
    """
    Calculate the horizontal distance traveled by a projectile and determine if it hits the target.
    
    Parameters:
    initial_speed (float): Initial speed of the projectile in m/s
    angle (float): Launch angle in degrees
    target_distance (float): Distance to the target in meters
    
    Returns:
    tuple: (distance traveled, hit/miss message)
    """
    # Convert angle from degrees to radians
    angle_rad = math.radians(angle)
    
    # Gravitational acceleration (m/s²)
    g = 9.81
    
    # Calculate the horizontal distance
    distance = (initial_speed**2 * math.sin(2 * angle_rad)) / g
    
    # Determine if the projectile hits the target (with 1m tolerance)
    hit = abs(distance - target_distance) <= 1.0
    result = "Yes, it will hit Sam!" if hit else "No, it won't reach Sam."
    
    
    logger.info(f"Result: distance={distance:.2f}m, hit={hit}")
    
    return distance, result

app = gr.Interface(
    fn=compute_projectile_distance,
    inputs=[
        gr.Number(label="Initial Speed (m/s)"),
        gr.Number(label="Launch Angle (degrees)"),
        gr.Number(label="Target Distance (m)")
    ],
    outputs=[
        gr.Number(label="Distance Traveled (m)"),
        gr.Textbox(label="Will it hit Sam?")
    ],
    title="Projectile Hit Calculator",
    description="Calculate if a projectile will hit a target based on initial speed and launch angle."
)

# Launch with MCP server configuration
app.launch(
    server_name="0.0.0.0",
    server_port=7860,
    share=True,
    mcp_server=True
)