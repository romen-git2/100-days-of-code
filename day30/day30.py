import requests
import time
import statistics
from dataclasses import dataclass, field
from typing import List

# metrics engine(brain)
@dataclass
class ServiceMetrics:
    target_url: str
    start_time: float = field(default_factory=time.time)
    latencies_ms: List[float] = field(default_factory=list)
    errors: int = 0
    
    def record_request(self, latency_ms: float, success: bool):
        if success:
            self.latencies_ms.append(latency_ms)
        else:
            self.errors += 1

    @property
    def current_uptime(self) -> float:
        return round(time.time() - self.start_time, 2)

    @property
    def request_count(self) -> int:
        return len(self.latencies_ms) + self.errors

    @property
    def average_latency(self) -> float:
        if not self.latencies_ms:
            return 0.0
        return round(statistics.mean(self.latencies_ms), 2)

    @property
    def max_latency(self) -> float:
        if not self.latencies_ms:
            return 0.0
        return round(max(self.latencies_ms), 2)

    @property
    def success_rate(self) -> float:
        total = self.request_count
        if total == 0:
            return 0.0
        # formula: (total - errors) / total
        return round(((total - self.errors) / total) * 100, 1)

    @property
    def status(self) -> str:
        """Determines health based on thresholds"""
        if self.errors > 0:
            return "DEGRADED(Errors Detected)"
        if self.average_latency > 300:
            return "SLOW(High Latency)"
        return "HEALTHY"

class UptimeAgent:
    def __init__(self, target_url: str):
        self.metrics = ServiceMetrics(target_url=target_url)
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "UptimeBot/1.0"})

    def ping(self):
        """Performs network check"""
        start = time.perf_counter()
        try:
            response = self.session.get(self.metrics.target_url, timeout=2)
            
            duration_ms = (time.perf_counter() - start) * 1000
            
            is_success = (response.status_code == 200)
            self.metrics.record_request(duration_ms, is_success)
            
            print(f"Ping: {response.status_code} | Latency: {duration_ms:.1f}ms")

        except requests.exceptions.RequestException:
            self.metrics.record_request(0.0, success=False)
            print("Ping: FAILED(Connection Error)")

    def generate_report(self):
        """Outputs the final dashboard"""
        m = self.metrics
        print(f"Target:       {m.target_url}")
        print(f"Status:       {m.status}")
        print(f"Total Pings:  {m.request_count}")
        print(f"Success Rate: {m.success_rate}%")
        print(f"Latency:      Avg: {m.average_latency}ms | Max: {m.max_latency}ms")
        print(f"Time Elapsed: {m.current_uptime}s")

if __name__ == "__main__":
    target = "https://www.google.com"
    
    bot = UptimeAgent(target)
    
    print(f"Starting Monitor on {target}...")

    try:
        for i in range(1, 6):
            print(f"[{i}/5]", end=" ")
            bot.ping()
            time.sleep(0.5) 
            
        bot.generate_report()

    except KeyboardInterrupt:
        print("Stopping monitor...")
        bot.generate_report()