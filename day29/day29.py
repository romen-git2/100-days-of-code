import logging
import json
import time
import uuid
import requests

# JSON formatter
class StructuredFormatter(logging.Formatter):
    """
    The Translator that turns Python log objects into JSON strings
    """
    def format(self, record: logging.LogRecord) -> str:
        log_obj = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "line": record.lineno
        }

        if hasattr(record, "context"):
            log_obj.update(record.context)

        if record.exc_info:
            log_obj["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_obj)
    
def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(StructuredFormatter())
        logger.addHandler(handler)
        
        file_handler = logging.FileHandler("agent_audit.jsonl")
        file_handler.setFormatter(StructuredFormatter())
        logger.addHandler(file_handler)
        
    return logger

class NetworkAgent:
    def __init__(self):
        self.logger = get_logger("NetWatch")
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "AgentBot/1.0"})

    def audit_url(self, url: str):
        # generate a trace id
        trace_id = str(uuid.uuid4())[:8]
        
        # log intent
        self.logger.info(f"Checking URL: {url}", extra={"context": {
            "event": "audit_start",
            "trace_id": trace_id,
            "target_url": url
        }})

        start_time = time.perf_counter()

        try:
            response = self.session.get(url, timeout=5)
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

            # log success with metrics
            self.logger.info("Request successful", extra={"context": {
                "event": "audit_success",
                "trace_id": trace_id,
                "status_code": response.status_code,
                "latency_ms": duration_ms,
                "content_size_bytes": len(response.content),
                "server": response.headers.get("Server", "Unknown")
            }})

        except requests.exceptions.Timeout:
            # log timeout
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            self.logger.error("Request timed out", extra={"context": {
                "event": "audit_timeout",
                "trace_id": trace_id,
                "latency_ms": duration_ms,
                "timeout_limit": 5
            }})

        except requests.exceptions.RequestException as e:
            # log crash(DNS errors, connection refused etc.)
            self.logger.error("Network failure", exc_info=True, extra={"context": {
                "event": "audit_failure",
                "trace_id": trace_id,
                "error_type": type(e).__name__
            }})

if __name__ == "__main__":
    bot = NetworkAgent()
    
    targets = [
        "https://api.github.com",       
        "https://httpbin.org/delay/2",   
        "https://this-site-is-fake.xyz" 
    ]

    print("Starting Agent Audit...")
    for target in targets:
        bot.audit_url(target)