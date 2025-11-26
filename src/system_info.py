"""
System Information Module
Retrieves CPU, GPU, RAM, and Storage statistics
"""

import psutil
import platform

class SystemInfo:
    def __init__(self):
        pass
    
    def get_cpu_usage(self):
        """Get CPU usage percentage"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """Get RAM usage percentage"""
        memory = psutil.virtual_memory()
        return memory.percent
    
    def get_memory_info(self):
        """Get detailed memory information"""
        memory = psutil.virtual_memory()
        return {
            "total": round(memory.total / (1024**3), 2),  # GB
            "available": round(memory.available / (1024**3), 2),  # GB
            "used": round(memory.used / (1024**3), 2),  # GB
            "percent": memory.percent
        }
    
    def get_disk_usage(self):
        """Get disk usage for C: drive"""
        disk = psutil.disk_usage('C:/')
        return {
            "total": round(disk.total / (1024**3), 2),  # GB
            "used": round(disk.used / (1024**3), 2),  # GB
            "free": round(disk.free / (1024**3), 2),  # GB
            "percent": disk.percent
        }
    
    def get_cpu_info(self):
        """Get CPU information"""
        return {
            "physical_cores": psutil.cpu_count(logical=False),
            "total_cores": psutil.cpu_count(logical=True),
            "max_frequency": psutil.cpu_freq().max if psutil.cpu_freq() else "N/A",
            "current_frequency": psutil.cpu_freq().current if psutil.cpu_freq() else "N/A"
        }
    
    def get_gpu_info(self):
        """
        Get GPU information (basic - requires additional libraries for detailed info)
        For more detailed GPU info, install: pip install GPUtil
        """
        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                return {
                    "name": gpu.name,
                    "load": f"{gpu.load * 100}%",
                    "memory_used": f"{gpu.memoryUsed}MB",
                    "memory_total": f"{gpu.memoryTotal}MB",
                    "temperature": f"{gpu.temperature}°C"
                }
        except ImportError:
            pass
        
        return {"info": "GPU monitoring not available. Install GPUtil for GPU stats."}
    
    def get_system_info(self):
        """Get general system information"""
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
    
    def get_all_stats(self):
        """Get all system statistics in one call"""
        disk = self.get_disk_usage()
        memory = self.get_memory_info()
        
        return {
            "cpu": self.get_cpu_usage(),
            "memory": self.get_memory_usage(),
            "memory_used": memory["used"],
            "memory_total": memory["total"],
            "disk_used": disk["used"],
            "disk_free": disk["free"],
            "disk_total": disk["total"]
        }