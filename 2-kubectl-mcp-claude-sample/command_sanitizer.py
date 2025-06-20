DANGEROUS_OPERATIONS = [
    "scale", "drain", "taint"
]

# DANGEROUS_OPERATIONS = [
#     "delete", "edit", "apply", 
#     "create", "patch", "replace",
#     "scale", "drain", "taint"
# ]


ALLOWED_NAMESPACES = ["default", "monitoring", "istio-system", "kube-system"]

def validate_kubectl_command(command: str) -> bool:
    """Validate kubectl commands against safety rules"""
    parts = command.lower().split()
    
    # Block dangerous operations
    if any(op in parts for op in DANGEROUS_OPERATIONS):
        return False
        
    # Validate namespace access
    if "-n" in parts:
        ns_index = parts.index("-n") + 1
        if ns_index < len(parts) and parts[ns_index] not in ALLOWED_NAMESPACES:
            return False
            
    # Allow only read operations
    allowed_verbs = ["get", "describe", "logs", "top", "cluster-info", "config view", "api-versions"]
    if not parts or parts[0] not in allowed_verbs:
        return False
        
    return True